sentence = input("Type a sentence of at least 3 words : \n")
words = sentence.split()
if len(words) < 4:
    print("You need to type more words!")
else:
    print("Wow you got it right!")
