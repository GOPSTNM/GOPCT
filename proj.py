import os
import random
import time
def sub1():
  #generate random no
  num = random.randint(2, 99)
  #lower value
  lv = 1
  #higher value
  uv = 100
  userinput = 0
  while (userinput != num):
    #correct means if ans is correct (in range)
    #1=correct
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
  num = random.randint(2, 99)
  userinput = 0
  while (userinput != num):
    numlist = [num]
    print("**********************************************************")
    #make 5 numbers insert in list in random position
    for i in range(5):
      numlist.insert(random.randint(0, len(numlist)), random.randint(2, 99))
    print (numlist)
    while not(userinput in numlist):
      userinput = int(input("Guess a number from the list by typing the number: "))
      if not(userinput in numlist):
        print("Input out of range, please input again.")
    if (userinput != num):
      print("The number is incorrect. Try again.")
    else:
      print("Bingo")
def bonus():
  num = random.randint(2, 99)
  #lower value
  lv = 1
  #higher value
  uv = 100
  userinput = 0
  #record start time
  start_time = time.time()
  print(str(num))
  #number of guess
  nog = 0
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
    print("hint")
    nog += 1
  print("Bingo")
  print("You used " + str(int(time.time()-start_time)) + " secounds to guess the number.")
  print("You guessed " + str(nog) + " times.")
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
    print('*************************Bye Bye!*************************')
