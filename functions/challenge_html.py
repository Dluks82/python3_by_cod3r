#!/usr/bin/python3

def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    attrs = ''.join(f'{k}="{v}"' for k, v, in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'

# Expected result
# <p class="alert"><span >Python3 course, by </span><strong id="do">Diogo Oliveira</strong><span > and </span><strong id="lo">Lucas Oliveira</strong><span >.</span></p>


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Python3 course, by '),
            tag('strong', 'Diogo Oliveira', id='do'),
            tag('span', ' and '),
            tag('strong', 'Lucas Oliveira', id='lo'),
            tag('span', '.'),
            html_class='alert')
    )
