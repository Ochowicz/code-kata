def remove_rotten(bag_of_fruits):
    if bag_of_fruits == None:
        return []
    return [fruit[6:].lower() if fruit.startswith('rotten') else fruit for fruit in bag_of_fruits]