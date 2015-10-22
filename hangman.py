word_list = ['a', 'r', 'q', 'u', 'e', 't', 'i', 'p', 'o']

correct = []
guesses = 16

while word_list and guesses:
    var = raw_input("Pick a letter: ")

    # input validation
    if len(var) > 1:
        print var + ' has more than one letter'
    if not var.isalpha():
        print var + ' is not a letter'

    else: # logic
        if var in word_list:
            print 'Correct!'
            correct.append(var)
            while var in word_list:
                word_list.remove(var)
            print 'you guessed :'
            print correct
        else:
            guesses=guesses-1        
            print 'Not in word!'
            print str(guesses) + ' left!'

if guesses:
    print 'Cool! You guessed all the letters'
else:
    print 'No more guesses left!'
