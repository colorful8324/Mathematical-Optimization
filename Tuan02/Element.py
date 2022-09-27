def is_included(list: list, element):
    for i in list:
        if i == element:
            return True
    return False

def filtered_elements(A: list, B: list):
    C = []
    for i in A:
        if not is_included(B, i):
            C.append(i)
    return C

A = {1,2,3,4,5,6,7}
B = {2,4,6,8,10,12}
C = {13,14,15}
D = {}
print(filtered_elements(D, A))
print(filtered_elements(A, B))
print(filtered_elements(A, C))

