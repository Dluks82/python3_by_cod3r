def tag_block(text, class_name='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{class_name}">{text}</{tag}>'


if __name__ == '__main__':

    print(tag_block('block'))
    print(tag_block('inline and class', 'info', True))
    print(tag_block('inline', inline=True))
    print(tag_block(inline=True, text='inline'))
    print(tag_block('failed', 'error'))
