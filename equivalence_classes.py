"""
Module consists of a function that works on
determination of equivalence classes of equivalence relations.
"""

import doctest
from transitive import check_if_transitive


def find_classes(relation: str, n: int) -> list:
    '''
    Returns equivalence classes of given
    relation

    >>> find_classes({(1,2), (2,1), (1,1), (2,2)}, 2)
    [[1, 2]]
    >>> find_classes({(1,2), (2,1), (1,1), (2,2)}, 3)
    'Not equivalence relation'
    '''
    if not check_if_transitive(relation):
        return "Not equivalence relation"
    for i in range(1, n+1):
        if (i, i) not in relation:
            return "Not equivalence relation"
    for x, y in relation:
        if (y, x) not in relation:
            return "Not equivalence relation"
       
    classes = []
    relation = list(relation)
    while len(relation) != 0:
        relation_copy = set(relation)
        x, y = relation[0]
        x_pairs = set()
        for a, b in relation_copy:
            if a == x:
                x_pairs.add(b)
                relation.remove((a, b))
        if x_pairs not in classes:
            classes.append(x_pairs)
    classes = list(map(list, classes))
    return classes


if __name__ == "__main__":
    print(doctest.testmod())
