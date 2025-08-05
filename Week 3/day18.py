# Day 18 - Regular Expressions
# import re
import re

#2
txt = ("The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 "
       "in the negative direction, 0 at origin, 4 and 8 in the positive direction. "
       "Extract these numbers from this whole text and find the distance between the two furthest particles")
matches = re.findall(r"[+-]?\d+", txt)
print(matches)
postion1 = re.search(r"[+-]?\d+", txt)
span = postion1.span()
print(span)
match = re.search(r"-12", txt)
print(match)
match2 = re.search(r"8", txt)
print(match2)