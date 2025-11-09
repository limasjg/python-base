#Collection is a single variable with many values stored
# list = [] ordered, changeable, duplicates ok.
# set = {} unordered, unchangeable, but add/remove ok, no duplicates
# tuple = () ordered and unchangeable, duplicate ok, faster.


# List
# animes = ["Naruto", "Dragon Ball", "Hunter x Hunter", "One punchman"]

# print(animes[::2]) # You can indexing the values
#print(dir(animes))
# print(help(animes))
#print(len(animes))
#print("Naruto" in animes)
# animes[0] = "One Piece"
# animes.append("One Piece")
# animes.remove("One punchman")
# animes.sort()
# animes.reverse()
# animes.clear()
# print(animes.index("Naruto"))
# print(animes.count("Naruto"))
# print(animes)

# for anime in animes:
#     print(anime)

#Set
# fruits = {"banana", "apple", "orange", "coconut"}

#print(dir(fruits))
# print(help(fruits))
#print(len(fruits))
# fruits.add("pineapple")
# fruits.remove("apple")
# print(fruits)


 #Tuple

fruits = ("banana", "apple", "orange", "coconut", "coconut")
# print(fruits)
# print(len(fruits))
# print("apple" in fruits)
# print(fruits.index("apple"))
print(fruits.count("coconut"))