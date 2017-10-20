# -*- coding: latin-1 -*-
# Extract renderings for names from html output produced by Biblical Terms tool

from bs4 import BeautifulSoup
import nm

html = nm.read('names.htm', encoding="utf-16")
soup = BeautifulSoup(html, 'html.parser')

names = set()
for rends in [x.string for x in soup.find_all(class_="Renderings")]:
    if not rends: continue
    for rend in rends.split("|"):
        if rend.find("*") >= 0: continue
        names.add(rend.lower())

names2 = set(names)
for name in names2:
    if name + u"n" in names: names.remove(name + u"n")
    if name + u"\xe7n" in names: names.remove(name + u"\xe7n")

names = list(names)
names.sort()

nm.write("names.txt", "\r\n".join(names))