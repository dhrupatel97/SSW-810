""" 
    Implement a Rock/Papers/Scissors game where a human plays against the computer
    who randomly chooses a move.
"""

from random import choice


def get_computer_move() -> str:
    """ return the computer's random choice using random.choice """
    move: str = choice(['rock', 'paper', 'scissors'])
    return move


def get_human_move() -> str:
    """ Ask the user for R, P, or S.  Loop until given a valid input """
    while True:
        user_input: str = input("Please choose a move  from 'R', 'P', 'S' OR 'Q' TO quit: ")
    
        if user_input == 'R':
            user_input = 'rock'
            break
        elif user_input == 'P':
            user_input = 'paper'
            break
        elif user_input == 'S':
            user_input = 'scissors'
            break
        elif user_input == 'Q':
            user_input = 'quit'
            break
        else:
            print('Invalid Inputs. Please provide a valid one.')
    return user_input 


def play_game() -> bool:
    """ play Rock/Paper/Scissors
        The human may enter 'Q' or 'q' any time to stop the game.
        Get the human's move, the computer's move, and print a message with the winner.
        Return a bool to specify if the human wants to play again, 
        i.e. False when the human wants to quit or True to play again
    """
    human: str = get_human_move()

    if human == 'quit':
        return False

    computer: str = get_computer_move()

    if human == 'rock' and computer == 'scissors':
        print('rock smashes scissors. You Win!')
    elif human == 'scissors' and computer == 'paper':
        print('scissors cuts paper. You Win!')
    elif human == 'paper' and computer == 'rock':
        print('paper covers rock. You Win!')
    else:
        print("Computer Wins!")

    return True


def main() -> None:
    """ Play multiple games until the human asks to stop """
    again: bool = True
    while again:
        again = play_game()
    print("Thanks for Playing")


if __name__ == '__main__':
    main()
