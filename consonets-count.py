vowels=['a','e','i','o','u']
count=0
word="programming"

for i in word:
	if i not in vowels:
		count+=1

print(f"Consonents count in {word}: ",count)
