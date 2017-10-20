# Find words in words.txt that do not have any of the stems in stems.txt
# OBSOLETE - should read stems from WordAnalyses.xml instead

import nm
import re
import sys

stems = nm.read("stems.txt").splitlines()
words = nm.read("words.txt").splitlines()

stems.sort(key=lambda x:-len(x))

#print stems
#sys.exit(0)

pat = ".*(" + "|".join(stems) + ")"

nostem = []

for word in words:
    m = re.match(pat, word)
    if not m:
        nostem.append(word)

nm.write("nostem.txt", "\r\n".join(nostem))
