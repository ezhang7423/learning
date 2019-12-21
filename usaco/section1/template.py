"""
ID: your_id_here
LANG: PYTHON3
TASK: test
"""
with open("test.out", 'w') as out, open("test.in", 'r', encoding='utf-8') as fin:
        lines = fin.readlines() #lines is list type
        out.write(str(lines))