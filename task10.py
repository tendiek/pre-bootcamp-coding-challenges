#function that takes in a string and then prints out all the vowels in the string
def vowel_count(sentence):
    count = 0
    my_vowels =[]
    vowels ="aeiou"
    
    sentence = sentence.casefold()
    for letter in sentence:
        if letter in vowels:
            my_vowels.append(letter)
            count += 1
    print(my_vowels)

sentence = input("Enter a sentence: ")
vowel_count(sentence)

