#!/usr/bin/python3

def tag_block(content, *args, class_name='success', inline=False):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args)
    return f'<{tag} class="{class_name}">{html}</{tag}>'


def tag_list(*items):
    list = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul>{list}</ul>'


if __name__ == '__main__':

    print(tag_block('block'))
    print(tag_block('inline and class', class_name='info', inline=True))
    print(tag_block('inline', inline=True))
    print(tag_block(inline=True, content='inline'))
    print(tag_block('failed', 'error'))

    print(tag_block(tag_list('Item 1', 'Item 2'), class_name='info'))
    print(tag_block(tag_list, 'Saturday', 'Sunday', class_name='info', inline=True))
