def nickname_generator(name):
    return "Error: Name too short" if len(name) < 4 else name[:3] if name[2] not in 'aeiou'else name[:4]