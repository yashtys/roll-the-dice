import random
def roll_the_dice(yes):
    while yes > 0:
        no=random.randint(1,6)
        print(no)    
    print("over") 
    no=input("press āyā to continue and ānā to exit.")
    roll_the_dice(int(yes))
  