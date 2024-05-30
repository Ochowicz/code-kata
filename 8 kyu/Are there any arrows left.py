def any_arrows(arrows):
    if not arrows: return False
    for arrow in arrows:
        if not 'damaged' in arrow or not arrow['damaged']:
            return True
    return False