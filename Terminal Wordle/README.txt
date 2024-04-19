===================================================
            -=+=- Terminal Wordle -=+=- 

              Created by Alek Holiman
===================================================


Set Up:

First install colorama by typing 'pip install colorama'

> pip install colorama


Next once that is done, type "python wordle.py" into 
your terminal from the 'Terminal Wordle' directory

Terminal Wordle> python wordle.py

You are all ready to go!


How To Play:

It will start up with the amount of letters in the word 
to guess and will ask you to enter a guess, like below

|
| Generating word...
|
|
| 5 Letters: _ _ _ _ _ _
|
| -=Terminal Wordle=-
| Enter guess:


Once you enter in a word it will output like this,
and show different colors as follows:

- Green: Right letter at right spot
- Yellow: Right letter at wrong spot
- Grey/Black: Letter not in word / too many
- None (For Display): word not used yet

This is an example of what it might look like:

| -=Terminal Wordle=-
| Enter guess: hello
|
| [H] [E] [L] [L] [O] 
| 
| Letter display:
| 
| A B C D E F G H I
| J K L M N O P Q R
| S T U V W X Y Z


You can either keep guessing until you get it right OR
you can type in 'peek' to see the right word, displayed in green

| Enter guess: peek
|
| MARIO

You can enter that word into your next guess and it will show
a prompt telling you that you won!

| Correct! The word was BEACH 
| Guesses used: 2
| Type R to play again, C to change modes or anything else to quit:

You can now choose to play again by typing R and you can change
the difficulty by typing C, anything else will quit the program.
If you change modes at this point you will now have a limited
amount of guesses, and are able to lose the game! Good luck!


Finally, you are able to exit the program at any time by typing
'q' or 'quit' as your guess. If succesful it will look like so:

| -=Terminal Wordle=-
| Enter guess: quit
| Quitting...


Errors/Bugs:

If you enter in an invalid word length it
will tell you to enter in a new word:

| ERROR: Please enter a 5 letter word.

Please do not enter any numbers or anything
other than letters, it will not work properly

Make sure not to use 'q', 'quit', or 'peek'
as words if you choose to edit words.txt (see below)


Features:

You can choose whatever words you want for this wordle!

I have provided a sample "words.txt", but you can edit or
replace this file with whatever words you would like to use.
To do so, make sure it is laid out like so:

| cat
| dog
| bird
| ...

That is all you should have to know! I hope you enjoy playing 
with my program and reach out if you would like to report any feedback