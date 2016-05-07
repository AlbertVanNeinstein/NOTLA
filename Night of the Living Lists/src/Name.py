""" Fixed up some errors in the code, and added the or statement again, but it works. If there are errors, play with indentation"""
""" Just checked it out, seems good, ben!"""

print'Welcome to Working Title! We hope you have a good stay'
print"(PLEASE capitalise each choice, the game won't work if you don't! (other than your name)"
def name():
    print 'What is your name?'
    n='no'
    while n=='no' or n=='No':
        x=raw_input('>>')
        name=x
        if x=='debug' or x=='Debug':
            print'You Have Won! We will now end the game'

        print 'So, your name is %r?' % name
        n = raw_input('Are you sure? >')
        if n =='No' or n=='no':
                print 'Okay, Whats your name?'
        if n == 'Yes' or n=='yes':
            print 'Lets Go!'
            return name
        else:
            print"That's not an option"

name()