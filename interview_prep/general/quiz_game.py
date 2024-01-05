#!/usr/bin/python3

# Version 1 of the code
# the right number
num_right = 0

# Question 1
print('What is the capital city of france?', end='')
guess = input()
if guess.lower()=='paris':
    print("Correct!")
else:
    print("Wrong input, the answer is paris")
print("Ypu have", num_right, "out of 1 right")
#Question 2
print("Which state has only one neighbor?", end='')
guess=input()
if guess.lower() == 'maine':
    print("Correct!")
    num_right += 1
else:
    print("Wrong the answer is Maine")
print('You have', num_right, 'out of 2 right')

# Version 2 of the code
questions = ['What is the capital of france?', 'Which state has only one neighbor?']

answer = ['Paris', 'Maine']

num_right = 0

for i  in range(len(questions)):
    guess = input(questions[i])
    if guess.lower == answer[i].lower():
        print("Correct !")
        num_right = num_right + 1
    else:
        print("Wrong answer. The answer is", answer[i])
    print("You have", num_right, "out of", i+1, 'right')