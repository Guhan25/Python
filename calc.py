num1 = input("enter n1 ")
num2 = input("enter n2 ")
if(num1.isalpha() or num2.isalpha()):
   print("enter the valid number ")
else:
    choose = input("choose the option\nAdd\nSub\nMul\nDiv\n")
    floatnum1 = float(num1)
    floatnum2 = float(num2)
    if choose == "1":
     output=floatnum1+floatnum2
     print("Your Answer: "+str(output))
    elif choose == "2":
     output=floatnum1-floatnum2
     print("Your Answer: "+str(output))
    elif choose == "3":
     output=floatnum1*floatnum2
     print("Your Answer: "+str(output))
    elif choose == "4":
      if num2=="0":
       print ("the num2 is zero  ")
      else:
        output=floatnum1/floatnum2
        print("Your Answer: "+str(output))
    else:
      print("invalid code ")
    
    
