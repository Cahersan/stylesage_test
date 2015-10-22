import sys

number = 1335

str_number = str(number)

output = ''
count = len(str_number)-1

for s in str_number:
    output = output + s 
    if count % 3 == 0:
       output = output +  ','
    
    count=count-1

print output[0:len(output)-1]    