def checkPoilindromeByJoin():
 a="malayalam"
 b=''.join(reversed(a))

 if a==b:
  print("Polindrome")
 else:
  print("Not polindrome")

def checkPoilindromeNegtveIndexing():
 a="malayalam"
 c=a[::-1]
 if a==c:
  print("Polindrome")
 else:
  print("Not polindrome")

checkPoilindromeByJoin()
checkPoilindromeNegtveIndexing()