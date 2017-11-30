state = [1, 2, 3]
state_temp = []*3
state_saved = []*3

while True:
    for index in range(3):
        state[index] += 1
    state_temp = state
    print(state)
    print(state_temp)
    print(state_saved)
    print()
    if state_temp != state_saved:
        stable = 0
    state_saved = state_temp
