def starting_mark(height):
    # Define the two guidelines
    guideline_1 = (1.52, 9.45)
    guideline_2 = (1.83, 10.67)

    # Calculate the slope (rate of change)
    slope = (guideline_2[1] - guideline_1[1]) / (guideline_2[0] - guideline_1[0])

    # Calculate the y-intercept (constant offset)
    intercept = guideline_1[1] - slope * guideline_1[0]

    # Calculate the starting mark using linear interpolation
    starting_mark = slope * height + intercept

    # Round the result to two decimal places
    starting_mark = round(starting_mark, 2)

    return starting_mark