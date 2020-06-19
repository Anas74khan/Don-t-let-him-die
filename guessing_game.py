import random

def effects(x):
        if(x == 0):
                print("    O_| ")
                print("   /|\  ")
                print("   / \  ")
                print("\n")
        if(x == 1):
                print("   \O_| ")
                print("    |\  ")
                print("   / \  ")
                print("\n")
        if(x == 2):
                print("   \O/_|")
                print("    |   ")
                print("   / \  ")
                print("\n")
        if(x == 3):
                print("   \O/_")
                print("    |  ")
                print("   / \ ")
                print("\n")
        if(x == 4):
                print("   \O/ ")
                print("    |  ")
                print("   / \ ")
                print("\n")
        if(x == 5):
                print("   \O/ ")
                print("    |  ")
                print("   /   ")
                print("\n")
        if(x == 6):
                print("   \O/ ")
                print("    |  ")
                print("\n")
        if(x == 7):
                print("   \O/ ")
                print("\n")
        if(x == 8):
                print("   \O   ")
                print("\n")
        if(x == 9):
                print("    O  ")
                print("\n")



def result(m):
        lifes = 10
        print("You have 10 lifes to guess the word")
        s = random.choice(m.split(' '))
        b = []
        letter = []
        for i in s:
            b.append('_')
            letter.append(i)
        l="lost"
        while(lifes!=0):
            print(*b,' ')
            print("Lifes: ",lifes)
            j = input("Enter guess: ")
            red = True
            for i in range(len(letter)):
                if((j.upper()==letter[i]) or (j.lower()==letter[i])):
                    b[i] = letter[i]
                    red = False
            if(red==True):
                lifes-=1
            if(b==letter):
                    l="win"
                    break
            print("_"*70)
            effects(lifes)
        print("\nletter was: ", s)
        return l


print("Create a text file having diffent words separted by spaces")
print("_"*70)
first = 'Y'
second = 'N'
while(first=='Y' or first=='y'):
    fi=input("Enter file name with extension: ")
    print("_"*70)
    try:
        f=open(fi,"r")
        g = f.read()
        f.close()
        first='n'
        second = 'y'
    except FileNotFoundError:
        print("please check the file name and start again")
        first = input("Enter Y if you want to restart or enter any other key to exit: ")
        print("_"*70)
while(second=='y' or second=='y'):
    z=result(g)
    if z=='win':
        print('congrats you won!!!')
    else:
        print("You let him die!! better luck next time")
    second = input("Enter Y if you want to play again or enter any other key to exit: ")
    print("_"*70)
