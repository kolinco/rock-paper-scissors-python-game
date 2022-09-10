import random
#humans part
print("Welcome to rock papaer sissors game.")
ch1=int(input('what do you choose ? type "0"for Rock , "1" for Paper or "2" for Sissors'))
if ch1==0:
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
     ---.__(___)
    ''')
elif ch1==1:
    print('''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    ''')
else:
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')

#computer part
ch2=random.randint(0, 2)
if ch2==0:
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
     ---.__(___)
    ''')
elif ch2==1:
    print('''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    ''')
else:
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')
##
if (ch1==ch2):
    print("its a draw")
elif(ch1==1 and ch2==0):
    print("you win")
elif(ch1==2 and ch2==1):
    print("you win")
else:
    print("you loose")