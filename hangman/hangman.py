from modules import list, art
import os

chances = 6
word = list.word_list()
# print(word)
underscore = '_'
encrypted_word = ''
count = 0
new_word = ''

def add_spaces(parm):
    list=[]
    new_word = ''
    for letter in parm:
        list.append(letter)
    for letter in list:
        if new_word == '':
            new_word = letter
        else:
            new_word = new_word + " " + letter
    return new_word

os.system('cls')
print(art.welcome(), '\n')
for i in range(len(word)):
    encrypted_word = encrypted_word + underscore
print(rename.add_spaces(encrypted_word))

while '_' in encrypted_word:
    positions = []
    if chances == 0:
        print(art.chances(chances))
        print('You lose! The correct answer was', rename.add_spaces(word))
        quit()

    guess = input('\nGuess a letter: ')
    if len(guess) < 1:
        print('No letter guessed')
        continue
    if guess not in word:
        chances = chances - 1
        print(art.chances(chances))
        print('Wrong answer!', 'chance remaining', chances)
        print(rename.add_spaces(encrypted_word))

        continue

    if guess in word:
        print(art.chances(chances))
        print(guess, 'is a correct guess!')
        count = 0
        for i in word:
            if i == guess:
                positions.append(count)
            count = count + 1

        index = 0
        new_word = ''
        while index < len(word):

            if index in positions:
                letter = word[index]
            else:
                letter = encrypted_word[index]

            new_word = new_word + letter

            index = index + 1
        encrypted_word = new_word
        print(rename.add_spaces(new_word))

print('Congrats! You have won. The answer is', new_word)
