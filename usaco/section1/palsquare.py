"""
ID: futzipe1
LANG: PYTHON3
TASK: palsquare
"""
with open("palsquare.out", 'w') as out, open("palsquare.in", 'r', encoding='utf-8') as fin:
    lines = fin.read().splitlines()  # lines is list type
    out.write(str(lines))
