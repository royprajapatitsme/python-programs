sentence = input("Enter a sentence :").lower()

vowels = 'aeiouAEIOU'

count = 0

for char in sentence:
    if char in vowels:
        count = count+1

print("The number of vowels in the sentence is:", count)

