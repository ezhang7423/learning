"""
ID: futzipe1
LANG: PYTHON3
TASK: transform
"""
def prettify(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] = '@':
                matrix[x][y] = 'X'
            else:
                matrix[x][y] = 'O'
    return matrix

def mp(matrix):
    for x in range(len(matrix)):
        print(matrix[x])

with open("transform.out", 'w') as out, open("transform.in", 'r', encoding='utf-8') as fin:
        lines = fin.readlines()
        for i, x in enumerate(lines):
            lines[i] = (x.strip('\n'))
        
        lines = lines.pop(0)
        lines = prettify(matrix)            
        # out.write(str(lines))