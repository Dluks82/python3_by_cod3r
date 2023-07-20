#!/usr/bin/python3

FORBIDDEN_WORDS = ('football', 'religion', 'politics')
texts = [
    'John likes to watch football and play tennis',
    'Jane likes to play chess',
]

for text in texts:
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print(f'Found forbidden word: { word}')
            break
    else:
        print('No forbidden words in', text)

# The else clause is executed only if the loop terminates normally, that is, if
# no break statement is executed.
# The else clause won't be executed if the loop is terminated by a break
# statement.
# The else clause is also executed when the loop is empty, that is, when the
# sequence to be iterated over is empty.
# The else clause is also executed when the sequence to be iterated over
# contains no items that satisfy the condition in the if statement.
# The else clause is also executed when the sequence to be iterated over
# contains no items at all.
# The else clause is also executed when the sequence to be iterated over
# contains no items that satisfy the condition in the if statement and the loop
# is terminated by a break statement.
# The else clause is also executed when the sequence to be iterated over
# contains no items at all and the loop is terminated by a break statement.
# The else clause is also executed when the sequence to be iterated over
# contains no items that satisfy the condition in the if statement and the loop
# is empty.
