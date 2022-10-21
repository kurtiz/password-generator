# import win32api 

# drives = win32api.GetLogicalDriveStrings()
# win32api.FindExecutable("*.exe")
# print (drives)

# import os

# from typing import List

# path_dir: str = "c:/Users/Jenam/Desktop"

# List[str] = os.listdir(path_dir)
# print(List)

# # list variable
# letters =  ["a", "b", "c", "d"]

# for letter in letters:
#     print(letter) # letter becomes each single element of the list as the loop runs

# #tuple variable
# fruits = ("apple", "strawberry", "orange") 

# for fruit in fruits:
#     print(fruit) # fruit becomes each single element of the tuple as the loop runs

# # set variable 
# languages = {"Java", "C++", "Python"}

# for language in languages:
#     print(language) # language becomes each single element of the set as the loop runs

# # dictionary variable
# dictionary = {  "car" : "Ford", "sneaker" : "Air max", "game" : "Soccer" }

# for index in dictionary:
#     print(index) # the id or index of each element in the dictionary will be printed

# for index in dictionary:
#     print(dictionary[index]) # each element in the dictionary will be printed

# for index in dictionary:
#     print(index + " -> " + dictionary[index]) # each element and its corresponding index or id 
#     #in the dictionary will be printed

import requests

url = "https://google.com"

requestQuery = requests.get(url)

print(requestQuery.text)