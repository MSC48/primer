num1=int(input('escriba un numero'))
num2=int(input('escriba un numero'))
num3=int(input('escriba un numero'))

if num1>num2>num3:
    print('primero',num1)
elif num1<num2<num3:
    print(num3)
elif num1<num2>num3:
    print (num2)
elif num1==num2==num3:
    print('son iguales')        



