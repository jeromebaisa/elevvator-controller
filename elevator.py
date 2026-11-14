# Elevator Controller

# Elevator starts at floor 1
state = "AT_FLOOR1"

while True:
    try:
        event = input().strip()
    except EOFError:
        break

# Floor 1 to Floor 3
    if state == "AT_FLOOR1":
        if event == "CAR_FLOOR3":
            print("CLOSE_DOOR")
            print("MOVE_UP_FAST")
            state = "MOVING_UP_TO_FLOOR3"

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

# Arriving at Floor 3
    elif state == "SLOWING_UP_TO_FLOOR3":
        if event == "AT_FLOOR3":
            print("STOP")
            print("OPEN_DOOR")
            state = "AT_FLOOR3"

 # Arriving at Floor 2
    elif state == "SLOWING_UP_TO_FLOOR2":
        if event == "AT_FLOOR2":
            print("STOP")
            print("OPEN_DOOR")
            state = "AT_FLOOR2"

# Floor 2 to Floor 3
    elif state == "AT_FLOOR2":
        if event == "CAR_FLOOR3":
            print("CLOSE_DOOR")
            print("MOVE_UP_FAST")
            state = "MOVING_FLOOR2_TO_FLOOR3"

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
