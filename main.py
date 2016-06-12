import timeit
import random
import os.path
from time import sleep
import sys

motivate = ["You got this!", "Hang in there!"]
better_luck = ["Better luck next time!", "Don't lose direction!"]

if not os.path.isfile("total"):
    f = open("total", "w")
    f.write("0\n")
    f.close()

f = open("total", "r")
try:
    total = int(f.readlines()[0])
except:
    print("Error reading the file")
    sys.exit(1)
f.close()


args = sys.argv
if len(args) == 2 and args[1] == "reset":
    f = open("total", "w")
    f.write("0\n")
    f.close()
    print("You are now back at a total focus score of 0.")
    sys.exit(0)

for i in range(random.randint(1, 6)):
    for j in range(5):
        print("Loading"+"."*j)
        sleep(.15)
        sys.stdout.write("\033[F\033[K")

while True:
    print(">>> Please enter your command:")
    command = input().split()

    if command[0] in ["man", "help", "about"]:
        print(">>> The possible commands are:\n+ man\n+ help\n+ about\n+ reset\n+ min\n+ exit\nreset can also be used as a command argument")
        continue
    if command[0] == "exit":
        for i in range(random.randint(1, 4)):
            for j in range(5):
                print("Exiting"+"."*j)
                sleep(.15)
                sys.stdout.write("\033[F\033[K")
        sys.exit(0)

    if command[0] == "reset":
        f = open("total", "w")
        f.write("0\n")
        f.close()
        print("You are now back at a total focus score of 0.")
        continue

    if command[0] == "min":
        if (len(command) == 1):
            print(">>> Please input the number of minutes:")
            minutes = int(input())
        else:
            minutes = int(command[1])

        print("You already have a total focus score of %d." % total)

        seconds = minutes * 60

        try:
            current = 0
            while current < seconds:
                sleep(.1)
                current += 60
                num = int(current//60/minutes*20) # so it can't round() up to full bar when it's not
                bar = "Progress: |"+"="*num+"-"*(20-num)+"|"

                if (current == 60):
                    print("%s%25s%50s" % ("1 minute elapsed.", motivate[random.randrange(0, len(motivate))], bar), end="\r")
                else:
                    print("%s%25s%50s" % (str(current//60)+" minutes elapsed.", motivate[random.randrange(0, len(motivate))], bar), end="\r")
        except KeyboardInterrupt:
            print("\nYou have decided to quit. Would you like to count these minutes toward your total? (y/n)")
            yn = input()
            if yn.lower() == "y":
                total += current//60
                print("Congratulations! You have now focused for %d minutes." % total)
                f = open("total", "w")
                f.write(str(total)+"\n")
                f.close()
            elif yn.lower() == "n":
                print(better_luck[random.randrange(0, len(better_luck))])
            sys.exit(0)

        total += minutes
        print("Congratulations! Your new focus score is %d." % total)
        f = open("total", "w")
        f.write(str(total)+"\n")
        f.close()
