'''
Name: Justine Sanchez
Date: 11/19/25
'''

print("#1: Area of a Circle")
radius = input("What is the radius of the circle?")
int_number = int(radius)
area = ((int_number ** 2) * 3.14)
area = str(area)
print("The area of the circle is " + area)
print(str)


print ("#2: Expression Solver")
print("This is the expression solver for (a - b) + (a * b)")
a = input("Enter value of a:")
b = input("Enter value of b:")
a = int(a)
b = int(b)
result = ((a-b) + (a*b))
result = str(result)
print ("The solution is " + result)
print (str)
  

print("#3: ASCII Art")
print ("Welcome to ASCII Art!")
choice =input("Do you want to see picture 1 or 2?")
choice = int(choice)
if choice == 1: 
  print (""" Here is a sleepy kitten:  
             ______         Z
           / > _  _ >     Z
           |  =  x  )   z
          /     -- /
         /        |   
       /    \     )
      |     |  |  |
     /  _    |  |  |
    |  ( \__ \__\__)
     \__)                  """)

else: 
  print (""" Here is a fierce dinosaur:
             ____
            /.  _)
           /   /    rawr
     .^ ^ /   /
    (         )
     |_|---|_|   """)

