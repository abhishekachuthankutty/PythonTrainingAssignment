import requests

def display_with_spaces(word):
    new_word = ''
    for i in word:
        new_word = new_word + i + ' '
    return new_word

def unmask_letter(masked,unmasked, letter_to_be_unmasked):
    masked_list = list(masked)
    unmasked_list = list(unmasked)
    len = 0
    for i in unmasked_list:
        if i == letter_to_be_unmasked:
            masked_list[len] = letter_to_be_unmasked
        len += 1
    return "".join(masked_list)

def get_word(url):
    r = requests.get(url = url)
    return r.json()


url = "https://random-word-api.herokuapp.com/word"
while True:
    data = get_word(url)
    word = ''.join(data)
    if not word.isalpha():
        data = get_word(url)
        word = ''.join(data)
    else:
        break   

print('Hangman')
print('Guess The Word!')
lives = 6
entered_letters = []
discoveredOrDead = False
masked_word = ''
for i in range(len(word)):
    masked_word += '_'


while not discoveredOrDead:
    print(display_with_spaces(masked_word))
    print('Letters entered so far:' + ' '.join(entered_letters)) 
    print('You have ' + str(lives) + ' lives left')
    letter = input('Enter a letter: ')     
    if len(letter) > 1:
        print('Only one letter can be entered!')
    elif not letter.isalpha():
        print('Only letters can be entered!')
    elif letter in entered_letters:
        print(letter + ' has already been entered!')
    elif word.find(letter) != -1:
        print(letter + ' is part of the word!')
        entered_letters.append(letter)
        masked_word = unmask_letter(masked_word,word,letter)
        if masked_word.find('_') == -1:
            print('Great Job! The word is ' + word)
            discoveredOrDead = True
    else:
        lives -= 1
        entered_letters.append(letter)
        print(letter + ' is not part of the word!')
        if lives <= 0:
            discoveredOrDead = True
            print('Sorry you are out of lives, the word was ' + '"' + word + '"')