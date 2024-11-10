items = ('mix', 'xyz', 'apple', 'xanadu', 'rovio')

x_words = []
other_words = []

for word in items:
    if word.startswith('x'):
        x_words.append(word)
    else:
        other_words.append(word)

x_words.sort()
other_words.sort()

sorted_items = x_words + other_words

print(sorted_items)


words = ('xxx','aaa','r5t6yy','g','wow')

count = 0

for counter in words:
    if len(counter) >= 2 and counter[0] == counter[-1]:
        count += 1

print(count)

password = ('banana')
attempts = 3

for i in range(attempts):
    guess = input('guess the password: ')

    if guess == password:
        print('welldone you win')
        break

    else:
        print(f'you failed, try again. you have {attempts - i -1} attemopts(s) left')

else:
    print('you lost')