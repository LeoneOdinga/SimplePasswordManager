import random

# global variables - CONSTANTS
alphabetsLowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                      'o','p','q','r','s','t','u','v','w','x','y','z']

alphabetsUpperCase =['A','B','C','D', 'E','F','G','H','I','J','K','L','M','N',
                     'O','P','Q','R','S','T','U','V','W','X','Y','Z']

allLetters = alphabetsUpperCase+alphabetsLowerCase

numbers =['0','1','2','3','4','5','6','7','8','9']

specialCharacters = ['!','#','$','%','&','|','>','*','^','@','+','~','?']

'''Function Accepts number of letters, symbols and numbers to include in random password returned'''

def randomPasswords(letterCount,symbolCount,numberCount):
    passwordContainer = []

    for char in range(letterCount):
        passwordContainer+=random.choice(allLetters)
    for char in range(symbolCount):
        passwordContainer+=random.choice(specialCharacters)
    for char in range(numberCount):
        passwordContainer+=random.choice(numbers)
    random.shuffle(passwordContainer)

    returnedPassword =""

    for passwordChar in passwordContainer:
        returnedPassword+=passwordChar
    return returnedPassword
#
# '''==================================User Area==================================================='''
#
# howManyLetters =int(input("\nHow Many Letters Do You Need For Your Password?"))
#
# howManyNumberCharacters = int(input("\nHow Many Number Characters Do You Need For Your Password?"))
#
# howManySpecialCharacters = int (input("\nHow Many Special Characters Do You Wish To Include?"))

# print(f"\nYour Generated Password is: {randomPasswords(5,4,2)}")