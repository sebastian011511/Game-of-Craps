"""
Created by Sebastian Vasco
This program is a simulation of the game craps.

PLEASE NOTE TO MODIFY THE DIRECTORY TO MATCH YOUR HOME DIRECTORY FOR READING AND WRITING FILES


"""

import random
import sys
import os

rollAgain=False


def checkvalues(value1, value2):
    totalvalue = value1 + value2

    if totalvalue==7 or totalvalue==11:
        wonGame=True
    else:
        wonGame=False

    return wonGame


def checkrollagain(reRoll,tfunds,betAmount):     # this function will re roll dice again until user wins or loose
    tempValue=0
    tempRandNum=0
    tempRandNum2=0
    tempPoints=0

    while True:
        while True:

            print("""\n\n\tRoll again!  If you roll a total of """,reRoll,"""before rolling a 7, 
            then you win the bet. If you roll a 7 before rolling a""",reRoll,"""you loose the bet.""",end='\n')
            roll1 = str(input('\t\tR/r to roll: '))
            if roll1 == 'r' or roll1 == 'R':
                tempRandNum = random.randint(1, 6)
                print('\tFirst Roll: ', tempRandNum, end=" ")
                break
            else:
                print('\n\tInvalid input.', end=' ')
        while True:

            print("""\n\tRoll again. """,end=" ")
            roll2 = str(input('R/r to roll again: '))
            if roll2 == 'r' or roll2 == 'R':
                tempRandNum2 = random.randint(1, 6)
                print('\tSecond Roll: ', tempRandNum2, end=" ")
                break
            else:
                print('\n\tInvalid input.', end=' ')

        tempValue=tempRandNum+tempRandNum2

        if tempValue==7 or tempValue==reRoll: # if total value of rolls is not e
            break

    if tempValue==reRoll:     # wins bet if it matches point number
        os.system('cls')

        print('\n\tYou have won your bet! You got a ',tempValue,end='\n')
        tfunds=tfunds+betAmount+betAmount

    elif tempValue==7:        # loose bet and money
        os.system('cls')
        print('\n\tYou have lost your bet, sorry. You got a ',tempValue,".",end='\n')
        tfunds=tfunds-betAmount

    return tfunds


def main():
    # Menu Options
    play = 1
    funds = 2
    reset = 3
    save = 4
    quitGame = 5

    # game variables
    roll1 = ''  # hold R to roll
    totalFunds = 1000  # holds total funds
    startingBank=1000
    betAmount = 100
    wonGame = False  # keeps track is the player won or lost the game
    userName=''

    infile=open(r'c:\Users\svasco\Documents\OOPL\Python\GameOfCraps\SavedGames.txt','r')

    try:

        os.system('cls')
        print('\n\tWelcome to the Game of Craps:\n')
        print('\tPlease enter your name.')
        playersName=str(input('\t\tName: '))

        for line in infile:
            userName, tempPoints=line.split(';') # reads file and add name and score to two dif variables

            if playersName == userName:
                print("\n\tGood to see you back ",userName,'! Here is your last score: ',tempPoints)
                totalFunds=int(tempPoints)
                break

        # If name was not found in file, then assign name to username which will be used to write to file
        userName=playersName

    finally:
        infile.close()

    while True:
        print('\n\t********Main Menu********')
        print('\t1.\tPlay the Game\n\t2.\tDisplay Available Funds\n\t3.\tReset Winnings to Zero')
        print('\t4.\tSave Name and Score\n\t5.\tQuit\n\n')
        # menuOption = int(input("Choice:\t"))

        while True:
            try:
                menuOption = int(input("\tChoice:\t"))

            except ValueError:
                print('\n\tInvalid input. Please try again.',end='\n')
                continue

            if menuOption<1 or 5<menuOption:
                print('\n\tInvalid input. Please try again.',end='\n')
            else:
                break

        if menuOption == play:

            os.system('cls')
            while True:  # 1st input
                roll1 = str(input('\tPress R/r to roll the first die:'))
                if roll1 == 'r' or roll1 == 'R':
                    randNum = random.randint(1, 6)
                    print('\tFirst roll: ', randNum, end=" ")
                    break
                else:
                    print('\tInvalid input.', end=' ')

            while True:  # 2nd input
                roll1 = str(input('\n\tPress R/r to roll the second die:'))
                if roll1 == 'r' or roll1 == 'R':
                    randNum2 = random.randint(1, 6)
                    print('\tSecond roll: ', randNum2, end=" ")
                    break
                else:
                    print('\tInvalid input.', end=' ')

            if checkvalues(randNum, randNum2):       # statement calls method that checks if the user won game

                # If won, user takes the money betted ($100) + wins another $100 and is added to total bank
                totalFunds = totalFunds+betAmount+betAmount

                print("\n\n\tCongratulations! Your roll: ", randNum+randNum2,".  Available funds: $", totalFunds)

            else:                                    # did not win so needs to check if lost of needs to roll again
                if randNum+randNum2==2 or randNum+randNum2==3 or randNum+randNum2 == 12:   # if rolls total of 2,3 or 12, user looses bet and money
                    totalFunds = totalFunds-betAmount

                    print("\n\n\tYou lost the game. You scored ",randNum+randNum," Available funds: $",totalFunds)
                else:

                    totalFunds=checkrollagain(randNum+randNum2,totalFunds,betAmount)
                    print('\n\tAvailable Funds: $',totalFunds,end='\n')

            if totalFunds<=0:
                        print('\n\t\tGAME OVER--YOUR ARE OUT OF FUNDS!')
                        sys.exit()

        elif menuOption==funds:

            print('\n\tAvailable Funds: $',totalFunds,end='\n\n')

        elif menuOption==reset:

            print('\n\t\nAre you Sure?:')
            while True:
                tempValue=str(input('(Y/N):')).lower()
                if tempValue=='y':
                    totalFunds=startingBank
                    print('\tYour winnings has been set to zero...')
                    break
                elif tempValue=='n':
                    print('\tAvailable Funds: ',totalFunds)
                    break

        elif menuOption==save:

            outfile=open(r'c:\Users\svasco\Documents\OOPL\Python\GameOfCraps\SavedGames.txt','a')   # 'a'= append to end of file
            try:
                tempString=userName+';'+str(totalFunds)  # string that will be written to file

                outfile.write(tempString+'\n')
            finally:
                outfile.close()
            print('\n\tName and Score has been saved...',end="\n")

        elif menuOption==quitGame:
            print('\n\t\nAre you Sure?:')
            while True:
                tempValue=str(input('(Y/N):')).lower()
                if tempValue=='y':
                    print('\tYou have quit the game! See you next time.')
                    sys.exit()
                elif tempValue=='n':
                    break


if __name__=="__main__":
    main()