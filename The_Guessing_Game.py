# learning to do the guessing game

Secret_Word = "Animal"  # That's the word
User_guess = ""
guess_Count = 0
final_guess = 3
out_of_guesses = False

while User_guess != Secret_Word and not (out_of_guesses):  # as long as user guess is
    # not the # secret word and
    # out of guesses is not False,
    # move forward with what ever is inside.
    if guess_Count < final_guess:
        User_guess = input("Is the word Name, Place, Animal or Thing, you have three tries: ")
        guess_Count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print(bool(out_of_guesses))
    # if out of guesses becomes true, there are no more guesses and therefore:
    print("Sorry, you Lose")
else:
    print("You win")

print("---------------------------------")

# Prime Numbers

start = 1
end = 10

for j in range(start, end + 1):  # # w has a range of 0,1,2,3,4,5,6,7,8,9, 10
    if j > 1:
        for new in range(2, j):  # x has a range of 2, [0,1,2,3,4,5,6,7,8,9, 10]
            if (j % new) == 0:  # the logic of prime number is: if a number is divisible
                # by any other numbers leaving a remainder of 0, it is not prime
                print(j, "is not prime")
                break  # break is required for the computer to stop computing after the first time,
                # otherwise it will compute, when w = 5 and therefore x becomes (2,5), while x = 4 and say 4 is prime
        else:
            print(j, "is prime")
