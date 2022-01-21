##Assignment One, Tic-Tac-Toe Game
##Author: Aubury Orr
##Class: CSE 210 Programming With Classes
##Teacher: Brother Hayes


from re import T
from tkinter import N


def main():
    ##This is the main menu, with a time function for effect
    import time
    print('TICK-TACK-TOE')
    print()
    time.sleep(1)
    input('Press \033[1;32;40m `ENTER` \033[0m to continue    ')


    ## Lists out the variables for each space, these can be changed 
    ## by the users as they imput answers with x's and 0's
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'

    ## All the possible answers that could result in a victory, these
    ## will be compared to the players answers continually.
    answer1 = [1,2,3]
    answer2 = [4,5,6]
    answer3 = [7,8,9]
    answer4 = [1,4,7]
    answer5 = [2,5,8]
    answer6 = [3,6,9]
    answer7 = [1,5,9]
    answer8 = [3,5,7]

    ## Makes empty lists we will need later to be appended to.
    player_one_list = []
    player_two_list = []
    victory = 'undecided'
    all_list = []
    counter = 1

    ## This while loop with have the turns go on until a tie or a win
    while victory == 'undecided':
        
        ## Calls the display_game_board function which generates the game graphic
        display_game_board(one,two,three,four,five,six,seven,eight,nine)

        ##Ask's the user for their first answer. We will then save that answer
        ##to their specific list, so we can keep track of them, and then an all
        ##list so we will know if all spaces are taken with no victor (tie.) Lists
        ##are then sorted even though that may bot be nessisary
        playeronechoice = input('\033[1;35;40mPlayer one\033[0m, please select a number: ')
        player_one_list.append(int(playeronechoice))
        player_one_list.sort()
        all_list.append(int(playeronechoice))
        all_list.sort()

        ##Checks to see which spot the user selected
        if playeronechoice == one:
            one = '\033[1;35;40mO\033[0m'
        elif playeronechoice == two:
            two = '\033[1;35;40mO\033[0m'
        elif playeronechoice == three:
            three = '\033[1;35;40mO\033[0m'
        elif playeronechoice == four:
            four = '\033[1;35;40mO\033[0m'
        elif playeronechoice == five:
            five = '\033[1;35;40mO\033[0m'
        elif playeronechoice == six:
            six = '\033[1;35;40mO\033[0m'
        elif playeronechoice == seven:
            seven = '\033[1;35;40mO\033[0m'
        elif playeronechoice == eight:
            eight = '\033[1;35;40mO\033[0m'
        elif playeronechoice == nine:
            nine = '\033[1;35;40mO\033[0m'

        ##Board shows up again
        display_game_board(one,two,three,four,five,six,seven,eight,nine)

        ##This will check and see if all the items for one of our answer
        ##lists show up in the users list. This is nessisary becuase their
        ##lists will not be the same and may have other numbers.
        check1 = all(item in player_one_list for item in answer1)
        check2 = all(item in player_one_list for item in answer2)
        check3 = all(item in player_one_list for item in answer3)
        check4 = all(item in player_one_list for item in answer4)
        check5 = all(item in player_one_list for item in answer5)
        check6 = all(item in player_one_list for item in answer6)
        check7 = all(item in player_one_list for item in answer7)
        check8 = all(item in player_one_list for item in answer8)
        
        ##Checks to see if any are true, which would mean a player one victory.
        if check1 is True or check2 is True or check3 is True or check4 is True or check5 is True or check6 is True or check7 is True or check8 is True:
            print('\033[1;35;40mPLAYER ONE WINS\033[0m')
            victory = 'playerone'
        ##Checks to see if all the spaces are filled. If they are with no victors
        ##at this point, than it is a tie game.
        elif all_list == [1,2,3,4,5,6,7,8,9]:
            print('\033[1;32;40mTIE-GAME\033[0m')
            victory = 'draw'
        else:
            ##If neither of those are true than it is player 2's turn, which is coded
            ##basically the same as players one, just with differing variables.
            print()
            playertwochoice = input('\033[1;36;40mPlayer two\033[0m, please select a number: ')
            player_two_list.append(int(playertwochoice))
            player_two_list.sort()
            all_list.append(int(playertwochoice))
            all_list.sort()

            if playertwochoice == one:
                one = '\033[1;36;40mX\033[0m'
            elif playertwochoice == two:
                two = '\033[1;36;40mX\033[0m'
            elif playertwochoice == three:
                three = '\033[1;36;40mX\033[0m'
            elif playertwochoice == four:
                four = '\033[1;36;40mX\033[0m'
            elif playertwochoice == five:
                five = '\033[1;36;40mX\033[0m'
            elif playertwochoice == six:
                six = '\033[1;36;40mX\033[0m'
            elif playertwochoice == seven:
                seven = '\033[1;36;40mX\033[0m'
            elif playertwochoice == eight:
                eight = '\033[1;36;40mX\033[0m'
            elif playertwochoice == nine:
                nine = '\033[1;36;40mX\033[0m'

            display_game_board(one,two,three,four,five,six,seven,eight,nine)

            check11 = all(item in player_two_list for item in answer1)
            check12 = all(item in player_two_list for item in answer2)
            check13 = all(item in player_two_list for item in answer3)
            check14 = all(item in player_two_list for item in answer4)
            check15 = all(item in player_two_list for item in answer5)
            check16 = all(item in player_two_list for item in answer6)
            check17 = all(item in player_two_list for item in answer7)
            check18 = all(item in player_two_list for item in answer8)

            if check11 is True or check12 is True or check13 is True or check14 is True or check15 is True or check16 is True or check17 is True or check18 is True:
                print('\033[1;36;40mPLAYER TWO WINS\033[0m')
                victory = 'playertwo'
            elif all_list == [1,2,3,4,5,6,7,8,9]:
                print('\033[1;32;40mTIE-GAME\033[0m')
                victory = 'draw'
            else:
                counter += 1
                print(f'ROUND {counter}')

def display_game_board(one,two,three,four,five,six,seven,eight,nine):
    print()
    print(f'{one} | {two} | {three}')
    print(f'----------')
    print(f'{four} | {five} | {six}')
    print(f'----------')
    print(f'{seven} | {eight} | {nine}')
    print(f'----------')
if __name__ == "__main__":
    main()