from utils import checkType

def sumNumbers():
  firstNumber = input("Insert the A value \n")
  
  if (checkType(firstNumber) == False):
    print("The character given isn't a number!\n\n\n\n")
    return

  secondNumber = input("Insert the B value \n")
  
  if (checkType(secondNumber) == False):
    print("The character given isn't a number!\n\n\n\n")
    return

  print("The sum is = {}".format(int(firstNumber) + int(secondNumber)))

if __name__ == '__main__':
  sumNumbers()

