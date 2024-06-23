def over_the_road(address, n):
    if address % 2 == 0:
        row = n - address/2 + 1
        return 1 + (row - 1) * 2
    if address % 2 != 0:
        row = (address + 1) / 2
        return (n - row + 1) * 2