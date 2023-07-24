#!/usr/bin/python3

block_attribs = ('block_accesskey', 'block_id')
ul_attribs = ('ul_id', 'ul_style')


def filter_attrbs(informed, supported):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informed.items() if k in supported)


def tag_block(content, *args, class_name='success', inline=False, **new_attribs):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args, **new_attribs)
    attribs = filter_attrbs(new_attribs, block_attribs)
    return f'<{tag} {attribs} class="{class_name}">{html}</{tag}>'


def tag_list(*items, **new_attribs):
    list = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul {filter_attrbs(new_attribs, ul_attribs)}>{list}</ul>'


if __name__ == '__main__':

    print(tag_block('block'))
    print(tag_block('inline and class', class_name='info', inline=True))
    print(tag_block('inline', inline=True))
    print(tag_block(inline=True, content='inline'))
    print(tag_block('failed', 'error'))

    print(tag_block(tag_list('Item 1', 'Item 2'), class_name='info'))
    print(tag_block(tag_list, 'Saturday', 'Sunday', class_name='info', inline=True))

    print(tag_block(tag_list, 'Item 1', 'Item 2', class_name='info',
          block_accesskey='m', block_id='content', ul_id='list', ul_blabla='abc', ul_style='color:red'))
