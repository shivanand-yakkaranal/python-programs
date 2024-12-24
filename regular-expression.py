import re
'''
txt="The rain in Bangalore"
x=re.search("^The .*Bangalore$",txt)

if x:
    print("Yes we have match")
else:
    print("No match found")
'''
#---------
"""
txt="python";
x=re.search("py.*on",txt)
if x:
    print("Found the match")
else:
    print("Not found")
"""
txt="The rain in Spain"
#x=re.findall("i",txt)
#x=re.search("\s",txt)
#print("The first white-space located at:",x.start())
#x=re.split("\s",txt)
#x=re.split("\s",txt,1)
#x=re.sub("\s","#",txt)
#print(x)
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())