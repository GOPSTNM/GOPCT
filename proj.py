import os
import random
def sub1():
  num = random.randint(2, 99)
  #lower value
  lv = 1
  #higher value
  uv = 100
  userinput = 0
  while (userinput != num):
    correct = 0
    while (correct == 0):
      userinput = int(input("Guess a number between " + str(lv) + " and " + str(uv) + ": "))
      if ((userinput >= uv) or (userinput <= lv)):
        print("Input out of range, please input again.")
      else:
        correct = 1
    if (userinput > num):
      uv = userinput
    if (userinput < num):
      lv = userinput
  print("Bingo")
def sub2():
  print("Write something...")
  input()
def bonus():
  print("Write something...")
  input()
if __name__ == "__main__":
  choice = ''
  while (choice!='E'):
    os.system('cls')
    print('**********************************************************')
    print('**************************YLMASS**************************')
    print('************************Bingo Game************************')
    print('*****************A.Easy Level*****************************')
    print('*****************B.Difficult Level ***********************')
    print('*****************C.Challenging Level *********************')
    print('*****************D.Exit **********************************')
    choice = input("Input a choice (A,B,C,D):    ")
    while ((choice<'A') or (choice>'D')):
      print("Input out of range, please input again.")
      choice = input("Input a choice (A,B,C,D):    ")
    if choice == 'A':
      sub1()
    if choice == 'B':
      sub2()
    if choice == 'C':
      bonus()
    print('*************************Bye Bye!**************************')
