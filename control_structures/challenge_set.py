#!/usr/bin/python3

FORBIDDEN_WORDS = {'football', 'religion', 'politics'}
texts = [
    'John likes to watch football and play tennis',
    'Jane likes to play chess',
]

for text in texts:
    intersection = FORBIDDEN_WORDS.intersection(set(text.lower().split()))
    if intersection:
        print(f'Found forbidden word(s): {intersection}')
    else:
        print('No forbidden words in', text)
