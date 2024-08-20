def fly_by(lamps, drone):
    return len(drone) * 'o' + (len(lamps) - len(drone)) * 'x' if len(lamps) >= len(drone) else len(lamps) * 'o'