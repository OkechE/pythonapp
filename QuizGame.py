import tkinter as tk
from tkinter import filedialog, Text 

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width= 700, bg="#263D42")
canvas.pack ()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

print("Welcome to the game.")

playing = input("Do you wish to play my quiz?  yes/no ")
print(playing)
if playing.lower() != "yes":
    print("Goodbye")
    quit()

print("Let's begin.")
score = 0

answer = input("First question. What is the circumfirence of the sun? ")
print(answer)
if answer.lower() == "2.720984 million miles":
    print("Cheaters never win!")
    quit()
else:
    print("I was just trying to see if you'd cheat. On to the real test. >:)")

answer = input("Anyways... Question 2. What is 5+5? ")
print(answer)
if answer.lower() == "10":
    print("Correct. Good job!")
    score += 1
else:
    print("Incorrect.")

answer = input("Question 3. What kind of animals are bears? ")
print(answer)
if answer.lower() == "mammals":
    print("Correct. Keep it up!")
    score += 1
else:
    print("Incorrect.")

answer = input("Question 4. What year was the declariation of independence signed? ")
print(answer)
if answer.lower() == "1776":
    print("Correct. One more question!")
    score += 1
else:
    print("Incorrect.")


answer = input("And for the last question! What is 1+1? ")
print(answer)
if answer.lower() == "2":
    print("Correct. You completed the test!")
    score += 1
else:
    print("Incorrect.")

print ("You got " + str(score) + " questions correct!")
if score == 4:
    print("You got a perfect score, great job!")
else:
    print("Thank you for playin my quiz!")

