"""
Module consists of functions that study transitivity of relations.
"""

import doctest


def check_if_transitive(relation: set) -> bool:
    """
    Checks if given relation is transitive.

    >>> check_if_transitive({(1,2)})
    True
    >>> check_if_transitive({})
    True
    >>> check_if_transitive({(1,2), (1,3)})
    True
    >>> check_if_transitive({(1,2), (2,3), (1,3)})
    True
    """

    for x, y in relation:
        y_pair = set(b for a, b in relation if a == y)
        for c in y_pair:
            if (x, c) not in relation:
                return False
    return True


def find_number_of_transitives(n: int) -> int:
    """
    Returns number of all transitive relations on a set with
    n elements.

    >>> find_number_of_transitives(0)
    1
    >>> find_number_of_transitives(1)
    2
    >>> find_number_of_transitives(2)
    13
    >>> find_number_of_transitives(3)
    171
    >>> find_number_of_transitives(4)
    3994
    """

    relation = [(a,b) for a in range(1, n + 1) for b in range(1, n + 1)]

    size = n*n
    count = 0
    for num in range(pow(2, size)):
        num = bin(num)[2:]          #removing '0b'
        num = num.zfill(size)

        check_relation = set()
        for ind in range(size):
            if num[ind] == '1':
                check_relation.add(relation[ind])
        if check_if_transitive(check_relation):
            count+=1
    return count


if __name__ == "__main__":
    print(doctest.testmod())
