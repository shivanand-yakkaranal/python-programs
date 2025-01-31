#print(ord("A"),ord("a"))
s = "l vey u"

#replacements = str.maketrans({"h": "H", "e": "E", "o": "O"})
replacements = str.maketrans({" ": "o"})
res = s.translate(replacements)
print(res)