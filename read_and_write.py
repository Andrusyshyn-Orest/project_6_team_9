"""
Module consists of functions that provide reading
relations from a file and write relations to a file.
"""

def read_file(path: str) -> (set, int):
    '''
    Reads relation from file and returns it as a
    list of tuples and its length.
    '''
    rel_file = open(path, 'r', encoding='utf-8')
    relation = set()
    rel_list = rel_file.readlines()
    separator = rel_list[0][1]
    rel_file.close()
    for i in range(len(rel_list)):
        rel_list[i] = rel_list[i].split(separator)
        for j in range(len(rel_list[i])):
            if rel_list[i][j].strip() == '1':
                relation.add((i+1, j+1))
    return relation, len(rel_list)


def write_file(relation: set, n: int, path: str):
    '''
    Writes relation in file as n x n matrix
    '''
    write_rel = [[0]*n for _ in range(n)]
    rel_file = open(path, 'w', encoding='utf-8')
    rel_file.close()
    rel_file = open(path, 'a', encoding='utf-8')
    for pair in relation:
        write_rel[pair[0]-1][pair[1]-1] = 1
    for line in write_rel:
        line = list(map(str, line))
        line = ','.join(line) + '\n'
        rel_file.write(line)
    rel_file.close()
