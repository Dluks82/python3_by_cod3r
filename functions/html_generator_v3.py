#!/usr/bin/python3

def tag_block(content, class_name='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{class_name}">{content}</{tag}>'


def tag_list(*items):
    list = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul>{list}</ul>'


if __name__ == '__main__':

    print(tag_block('block'))
    print(tag_block('inline and class', 'info', True))
    print(tag_block('inline', inline=True))
    print(tag_block(inline=True, content='inline'))
    print(tag_block('failed', 'error'))

    print(tag_block(tag_list('Item 1', 'Item 2'), class_name='info'))
