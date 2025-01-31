def replace_string(text,ch):
	result=''
	for i in text:
		if i==' ':
			i=ch
		result+=i
	return result

text="il vey u"
ch="o"
#text="D t C mpBl ckFrid yS le"
#ch="a"

print(replace_string(text,ch))