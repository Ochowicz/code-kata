# Your job is to find the gravitational force between two spherical objects (obj1 , obj2).
#
# input
# Two arrays are given :
#
# arr_val (value array), consists of 3 elements
# 1st element : mass of obj 1
# 2nd element : mass of obj 2
# 3rd element : distance between their centers
# arr_unit (unit array), consists of 3 elements
# 1st element : unit for mass of obj 1
# 2nd element : unit for mass of obj 2
# 3rd element : unit for distance between their centers
# mass units are :
#
# kilogram (kg)
# gram (g)
# milligram (mg)
# microgram (μg)
# pound (lb)
# distance units are :
#
# meter (m)
# centimeter (cm)
# millimeter (mm)
# micrometer (μm)
# feet (ft)
# Note
# value of G = 6.67 × 10−11 N⋅kg−2⋅m2
#
# 1 ft = 0.3048 m
#
# 1 lb = 0.453592 kg
#
# return value must be Newton for force (obviously)
#
# μ copy this from here to use it in your solution
def solution(arr_val, arr_unit):
    G = 6.67e-11  # Gravitational constant in N⋅kg−2⋅m2

    # Mass conversion factors
    mass_units = {
        "kg": 1,
        "g": 1e-3,
        "mg": 1e-6,
        "μg": 1e-9,
        "lb": 0.453592
    }

    # Distance conversion factors
    distance_units = {
        "m": 1,
        "cm": 1e-2,
        "mm": 1e-3,
        "μm": 1e-6,
        "ft": 0.3048
    }

    # Extract values and units
    m1, m2, r = arr_val
    unit_m1, unit_m2, unit_r = arr_unit

    # Convert mass and distance to base units (kg and m)
    m1_kg = m1 * mass_units[unit_m1]
    m2_kg = m2 * mass_units[unit_m2]
    r_m = r * distance_units[unit_r]

    # Calculate force
    force = G * m1_kg * m2_kg / (r_m ** 2)

    return force