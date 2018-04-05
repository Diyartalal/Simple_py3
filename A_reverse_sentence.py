def reverse(sentence):
    return ' '.join(sentence.split()[::-1])
sentence=input("Enter a sentence : ")
print(reverse(sentence))
