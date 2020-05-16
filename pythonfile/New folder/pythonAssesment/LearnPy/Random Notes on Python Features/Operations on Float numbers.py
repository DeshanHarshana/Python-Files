import math
print(0.1 + 0.2 == 0.3)
t=round(0.1+0.2,2)==round(0.3,2)#true #round 2 digit
t=round(0.1,2)+round(0.2,2)==round(0.3,2) #false
x=format(32.4467, '.4g')#this return 4 digit in left side with rounding
x=format(23.4567434533,'0.6g')
x=format(23.44564,'0.3f')#this consider decimal points
x=format(0.1,'0.1f')+format(0.2,'0.1f')==format(0.3,'0.1f')#false
x=(format(0.1+0.2,'0.1f')==format(0.3,'0.1f'))#true
print(x)

'''
python use Double (IEEE754 Double precision 64-bit)

it has one sign bit
it has 11 bit for exponent
it has 53 to mantissa(Significand)

it add floting point number by converting this format

take 0.1+0.2

0.1 double precision value=
>>>>> 0(sign) 01111111011(exponent) 1001100110011001100110011001100110011001100110011010(mantissa)

0.2 double precision value=
>>>>> 0(sign) 01111111100(exponent) 1001100110011001100110011001100110011001100110011010(mantissa)

addition of these numbers is we can get =
>>>>> 0(sign) 01111111101(exponent) 0011001100110011001100110011001100110011001100110100(mantissa)

but after we convert this number to decimal this is not a 0.3
this number is 3.00000000000000044408920985006

then we can't tell 0.1+0.2==0.3 is true it is false

we can use this case
round(0.1+0.2,2)==round(0.3,2)
x=math.isclose(0.1+0.2,0.3)
print(x)


'''

