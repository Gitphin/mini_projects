from colorama import Fore
import random


def wordle_game(r, m):
    # Checks if guesses are on
    guesses = m % 2
    r_len = count = len(r)
    b_char = y_char = g_char = ""
    letts = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Display how many letters in initialized word
    print("\nGenerating word...\n\n{} Letters: {}{}{}".format(r_len, Fore.BLACK," ".join(["_" for j in range(r_len)]),Fore.RESET))
    while True:
        # Prints used and unused letters
        if b_char:
            used_chars = Fore.RESET + "\nLetter display:\n"
            for i, c in enumerate(letts):
                if not i % 9:
                    used_chars += "\n"
                if c in g_char:
                    used_chars += "{}{} {}".format(Fore.GREEN, c, Fore.RESET)
                elif c in y_char:
                    used_chars += "{}{} {}".format(Fore.YELLOW, c, Fore.RESET)
                elif c in b_char:
                    used_chars += "{}{} {}".format(Fore.BLACK, c, Fore.RESET)
                else:
                    used_chars += c + " "
            print(used_chars)
        # Print guesses if enabled
        print("\n{}[ {} guesses remaining ]".format(Fore.RESET, count)) if guesses and b_char else None
        g = input("\n{}-=Terminal Wordle=-\n{}Enter guess: ".format(Fore.BLUE,Fore.RESET)).upper()
        # Quits program
        if g == "Q" or g == "QUIT":
            print("\nQuitting...")
            break
        # Peek at correct word
        elif g == "PEEK":
            print("\n{}{}{}".format(Fore.GREEN, r, Fore.RESET))
            continue
        # Error in length of word
        elif len(g) != r_len:
            print("{}\nERROR: {}Please enter a {} letter word.".format(Fore.RED, Fore.RESET, str(r_len)))
            continue
        else:
            real_hash = {}
            real_hash.update((c, real_hash.get(c, 0) + 1) for c in r)
            compare_real = console_out = ""
            for i, char in enumerate(g):
                # Check if guess character matches (yreen)
                if char == r[i]:
                    console_out += ("{}[{}] ".format(Fore.GREEN, char))
                    if char not in g_char:
                        g_char += char
                # Check if character in real (yellow)
                elif char in r:
                    g_check = 0
                    # peaks ahead to handle overlap yellow and green
                    for i in range(len(g)):
                        if g[i] == char and g[i] == r[i]:
                            g_check += 1
                    # caps to display no more of char present past real num
                    if g_check == real_hash[char]:
                        console_out += ("{}[{}] ".format(Fore.BLACK, char))
                    else:
                        console_out += ("{}[{}] ".format(Fore.YELLOW, char))
                        real_hash[char] -= 1
                    if char not in y_char:
                        y_char += char
                # Character not correct / not in real (black/gray)
                else:
                    console_out += ("{}[{}] ".format(Fore.BLACK, char))
                    if char not in b_char:
                        b_char += char
                compare_real += char
            print("\n" + console_out)
            # If all correct (win)
            if compare_real == r: 
                print(Fore.RESET + "\nCorrect! The word was {} {}".format((Fore.GREEN + r), Fore.RESET))
                print("Guesses used: {}".format(r_len - (count) + 1))
                again = input("Type {}R{} to play again, {}C{} to change modes or anything else to quit: ".format(Fore.BLUE, Fore.RESET,Fore.BLUE, Fore.RESET)).upper()
                # Check if user wants to keep playing
                m += 1 if again == "C" else 0
                new_word = gen_word()
                wordle_game(new_word, m) if again in "RC" else print("Quitting...")
                break
            # Update guesses
            count -= 1
            # If ran out of guesses (lose)
            if guesses and not count:
                print(Fore.RESET + "\nBad rng, the word was {} {}".format((Fore.GREEN + r), Fore.RESET))
                again = input("Type {}R{} to play again, {}C{} to change modes or anything else to quit: ".format(Fore.BLUE, Fore.RESET,Fore.BLUE, Fore.RESET)).upper()
                # Check if user wants to keep playing
                new_word = gen_word()
                m += 1 if again == "C" else 0
                wordle_game(new_word, m) if again in "RC" else print("Quitting...")
                break
    return
# Generate a random word from words.txt            
def gen_word():
    with open("words.txt") as word_file:
        words = word_file.read().split()
    return random.choice(words).upper()
# Start the game 
word = gen_word()
wordle_game(word, 0)





