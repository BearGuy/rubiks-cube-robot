import sys

class ColourDetection:

    def get_color_name(self, hsv):
        """ Get the name of the color based on the hue.

        :returns: string
        """
        (h,s,v) = hsv
        #print((h,s,v))

        # h values (theoretical)
        # red = 0
        # orange = 15
        # yellow = 30
        # green = 60
        # blue = 120

        # h values (in lab)
        # red = 0,1,2
        # orange = 3,4,5
        # yellow = 35
        # green = 70
        # blue = 100

        if s < 80:
            return 'white'

        elif v < 50:
            return 'black'

        elif h < 3:
            return 'red'
        elif h >= 3 and h < 15:
            return 'orange'
        elif h > 25 and h < 45:
            return 'yellow'
        elif h > 55 and h < 80:
            return 'green'
        elif h > 90 and h < 130:
            return 'blue'
        else:
            return 'purple'

    def name_to_rgb(self, name):
        """
        Get the main RGB color for a name.

        :param name: the color name that is requested
        :returns: tuple
        """
        color = {
            'red'    : (0,0,255),
            'orange' : (0,165,255),
            'blue'   : (255,0,0),
            'green'  : (0,255,0),
            'white'  : (255,255,255),
            'yellow' : (0,255,255),
            'black'  : (0,0,0),
            'purple' : (128,0,128)
        }
        return color[name]

    def color_to_notation(self, color):
        """
        Return the notation from a specific color.
        We want a user to have green in front, white on top,
        which is the usual.

        :param color: the requested color
        """
        notation = {
            'green'  : 'F',
            'white'  : 'U',
            'blue'   : 'B',
            'red'    : 'R',
            'orange' : 'L',
            'yellow' : 'D',
            'black'  : 'X',
            'purple' : 'P'
        }
        return notation[color]

    def average_hsv(self, roi):
        """ Average the HSV colors in a region of interest.

        :param roi: the image array
        :returns: tuple
        """
        h   = 0
        s   = 0
        v   = 0
        num = 0
        for y in range(len(roi)):
            if y % 10 == 0:
                for x in range(len(roi[y])):
                    if x % 10 == 0:
                        chunk = roi[y][x]
                        num += 1
                        h += chunk[0]
                        s += chunk[1]
                        v += chunk[2]
        h /= num
        s /= num
        v /= num
        return (int(h), int(s), int(v))
