# 10 operation calculator
import math
menue=int(input("Select the operation:\n1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Modulus\n6.Floor Division\n7.Exponent of a number\n8.sinus\n9.cosine\n10.tangent\nEnter your choice: "))
if menue not in range(1,11):
 print("You You intered wrong option.\nPlease input an integer number between 1 to 10 next time.")
 exit()
if menue not in range(1,8):
    x=float(input("Enter one number: "))
else: 
   x1=float(input("Enter the first number: "))
   x2=float(input("Enter the second number: "))
if menue==1:
  print("The sum of 2 numbers= " ,(x1+x2))
elif menue==2:
 print("The Subtraction of 2 numbers= ",(x1-x2))
elif menue==3:
 print("The Multiplication of 2 numbers=  ",(x1*x2))
elif menue==4:
 print("The Division of 2 numbers=",(x1/x2))
elif menue==5:
 print("The Modulus of 2 numbers= ",(x1%x2))
elif menue==6:
 print("The Floor Division of 2 numbers= ",(x1//x2))  
elif menue==7:
 print("The Floor Exponent of 2 numbers=  ",(x1**x2))  
elif menue==8:
 print("The Sinus of",x,"is equal to:  ",math.sin(x))
elif menue==9:
 print("The Cosine of",x,"is equal to:  ",math.cos(x))
else:
 print("The Tangent of",x,"is equal to:  ",math.tan(x))


  
   
