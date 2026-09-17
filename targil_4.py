words = []
while True:
    word = input('enter a word: ')
    if word == 'quit':
        break
    words.append(word)

word_set = set(words)
found = False
for word in words:
    if word[::-1] in word_set and word[::-1] != word:
        found = True
if found:
    print('reversed match found')
else:
    print('no reversed match found')




