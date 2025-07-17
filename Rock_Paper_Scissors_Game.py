import random

options=["rock","paper","scissors"]

system=random.choice(options)
user=input("Enter anyone from rock,paper or scissors : ")

print(f"System choice : {system}")
print(f"user choice : {user}")

if user==system :
    print("Tie")
elif (user=="rock" and system=="scissors") or (user=="paper" and system=="rock") or (user=="scissors" and system=="paper"):
    print("user win")
else:
    print("system win")