from utils import checkType

def findCircleAreaa():
  n = 3.14159
  radio = input("Insert the radio value \n")

  if (checkType(radio, float) == False):
    print("The character given isn't a number!\n\n\n\n")
    return

  area = n * pow(float(radio), 2)

  print("A={}".format(area))

if __name__ == '__main__':
  findCircleAreaa()

