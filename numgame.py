#!/usr/bin/env python3
def check_input_valid(inp):
    acceptable_inputs = ['c', 'l', 'h', 'y', 'n']
    if inp.lower() in acceptable_inputs:
        return inp.lower()

if __name__ == '__main__':
    playing = True
    guessed = False

    total_guesses, guesses_this_game = 0, 0
    games_played, min_bounds = 1, 1
    max_bounds = int(input("Please enter a number n: "))
    game_max_bounds = max_bounds
    instruction = ''

    while playing and not guessed:

        # guess at midpoint
        guess = (min_bounds + max_bounds) // 2

        # iterate stats
        guesses_this_game += 1
        total_guesses += 1

        # see if there's only one option left
        if guess == min_bounds == max_bounds:
            instruction = 'c'
        else:
            instruction = str(input('{}? '.format(guess)))

        if instruction == 'c':
            print("Your number is {}.\nIt took me {} guesses.\nI averaged {} guesses per game for {} game(s).".format(guess, guesses_this_game, (total_guesses/games_played), games_played))

            # update state now that we've completed this round
            guessed = True
            guesses_this_game = 0

            # iterate games played
            games_played += 1

            play_again = check_input_valid(input('Play again (y/n)?'))
            if play_again == 'y':
                # finish resetting state
                guessed = False
                max_bounds = game_max_bounds
                min_bounds = 1
            if play_again == 'n':
                playing = False
        elif instruction == 'h':
            # must be lower than the current guess, decrease bounds by one
            max_bounds = guess - 1
        elif instruction == 'l':
            # must be higher than the current guess, increase bounds by one
            min_bounds = guess + 1
        else:
            print('Unknown instruction, please try again')


    print("Thanks for playing!")


