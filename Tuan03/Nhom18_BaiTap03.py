def straight_line_equation_passing_two_points(point_a: tuple, point_b: tuple):
    normal_vector = ((point_a[1] - point_b[1]), (point_b[0] - point_a[0])) # Vecto phap tuyen
    a = normal_vector[0]   #Vecto phap tuyen
    b = normal_vector[1]
    c = - ((-point_a[0]) * a + (-point_a[1]) * b)
    return (a, b, c)

#print(straight_line_equation_passing_two_points((1,1), (2,3)))

def is_aligned(point_a: tuple, point_b: tuple, point_c: tuple):
    vector_ab = ((point_b[0] - point_a[0]), (point_b[1] - point_a[1]), (point_b[2] - point_a[2]))
    vector_ac = ((point_c[0] - point_a[0]), (point_c[1] - point_a[1]), (point_c[2] - point_a[2]))
    k = vector_ab[0] / vector_ac[0]
    if (vector_ac[1] * k == vector_ab[1] and vector_ac[2] * k == vector_ab[2]):
        return True
    else:
        return False

def plane_equation_passing_three_points(point_a: tuple, point_b: tuple, point_c: tuple):
    if (not is_aligned(point_a, point_b, point_c)):
        vector_ab = ((point_b[0] - point_a[0]), (point_b[1] - point_a[1]), (point_b[2] - point_a[2]))
        vector_ac = ((point_c[0] - point_a[0]), (point_c[1] - point_a[1]), (point_c[2] - point_a[2]))
        normal_vector = ((vector_ab[1] * vector_ac[2] - vector_ab[2] * vector_ac[1]), (vector_ab[2] * vector_ac[0] - vector_ab[0] * vector_ac[2]), (vector_ab[0] * vector_ac[1] - vector_ab[1] * vector_ac[0]))
        a = normal_vector[0]
        b = normal_vector[1]
        c = normal_vector[2]
        d = -(normal_vector[0] * (-point_a[0]) + normal_vector[1] * (-point_a[1]) + normal_vector[2] * (-point_a[2]))
    return (a, b, c, d)

print(plane_equation_passing_three_points((2,1,1), (4,2,3), (1,2,2)))
