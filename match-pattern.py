def switchDemo(month):
 match month:
  case 'jan':
   print("I am in January")
  case 'feb':
   print("I am in February")
  case 'dec':
   print("I am in December")
  case _:
   print("I am default")

switchDemo('jan')