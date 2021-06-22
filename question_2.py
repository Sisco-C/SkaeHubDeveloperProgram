#Find the length of last word Using split()  and list
def length(word):
    
    lis = list(word.split(" "))
    return len(lis[-1])

word = "I am a Developer"
print("last word's length is",
      length(word))