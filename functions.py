import math
O = 0.7
C = 0.78
H = 0.35
N = 0.71            #these are the covalent radii of the atoms


def connection_checker(first_array, second_array):     #args are arrays with type of atom and coordinates e.g.: ["C", 23.0, 18.9, 14.3]
    
    if first_array[0] == 'O':
        first_radius = 0.7

    elif first_array[0] == 'C':
        first_radius = 0.78

    elif first_array[0] == 'N':
        first_radius = 0.71
    else:
        first_radius = 0.35

    first_x = float(first_array[1])
    first_y = float(first_array[2])
    first_z = float(first_array[3])


    if second_array[0] == 'O':
        second_radius = 0.7
    elif second_array[0] == 'C':
        second_radius = 0.78
    elif second_array[0] == 'N':
        second_radius = 0.71
    else:
        second_radius = 0.35

    second_x = float(second_array[1])
    second_y = float(second_array[2])
    second_z = float(second_array[3])
    d = math.sqrt((first_x-second_x)**2 + (first_y-second_y)**2 + (first_z-second_z)**2)
    if (first_radius + second_radius >= d) and d != 0:
        return 1
    return 0


