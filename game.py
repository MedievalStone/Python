import sys
import random

if len(sys.argv)==3 :
        try:
            start=int(sys.argv[1]);
            end=int(sys.argv[2]);
            randomNumber=random.randint(int(start),int(end));

        except ValueError:
            print('Input is invalid friend and so i am taking default values');
            start=1
            end=100

else:
    start=1;
    end=100;
    randomNumber=random.randint(start,end);

# print(type(randomNumber))

while(True):
    temp=int(input(f'enter the number b/w {start} and {end}\t'));
    print(type(temp))
    if(temp==randomNumber):
        print("You are genius!!");
        break;
    else:
        print('You are Unsucessfull');
