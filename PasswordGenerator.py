def genPassword():
    import string
    import random
    num=1
    
    bContinue=True
    length=int(input('Enter the length of the password. \n'
                     'Length cannot be less than 1. \n'
                     'Enter 0 to cancel: '))
    forPass=int(input('Enter how many passwords to generate:'))
    while forPass >0:
        key=''
        if length==0:
            print("Thank you for using the Password Calculator.")
        elif length<0:
            print("Error.  Wrong Value Selected")
            genPassword()            
        elif length!=0:
            for num in range(length):
                key+=random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation)
        print(key)
        forPass -=1
    genPassword()
genPassword()
