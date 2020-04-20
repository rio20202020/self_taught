import re

t = "__one__ __two__ __three__"
l = "__hi__bye__hey__"

found = re.findall("__.*?__", l)
for match in found:
    print(match)
