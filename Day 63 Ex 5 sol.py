

# **************************************************************************** #
# import random

# print("""Welcome To The Game,
# You Will Get 3 Rounds,
# The Total Socre Will Be Evaluated At Last And Winner Will Be Decided,
# You Will Get 10 Points For Each Correct Answer And -5 For Each Wrong Answer
# So Let's Start!\n""")

# choices = ["Snake","Water","Gun"]
# user_points = 0
# computer_points = 0

# def get_results(user_choice:int,computer_choice:int):
#     if user_choice == computer_choice:
#         return "It's A Draw\n'0' Points Goes To Each\n"
#     elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
#         user_points += 10
#         computer_points -= 5
#         return f"You Won This Round!!\nPoints Are:\nYour Points: {user_points}\nComputer Points: {computer_points}\n"
#     elif (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2) or (user_choice == 1 and computer_choice == 3):
#         user_points -= 5
#         computer_points += 10
#         return f"You Loosed This Round!!\nPoints Are:\nYour Points: {user_points}\nComputer Points: {computer_points}\n"
#     else:
#         ...

# for i in range(1,3):

#     print(f"Round {i}: \n")

#     users_choice = int(input("Kindly Choose Between Snake, Water, Gun (1-3): "))
#     if users_choice == 1 or users_choice == 2 or users_choice == 3:
#         ...
#     else:
#         raise ValueError("You Enterd The Wrong Input!!")

#     computers_choice = random.randint(1, 3)

#     print("Computer choosed: ", str(lambda a: choices[a]))

#     print(get_results(users_choice,computers_choice))

#     if i == 3:
#         print("Rounds Are Over Now Let's Take A Look At The Results\n")
#         break

# if computer_points > user_points:
#     print("Points Are:\nYour Points: {user_points}\nComputer Points: {computer_points}\nYou Loosed The Game!!\n Better Luck Next Time!")
# else:
#     print("Points Are:\nYour Points: {user_points}\nComputer Points: {computer_points}\nYou Won The Game!!\nCongratulations!!!!")


import random


def check(comp, user):
    if comp == user:
        return 0

    if (comp == 0 and user == 1):
        return -1

    if (comp == 1 and user == 2):
        return -1

    if (comp == 2 and user == 0):
        return -1

    return 1


comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if (score == 0):
    print("Its a draw")
elif (score == -1):
    print("You Lose")
else:
    print("You Won")
