import re

if re.search("ape", "the ape at the apex"):
    print("there is an ape")
    
allApes = re.findall("ape", "the ape at the apex")
for i in allApes:
    print(i)
    
the_str = "The ape at the apex"
for i in re.finditter("ape", the_str):
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])