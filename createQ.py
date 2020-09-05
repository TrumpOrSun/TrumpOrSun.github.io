import json
from time import time
import sys
input(f"Press <enter> to backup and start {sys.argv[0]}")
q = []
f = open('q')
fr = f.read()
f.close()
q = json.loads(fr)
backup = open('q.backup.'+str(int(time())), 'w')
backup.write(fr)
backup.close

while True:
    line   = input('      >> ')
    if line == '' or line == 'stop':
        break
    hint   = input(' hint >> ')
    answer = input('  s/t >> ')
    author = input(' by@. >> ')
    if answer.lower() == 's' or answer == 'sun':
        q.append({'q':line,'a':'sun','h':hint,'s':author})
    elif answer.lower() == 't' or answer == 'trump':
        q.append({'q':line,'a':'trump','h':hint,'s':author})

jq = json.dumps(q)

fw = open('q', 'w')
fw.write(jq)
fw.close()
