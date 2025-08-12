import random
import time

print("Welcome to the Future Love Predictor! 💖\n")
time.sleep(1)

name = input("Enter your name: ")
print(f"Hello, {name}! Let's see what the future holds for you... 😊\n")
time.sleep(1)

crush = input("Enter your crush's name: ")

print(f"\nAnalyzing the future of {name} and {crush}...")
time.sleep(2)

guess = random.randint(1, 100)

if guess > 80:
    print(f"🌟 Wow! {name} and {crush} are destined for marriage! 💍 True love awaits you both!")
elif guess > 50:
    print(f"💬 Things are heating up! {name} and {crush} have started chatting. Let's see where this goes!")
elif guess > 30:
    print(f"😅 Looks like {name} might be in the friendzone with {crush}. But hey, friendships are important too!")
else:
    print(f"💔 Unfortunately, it seems the relationship between {name} and {crush} might not work out. Keep your hopes up!")

