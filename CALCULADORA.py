print('      C A L C U L A D O R A')
print('\nCs Calculadora simple           Cc Calculadora cientifica')
print('eliga una opcion')
cal=input()
if cal=='cs':
   print('eliga una operacion')
   print('\nsumar','\nrestar','\nmultiplicar','\nDividir')
   opera=input().lower()
   num1=float(input())
   num2=float(input())
    
   if opera=='s' :
    print(num1+num2)
   elif opera=='r' :
    print(num1-num2)
   elif opera=='m'or opera=='p' :
    print(num1*num2)    
   elif opera=='d' :
    print(num1/num2)
else:
  if cal=='cc':
   print('eliga una operacion')
   print('\nsumar','\nrestar','\nmultiplicar','\nDividir')
   opera=input().lower()
   num1=input()
   num2=input()

   num1==float(num1)
   print(num1)

