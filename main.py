import random
run = input("Ready to toss a coin ? Input yes or no").lower()
if(run=="yes"):
    zero_one = random.randint(0,1)
    if(zero_one==1):
        print("Heads")
    elif(zero_one==0):
        print("Tails")
else:
    exit()
