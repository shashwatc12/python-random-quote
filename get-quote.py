import random

def RunMyCode():
     f = open("quotes.txt") #read the file
     quotes = f.readlines() #read the lines from file into array
     f.close()
     last =len(quotes) -1 
     rnd = random.randint(0, last) #get the random number
     print(quotes[rnd])

if __name__== "__main__":
  RunMyCode()
