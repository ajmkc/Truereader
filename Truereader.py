
import random 
import time
import webbrowser
import os
x = random.randint(1, 3)
c = 0
f = open("Truetest.txt","r")    
y = random.randint(1, 2)
if y==1:
    print(f.read())
    for i in range(1,121):
        time.sleep(1)
        if i == 120:
            break
if y==2:
    while c < 36:
        print(f.readline())
        c+=1
        time.sleep(3)
    for i in range(1,13):
        time.sleep(1)
        if i == 12:
            break
os.system('cls')      
print("Move on to the quiz.")
time.sleep(3)
url = 'https://codepen.io/pen/?template=VwaObrB'
webbrowser.open_new(url)
