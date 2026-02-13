word = input("Enter the your string:")

def Word_count(word):
    charcter_count = {}
    for i in word:
        if word.isalpha():
            charcter_count[i] = charcter_count.get(i,0) +1 #This line indicates it will pick a character and will count and will increase the count as value.
    return charcter_count

# count = Word_count(word)
print(Word_count(word))


