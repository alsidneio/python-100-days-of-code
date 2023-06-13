# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true_key = "true"
love_key = "love"
total = 0 

name = name1.lower() + name2.lower()

for letter in name:
    if letter in true_key:
        total += 10
    
    if letter in love_key:
        total += 1

if total < 10 or total >90:
    print(f'Your score is {total}, you go together like coke and mentos.')
elif total >40 and total < 50:
    print(f'Your score is {total}, you are alright together.')
else:
    print(f'Your score is {total}.')