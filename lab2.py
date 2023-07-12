# Class: CIST 2742 Python Programming I
# Term: Summer 2023 Instructor: Chris Bishop
# Description: Solution to Lab #2
# Author: (Shamal Williams)# 900511291
# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.
# 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.

packet = int(input("Enter a pocket number: "))
if packet < 0 or packet > 36:
    print("The packet number should be between 0 and 36!!")

else:
    color = ""
    if packet == 0:
        color = "green"
    elif (packet >= 1 and packet <= 10) or (packet >= 19 and packet <= 28):
        if packet % 2 == 0:
            color = "black"
        else:
            color = "red"
    elif (packet >= 11 and packet <= 18) or (packet >= 29 and packet <= 36):
        if packet % 2 == 0:
            color = "red"
    else:
        color = "black"

print("Packet color is", color)
