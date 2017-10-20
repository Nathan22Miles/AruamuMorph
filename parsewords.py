# Read stems and suffixes file.
# Try to parse words into stems followed by one or more suffixes.
# TOO SLOW to be practical currently.
# To Do
#   - Read stems from wordlist
#   - Split off stems before tring to match suffixes

import xml.etree.ElementTree as ET
import nm
import re
import sys

words = ET.parse('wordlist.xml').getroot()

def sufs():
    text = nm.read('suffixes_revised.txt')
    text = text.replace('\n', ' ')
    text = text.replace('\r', '')

    s = text.split()
    s.sort(key=lambda x: -len(x))
    return "|".join(s)

def stems():
    text = nm.read('WordAnalyses.xml')
    parts = re.split(r"(Stem:.*?<)", text)

    s = []
    for i in range(1, len(parts), 2):
        s.append(parts[i][5:-1])

    s.sort(key=lambda x: -len(x))
    return "|".join(s)

def check(word):
    global bad
    m = re.match(rx, word)
    if not m:
        print word
        bad = bad + 1
        #if bad > 10: sys.exit(0)

rx = r"^(stems)(sufs)*$".replace('stems', stems()).replace('sufs', sufs())
bad = 0

for w in words:
    spelling = w.attrib['spelling']
    word = w.attrib['word']
    if spelling == 'Incorrect': continue

    check(word)

print len(words), bad