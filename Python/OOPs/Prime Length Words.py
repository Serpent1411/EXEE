text="The quick brown fox jumps over the lazy dog."

def prime_word_length(x): 
    if x < 2:
        return False
    for k in range(2,int(x**0.5)+1):
        if x % k == 0:
            return False
    return True

def prime_word(text):
    a = text.split()
    prime_words = []
    for a in a:
        if prime_word_length(len(a)):
            prime_words.append(a)

    return " ".join(prime_words) 

y = prime_word(text)

print(y) 

