number = ''

while not number.isdigit():
	number = raw_input("Please insert a long number: ")

output = ''
count = len(number)-1

for s in number:
    output +=  s 
    if count % 3 == 0:
       output += ','
    
    count -= 1

print output[0:len(output)-1]    