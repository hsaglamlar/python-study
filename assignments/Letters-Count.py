'''This program counts all chars of an input sentence emtered by the user.'''
sentence = input("Please enter a sentence :")
counts={}
for item in sentence:
    counts[item] = sentence.count(item)

print(counts)