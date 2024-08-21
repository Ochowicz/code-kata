def killer(suspect_info, dead):
    for suspect, seen in suspect_info.items():
        if all(person in seen for person in dead):
            return suspect