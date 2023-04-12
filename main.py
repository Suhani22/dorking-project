# Importing the requirements
import random
from googlesearch import search


# Collecting the dorks from the dorks.txt file
# open file in read mode
f = open("dorks.txt", "r")

# storing all lines in a list
lines = f.readlines()

# selection of any random line/dork
ran = random.randint(0, len(lines) - 1)

# storing selected dork in target variable
target = lines[ran]
f.close()
print(target)

# Gathering Results
for i in search(target, tld="com", num=10,stop=5, pause=2):
    print(i)


