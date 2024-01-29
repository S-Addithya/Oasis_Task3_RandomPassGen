import random
import string
print("Welcome to Password Generator.")
noletters=int(input("How many letters do you want: "))
num=int(input("How many Integers do you want: "))
spchara=int(input("How many special characters do you want: "))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']
passwordelements=[]
for i in range(noletters):
    passwordelements=passwordelements+[random.choice(letters)]
for i in range(num):
    passwordelements=passwordelements+[random.choice(numbers)]
for i in range(spchara):
    passwordelements=passwordelements+[random.choice(symbols)]
random.shuffle(passwordelements)
str=""
for i in range(noletters+num+spchara):
    str=str+passwordelements[i]
print(str)