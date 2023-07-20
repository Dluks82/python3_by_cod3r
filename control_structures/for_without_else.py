#!/usr/bin/python3

FORBIDDEN_WORDS = ('football', 'religion', 'politics')
texts = [
    'John likes to watch football and play tennis',
    'Jane likes to play chess',
]

for text in texts:
    found = False
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print(f'Found forbidden word: {word}')
            found = True
            break
    if not found:
        print('No forbidden words found in', text)
