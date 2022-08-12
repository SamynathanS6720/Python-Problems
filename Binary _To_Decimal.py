inp = 100 #get binary number as int format
result = 0
i = 0
while inp > 0 :
#To Compute the input value in to decimal number
n = inp % 10 ;
result = result + ( n * 2** i )
inp = inp // 10
i = i + 1
print( result )
