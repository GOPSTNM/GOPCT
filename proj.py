import os
import random
def sub1(): 
  print("Write something...") 
  input()
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
    choice = input("Input a choice (A,B,C,D):    ") 
    while ((choice<'A') or (choice>'D')): 
      print("Input out of range, please input again.")
      choice = input("Input a choice (A,B,C,D):    ") 
    if choice == 'A': 
      sub1() 
    if choice == 'B': 
      sub2() 
    if choice == 'C': 
      bonus() 
    print('*************************Bye Bye!****************************')
