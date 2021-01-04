"""
Module consists of the functions used
to find the closures of the relations.
"""

import doctest
from read_and_write import write_file


def transform_relation_into_matrix(relation: set, size: int) -> list:
    """
    Returns matrix (size x size) from given relation.

    >>> transform_relation_into_matrix({(1, 4), (2, 1), (2, 3),\
                                        (3, 1), (3, 4), (4, 3)}, 4)
    [[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]
    """

    matrix = []
    for _ in range(size):
        matrix.append([0]*size)

    for element in relation:
        row = element[0] - 1
        col = element[1] - 1
        matrix[row][col] = 1
    return matrix


def transform_matrix_into_relation(matrix: list) -> set:
    """
    Returns relation from given matrix.

    >>> sorted(transform_matrix_into_relation([[0, 0, 0, 1],\
                                        [1, 0, 1, 0],\
                                        [1, 0, 0, 1],\
                                        [0, 0, 1, 0]]))
    [(1, 4), (2, 1), (2, 3), (3, 1), (3, 4), (4, 3)]
    """

    relation = set()
    size = len(matrix)
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 1:
                relation.add( (row + 1, col + 1) )
    return relation


def find_transitive_closure(relation: set, size: int) -> set:
    """
    Returns transitive closure of given relation on set with
    number of elements == 4. Transitive closure is a set of tuples.

    >>> sorted(find_transitive_closure({(1, 4), (2, 1), (2, 3),\
                                 (3, 1), (3, 4), (4, 3)}, 4))
    [(1, 1), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 3),\
 (3, 4), (4, 1), (4, 3), (4, 4)]
    """

    closure = transform_relation_into_matrix(relation, size)
    for num in range(size):
        for row in range(size):
            if (row != num) and (closure[row][num] == 1):
                for col in range(size):
                    closure[row][col] = closure[row][col]\
                                      | closure[num][col]
    return transform_matrix_into_relation(closure)


def reflexive_closure(relation: set, n: int, path: str = '') -> set:
    '''
    Finds reflexive closure and return relation.
    It can be written in file if path is given.

    >>> reflexive_closure({(1,2), (2,1), (1,1)}, 3)
    {(1, 2), (2, 1), (1, 1), (3, 3), (2, 2)}
    >>> reflexive_closure(set(), 2)
    {(1, 1), (2, 2)}
    '''
    for i in range(1, n+1):
        if (i, i) not in relation:
            relation.add((i, i))
    if path:
        write_file(relation, n, path)
    return relation


def symmetric_closure(relation: set, n: int, path: str = '') -> set:
    '''
    Finds symmetric closure and return relation.
    It can be written in file if path is given.

    >>> symmetric_closure({(1,2), (2,2), (1,1)}, 3)
    {(1, 1), (1, 2), (2, 1), (2, 2)}
    >>> symmetric_closure({(1,2), (2,1), (1,1)}, 2)
    {(1, 1), (1, 2), (2, 1)}
    '''
    closure = set()
    for x, y in relation:
        if (y, x) not in relation:
            closure.add((y, x))
    relation |= closure
    if path:
        write_file(relation, n, path)
    return relation


if __name__ == "__main__":
    print(doctest.testmod())
