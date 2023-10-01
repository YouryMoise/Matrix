import random
from random import choice

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

def matrix_det(matrix):
    """
    Arg: A square matrix, written as a 2D list of lists
    Returns: The determinant of the matrix
    """
    #return the only element if size is 1
    if len(matrix) == 1:
        return matrix[0][0]

    #make sure matrix is square
    assert all(len(row) == len(matrix) for row in matrix), "Must be a square matrix"
    det = 0
    multiplier = 1

    #recursively use the determinant formula(first column
    #entries multiplied by determinant of cofactors) to 
    #find the determinant
    for row in matrix:
        rest = [roww[1:] for roww in matrix if row is not roww]
        det += multiplier*row[0]*matrix_det(rest)
        multiplier*=-1
    return det

def create_rand_matrix(size):
    """
    Arg: size(int), the size of the matrix we want
    Returns: a matrix(list of lists) of size size with every entry
    from 1 to size^2 inclusive in a random order
    """
    used_set = set()
    matrix = [
        [0 for i in range(size)] for i in range(size)
    ]
    #loop through the matrix, replacing each 0 entry with a random value
    #from 1 to size^2 that is not in the used_set
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            temp = choice([i for i in range(1,size**2+1) if i not in used_set])
            used_set.add(temp)
            matrix[j][k] = temp
    return matrix

def create_n_matrices(n,size):
    """
    Arg: n(int), the number of matrices to make
    Returns: A list of n unique matrices
    """
    used_set = set()
    matrices_found = []
    assert n <= factorial(size**2), f'There are not {n} unique {size} by {size} matrices'
    #create a matrix, if it is not in the used_set,
    #add it to matrices_found; otherwise create new matrices
    #until a new one is found and add it
    #repeat this n times
    for i in range(n):
        go = False
        while not go:
            m = create_rand_matrix(size)
            if str(m) not in used_set:
                used_set.add(str(m))
                matrices_found.append(m)
                go = True
    return matrices_found



def find_max_det(size):
    ms_to_test = create_n_matrices(factorial(size**2), size)
    return max(matrix_det(matrix) for matrix in ms_to_test)

#print(find_max_det(4))

def find_all_perms_helper(flat_matrix):
    """
    Arg: A square matrix(list of lists)
    Returns: A list of matrices representing all permutations
    of the input matrix
    """
    if len(flat_matrix) == 1:
        return flat_matrix
    all_perms = []
    for i in range(len(flat_matrix)):
        element = flat_matrix[i]
        rest = flat_matrix[:i]+flat_matrix[i+1:]
        all_perms+= [element] + find_all_perms_helper(rest)
    
    return all_perms



def find_matrix_with_det(det, size):
    found = False
    while not found:
        m = create_rand_matrix(size)
        if matrix_det(m) == det:
            return m



