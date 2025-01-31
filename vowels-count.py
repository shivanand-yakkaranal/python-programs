vowels=['a','e','i','o','u']
count=0
word="programming"

for i in word:
	if i in vowels:
		count+=1

print(f"Vowels count in {word}: ",count)
