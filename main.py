a = int(input("Pick a number "))#varibles
b = int(input("Pick a number "))
c = int(input("Pick a number "))

if a > b and a > c and b > c:#just different ifs checking different conditions
  print("The smallest number is " + str(c))
  print("The second smallest number is " + str(b))
  print("The biggest number is " + str(a))

elif a > b and a > c and c > b:
  print("The smallest number is " + str(b))
  print("The second smallest number is " + str(c))
  print("The biggest number is " + str(a))

elif b > a and b > c and a > c:
  print("The smallest number is " + str(c))
  print("The second smallest number is " + str(a))
  print("The biggest number is " + str(b))

elif b > a and b > c and c > a:
  print("The smallest number is " + str(c))
  print("The second smallest number is " + str(a))
  print("The biggest number is " + str(b))

elif c > a and c > b and a > b:
  print("The smallest number is " + str(b))
  print("The second smallest number is " + str(a))
  print("The biggest number is " + str(c))

elif c > a and c > b and b > a:
  print("The smallest number is " + str(a))
  print("The second smallest number is " + str(b))
  print("The biggest number is " + str(c))

elif b == a or b == c or a == c: #preventing from trying to break
  print("You can't do that! Try again")
  
