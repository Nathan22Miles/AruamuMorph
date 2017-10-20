# Read names.txt for list of approved Aruamu renderings for names
# Find matching words in wordslit.xml and update their morphology producing nameswordlist.xml

import xml.etree.ElementTree as ET
from xml.dom import minidom
import nm
import re
import sys

words = ET.parse('wordlist.xml').getroot()
print len(words), "words read"

names = set(nm.read('names.txt').splitlines())
print len(names), "names read"

removed = 0

for w in reversed(words):
    spelling = w.attrib['spelling']
    word = w.attrib['word']

    if word in names: 
        w.attrib["morphology"] = word
        w.attrib["morphologyApproved"] = "True"
        continue

    if word[:-1] in names and word[-1] == "n": 
        w.attrib["morphology"] = word[:-1] + " +n"
        w.attrib["morphologyApproved"] = "True"
        continue

    if word[:-2] in names and word[-2:] == u"\xe7n": 
        w.attrib["morphology"] = word[:-2] + u" +\xe7n"
        w.attrib["morphologyApproved"] = "True"
        continue

    removed = removed + 1
    words.remove(w)

print removed, "removed"
print len(words), "words remain"

#sys.exit(0) 

rough_string = ET.tostring(words, 'utf-8')
reparsed = minidom.parseString(rough_string)
nm.write("nameswordlist.xml", reparsed.toprettyxml(indent="  "))