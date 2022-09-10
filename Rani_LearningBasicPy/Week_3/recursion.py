def count_boxes():
    if robot.sense_color() == '':
        return 0
    else:
        robot.lift_up()
        if robot.sense_color() == '':
            return 0
        else:
            robot.lift_up()
            if robot.sense_color() == '':
                return 0
            else:
                robot.lift_up()
                num_above = count_boxes()
                robot.lift_down()
                return 1 + num_above
            robot.lift_down()
            return 1 + num_above
        robot.lift_down()
        return 1 + num_above

while True:
    robot.lift_up()
    num_above += 1
    robot.lift_down()
    if robot.sense_color() == "":
        break

while True:
    print(count)
    if count == 50:
        continue
    count+=1