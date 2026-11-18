# Elevator Controller Simulator

# Elevator starts at Floor 1
state = "AT_FLOOR1"

pending_requests = []

while True:
    try:
        event = input().strip()
    except EOFError:
        break

    # Remember requests while elevator is moving
    if state != "AT_FLOOR1" and state != "AT_FLOOR2" and state != "AT_FLOOR3":

        if event == "CAR_FLOOR1" or event == "FLOOR1_UP":
            if 1 not in pending_requests:
                pending_requests.append(1)

        elif event == "CAR_FLOOR2" or event == "FLOOR2_UP" or event == "FLOOR2_DOWN":
            if 2 not in pending_requests:
                pending_requests.append(2)

        elif event == "CAR_FLOOR3" or event == "FLOOR3_DOWN":
            if 3 not in pending_requests:
                pending_requests.append(3)

# Floor 1 to Floor 3
    if state == "AT_FLOOR1":
        if event == "CAR_FLOOR3" or event == "FLOOR3_DOWN":
            print("CLOSE_DOOR")
            print("MOVE_UP_FAST")
            state = "MOVING_UP_TO_FLOOR3"

        elif event == "CAR_FLOOR2" or event == "FLOOR2_UP" or event == "FLOOR2_DOWN":
            print("CLOSE_DOOR")
            print("MOVE_UP_FAST")
            state = "MOVING_UP_TO_FLOOR2"

        elif event == "FLOOR1_UP" or event == "CAR_FLOOR1":
            print("OPEN_DOOR")

# Slow down when nearing Floor 3
    elif state == "MOVING_UP_TO_FLOOR3":
        if event == "BETWEEN_2_3":
            print("MOVE_UP_SLOW")
            state = "SLOWING_UP_TO_FLOOR3"

# Stop at Floor 3
    elif state == "SLOWING_UP_TO_FLOOR3":
        if event == "AT_FLOOR3":
            print("STOP")
            print("OPEN_DOOR")
            state = "AT_FLOOR3"

# Moving toward Floor 2
    elif state == "MOVING_UP_TO_FLOOR2":
        if event == "BETWEEN_1_2":
            print("MOVE_UP_SLOW")
            state = "SLOWING_UP_TO_FLOOR2"
# Arriving at Floor 2
    elif state == "SLOWING_UP_TO_FLOOR2":
        if event == "AT_FLOOR2":
            print("STOP")
            print("OPEN_DOOR")
            state = "AT_FLOOR2"
# Elevator stopped at Floor 2
    elif state == "AT_FLOOR2":

# Floor 2 to Floor 3
        if event == "CAR_FLOOR3" or event == "FLOOR3_DOWN":
            print("CLOSE_DOOR")
            print("MOVE_UP_FAST")
            state = "MOVING_FLOOR2_TO_FLOOR3"

# Floor 2 to Floor 1
        elif event == "CAR_FLOOR1" or event == "FLOOR1_UP":
            print("CLOSE_DOOR")
            print("MOVE_DOWN_FAST")
            state = "MOVING_FLOOR2_TO_FLOOR1"

        elif event == "FLOOR2_UP" or event == "FLOOR2_DOWN" or event == "CAR_FLOOR2":
            print("OPEN_DOOR")
            
# Slow down when approaching Floor 3
    elif state == "MOVING_FLOOR2_TO_FLOOR3":
        if event == "BETWEEN_2_3":
            print("MOVE_UP_SLOW")
            state = "SLOWING_FLOOR2_TO_FLOOR3"

# Stop at Floor 3
    elif state == "SLOWING_FLOOR2_TO_FLOOR3":
        if event == "AT_FLOOR3":
            print("STOP")
            print("OPEN_DOOR")
            state = "AT_FLOOR3"

# Floor 3 to Floor 2
    elif state == "AT_FLOOR3":
        if event == "CAR_FLOOR2" or event == "FLOOR2_UP" or event == "FLOOR2_DOWN":
            print("CLOSE_DOOR")
            print("MOVE_DOWN_FAST")
            state = "MOVING_FLOOR3_TO_FLOOR2"

        elif event == "CAR_FLOOR1" or event == "FLOOR1_UP":
            print("CLOSE_DOOR")
            print("MOVE_DOWN_FAST")
            state = "MOVING_FLOOR3_TO_FLOOR1"

        elif event == "FLOOR3_DOWN" or event == "CAR_FLOOR3":
            print("OPEN_DOOR")

# Slow down when approaching Floor 2
    elif state == "MOVING_FLOOR3_TO_FLOOR2":
        if event == "BETWEEN_2_3":
            print("MOVE_DOWN_SLOW")
            state = "SLOWING_FLOOR3_TO_FLOOR2"

# Stop at Floor 2
    elif state == "SLOWING_FLOOR3_TO_FLOOR2":
        if event == "AT_FLOOR2":
            print("STOP")
            print("OPEN_DOOR")
            state = "AT_FLOOR2"

# Moving from Floor 2 to Floor 1
    elif state == "MOVING_FLOOR2_TO_FLOOR1":
        if event == "BETWEEN_1_2":
            print("MOVE_DOWN_SLOW")
            state = "SLOWING_FLOOR2_TO_FLOOR1"

# Arriving at Floor 1
    elif state == "SLOWING_FLOOR2_TO_FLOOR1":
        if event == "AT_FLOOR1":
            print("STOP")
            print("OPEN_DOOR")
            state = "AT_FLOOR1"

# Moving from Floor 3 to Floor 1
    elif state == "MOVING_FLOOR3_TO_FLOOR1":
        if event == "BETWEEN_1_2":
            print("MOVE_DOWN_SLOW")
            state = "SLOWING_FLOOR3_TO_FLOOR1"

# Arriving at Floor 1
    elif state == "SLOWING_FLOOR3_TO_FLOOR1":
        if event == "AT_FLOOR1":
            print("STOP")
            print("OPEN_DOOR")
            state = "AT_FLOOR1"

    # Process pending requests after arriving at a floor
    while pending_requests and (state == "AT_FLOOR1" or state == "AT_FLOOR2" or state == "AT_FLOOR3"):

        next_floor = pending_requests.pop(0)

        if state == "AT_FLOOR1":
            if next_floor == 2:
                print("CLOSE_DOOR")
                print("MOVE_UP_FAST")
                state = "MOVING_UP_TO_FLOOR2"

            elif next_floor == 3:
                print("CLOSE_DOOR")
                print("MOVE_UP_FAST")
                state = "MOVING_UP_TO_FLOOR3"

        elif state == "AT_FLOOR2":
            if next_floor == 1:
                print("CLOSE_DOOR")
                print("MOVE_DOWN_FAST")
                state = "MOVING_FLOOR2_TO_FLOOR1"

            elif next_floor == 3:
                print("CLOSE_DOOR")
                print("MOVE_UP_FAST")
                state = "MOVING_FLOOR2_TO_FLOOR3"

        elif state == "AT_FLOOR3":
            if next_floor == 1:
                print("CLOSE_DOOR")
                print("MOVE_DOWN_FAST")
                state = "MOVING_FLOOR3_TO_FLOOR1"

            elif next_floor == 2:
                print("CLOSE_DOOR")
                print("MOVE_DOWN_FAST")
                state = "MOVING_FLOOR3_TO_FLOOR2"
