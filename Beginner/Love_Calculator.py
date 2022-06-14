# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

true = lower_case_name1.count("t") + lower_case_name1.count("r") + lower_case_name1.count("u") + lower_case_name1.count(
    "e")
love = lower_case_name2.count("l") + lower_case_name2.count("o") + lower_case_name2.count("v") + lower_case_name2.count(
    "e")

love_score = int(f"{true}{love}")

if (love_score > 90) or (love_score < 10):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
