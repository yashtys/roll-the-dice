import random
def roll_the_dice(yes):
    while yes > 0:
        no=random.randint(1,6)
        print(no)    
    print("over") 
    no=input("press “y” to continue and “n” to exit.")
    roll_the_dice(int(yes))
  