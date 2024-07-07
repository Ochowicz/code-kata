def growing_plant(up_speed, down_speed, desired_height):
    height = up_speed
    n = 1
    while height < desired_height:
        height += - down_speed + up_speed
        n += 1
    return n