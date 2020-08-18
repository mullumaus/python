
def vowels(inString):
    letter =['a','e','i','o','u']
    count = 0
    inString = inString.lower()
    for l in inString:
        if l in letter:
            count = count + 1
    return count



if __name__=="__main__":
    print((vowels("Hello there!")))
