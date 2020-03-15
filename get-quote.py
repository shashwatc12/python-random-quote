import random

def RunMyCode():
     f = open("quotes.txt") #read the file
     quotes = f.readlines() #read the lines from file into array
     f.close()
     last =len(quotes) -1 
     rnd = random.randint(0, last) #get the random number
     rnd2 = random.randint(0, last) #get the random number
     print(quotes[rnd])
     print("If you like the first quote check out the next one \n ")
     print(quotes[rnd2])
     print ("Please provide a short quote from your favorite quote collection")
     quote=input()
     print("Thank you for your quote. We will use this quote for our next run. Here is what you provided :"+ quote)
if __name__== "__main__":
  RunMyCode()
