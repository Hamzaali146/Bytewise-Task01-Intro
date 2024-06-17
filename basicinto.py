1 a = 10
2 b = 3
3 print( ' Addition :' , a + b );
4 print( ' Subtraction : ' , a - b)
5 print( ' Multiplication: ' , a * b )
6 print( ' Division( float ) : ' , a / b )
7 print( ' Division( floor ) : ' , a // b )
8 print(' Modulus : ' , a % b )
9 print(' Exponent : ' , a ** b)
                           

msg='Welcome to Python 101: Strings'
print(msg.find('Python'))

msg='Welcome to Python 101: Strings'
print(msg.replace('Python','C'))

name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
#sales.extend(sales_w1)
#sales.extend(sales_w2)
sales = sales_w1 + sales_w2
sales.sort()
worst_day_prof = sales[0] * 1.5
best_day_prof = sales[-1] * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

msg = ' welcome to t \' s Python 101 : Strings '
print ( msg )
print ( msg.upper ( ) )
print ( msg.lower ( ) )
print ( msg.capitalize ( ) )
print ( msg.title ( ) )

