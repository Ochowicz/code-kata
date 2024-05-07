def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed/2
    if you_speed != 0 and shark_speed != 0:
        if pontoon_distance / you_speed > shark_distance / shark_speed:
            return "Shark Bait!"
        else:
            return "Alive!"