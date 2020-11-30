#function that takes two strings as input, and outputs the
#  common characters/letters that they share.
def letter_count(sentence1, sentence2):
    same_letters =[]
    
    sentence1 = sentence1.casefold()
    sentence2 = sentence2.casefold()
    for letter in sentence1:
        if letter in sentence2:
            same_letters.append(letter)
    print("Letters that appear in both sentences:",same_letters)

sentence1 = input("Enter a sentence: ")
sentence2 = input("Enter another sentence: ")
letter_count(sentence1, sentence2)
