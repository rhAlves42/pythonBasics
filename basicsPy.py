
def isInteger(number):
  try:
    float(number)
  except ValueError:
    return False
  else:
    return float(number).is_integer()

def sumNumbers():
  firstNumber = input("Insert the A value \n")
  
  if (isInteger(firstNumber) == False):
    print("The character given isn't a number!\n\n\n\n")
    return

  secondNumber = input("Insert the B value \n")
  
  if (isInteger(secondNumber) == False):
    print("The character given isn't a number!\n\n\n\n")
    return

  print("the sum is = {}".format(int(firstNumber) + int(secondNumber)))

if __name__ == '__main__':
   sumNumbers()

