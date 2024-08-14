def crap(garden, bags, cap):
    flattened_garden = [item for sublist in garden for item in sublist]
    return 'Dog!!' if 'D' in flattened_garden else 'Clean' if flattened_garden.count('@') <= bags * cap else 'Cr@p'