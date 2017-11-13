import sys
import cv2
import time

from colordetection import ColourDetection
from controller import Control

class Video:

    def __init__(self):
        self.cam              = cv2.VideoCapture(0)
        self.stickers         = self.get_sticker_coordinates('main')
        self.current_stickers = self.get_sticker_coordinates('current')
        self.postview_stickers = self.get_sticker_coordinates('postview')
        self.colour = ColourDetection()

    def get_sticker_coordinates(self, name):
        """
        Every array has 2 values: x and y.
        Grouped per 3 since on the cam will be
        3 rows of 3 stickers.

        :param name: the requested sticker type
        :returns: list
        """
        stickers = {
            'main': [
                [200, 120], [300, 120], [400, 120],
                [200, 220], [300, 220], [400, 220],
                [200, 320], [300, 320], [400, 320]
            ],
            'current': [
                [20, 20], [54, 20], [88, 20],
                [20, 54], [54, 54], [88, 54],
                [20, 88], [54, 88], [88, 88]
            ],
            'postview': [
                [20, 130], [54, 130], [88, 130],
                [20, 164], [54, 164], [88, 164],
                [20, 198], [54, 198], [88, 198]
            ]
        }
        return stickers[name]


    def draw_main_stickers(self, frame):
        """Draws the 9 stickers in the frame."""
        for x,y in self.stickers:
            cv2.rectangle(frame, (x,y), (x+30, y+30), (255,255,255), 2)

    def draw_current_stickers(self, frame, state):
        """Draws the 9 current stickers in the frame."""
        for index,(x,y) in enumerate(self.current_stickers):
            cv2.rectangle(frame, (x,y), (x+32, y+32), self.colour.name_to_rgb(state[index]), -1)

    def draw_postview_stickers(self, frame, state):
        """Draws the 9 postview stickers in the frame."""
        for index,(x,y) in enumerate(self.postview_stickers):
            cv2.rectangle(frame, (x,y), (x+32, y+32), self.colour.name_to_rgb(state[index]), -1)

    def scan(self):
        """
        Open up the webcam and scans the 9 regions in the center
        and show a postview in the left upper corner.

        After hitting the space bar to confirm, the block below the
        current stickers shows the current state that you have.
        This is show every user can see what the computer toke as input.

        :returns: dictionary
        """

        sides   = {}
        postview = ['white','white','white',
                   'white','white','white',
                   'white','white','white']
        state = ['white','white','white',
                 'white','white','white',
                 'white','white','white']

        while True:
            _, frame = self.cam.read()
            #frame = cv2.flip(frame,0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            key = cv2.waitKey(10) & 0xff

            # init certain stickers.
            self.draw_main_stickers(frame)
            self.draw_postview_stickers(frame, postview)

            for index,(x,y) in enumerate(self.stickers):
                roi          = hsv[y:y+32, x:x+32]
                avg_hsv      = self.colour.average_hsv(roi)
                color_name   = self.colour.get_color_name(avg_hsv)
                state[index] = color_name

            # update when space bar is pressed.
            if key == 32:
                postview = list(state)
                self.draw_postview_stickers(frame, state)
                face = self.colour.color_to_notation(state[4])
                notation = [self.colour.color_to_notation(color) for color in state]
                sides[face] = notation

            # show the new stickers
            self.draw_current_stickers(frame, state)

            # append amount of scanned sides
            text = 'scanned sides: {}/6'.format(len(sides))
            cv2.putText(frame, text, (20, 460), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

            # quit on escape.
            if key == 27:
                break

            # show result
            cv2.imshow("default", frame)

        self.cam.release()
        cv2.destroyAllWindows()
        if len(sides) == 6:
            return sides
        else:
            return False

    def scan_headless(self):
        """
        Open up the webcam and scans the 9 regions in the center
        and show a postview in the left upper corner.

        After hitting the space bar to confirm, the block below the
        current stickers shows the current state that you have.
        This is show every user can see what the computer toke as input.

        :returns: dictionary
        """

        state = ['white','white','white',
                 'white','white','white',
                 'white','white','white']
        state_saved = ['white','white','white',
                       'white','white','white',
                       'white','white','white']

        while True:
            _, frame = self.cam.read()
            key = cv2.waitKey(10) & 0xff
            #frame = cv2.flip(frame,0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            ready = False

            # init certain stickers.
            self.draw_main_stickers(frame)
            self.draw_postview_stickers(frame, state)

            for index,(x,y) in enumerate(self.stickers):
                sticker      = hsv[y:y+32, x:x+32]
                avg_hsv      = self.colour.average_hsv(sticker)
                color_name   = self.colour.get_color_name(avg_hsv)
                state[index] = color_name

            timer = time.time()
            if int(timer) % 1 == 0 and int(timer) % 2 != 0:
                state_saved = state
            if int(timer) % 2 == 0:
                if state == state_saved:
                    ready = True
            for color in state:
                if color == 'black' or color == 'purple':
                    ready = False

            # show result
            cv2.imshow("default", frame)

            # update when space bar is pressed.
            if ready:  # need to determine when to save cube face
                #face = self.colour.color_to_notation(state[4])  # get center colour
                notation = [self.colour.color_to_notation(color) for color in state]
                break


        #self.cam.release()
        cv2.destroyAllWindows()
        return notation

    def find_state(self):
        
        sides = {}

        control = Control()
        control.linear_front.move(0)
        control.linear_back.move(0)

        notation_1 = self.scan_headless()
        print(notation_1)
        control.rotate_2(control.motor_right, control.motor_left, 90)
        notation_2 = self.scan_headless()
        print(notation_2)
        control.rotate_2(control.motor_right, control.motor_left, 90)
        notation_3 = self.scan_headless()
        print(notation_3)
        control.rotate_2(control.motor_right, control.motor_left, 90)
        notation_4 = self.scan_headless()
        print(notation_4)

        control.linear_front.move(1)
        control.linear_back.move(1)

        control.linear_right.move(0)
        control.linear_left.move(0)
        control.rotate_2(control.motor_right, control.motor_left, 90)

        control.rotate_2(control.motor_back, control.motor_front, 90)
        notation_5 = self.scan_headless()
        print(notation_5)

        control.rotate_2(control.motor_back, control.motor_front, 180)
        notation_6 = self.scan_headless()
        print(notation_6)

        control.rotate_2(control.motor_back, control.motor_front, 90)

        control.linear_right.move(1)
        control.linear_left.move(1)

        control.linear_front.move(0)
        control.linear_back.move(0)

        control.rotate_2(control.motor_right, control.motor_left, 90)

        control.linear_front.move(1)
        control.linear_back.move(1)

        control.linear_right.move(0)
        control.linear_left.move(0)
        control.rotate_2(control.motor_right, control.motor_left, 90)
        control.linear_right.move(1)
        control.linear_left.move(1)

        sides[notation_1[4]] = notation_1
        sides[notation_2[4]] = notation_2
        sides[notation_3[4]] = notation_3
        sides[notation_4[4]] = notation_4
        sides[notation_5[4]] = notation_5
        sides[notation_6[4]] = notation_6

        self.cam.release()

        if len(sides) == 6:
            return sides
        else:
            return False
