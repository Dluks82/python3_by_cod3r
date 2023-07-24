def tag_block(text, class_name='success'):
    return f'<div class="{class_name}">{text}</div>'


if __name__ == '__main__':
    # Assertions
    assert tag_block('Successfully added') == \
        '<div class="success">Successfully added</div>'
    assert tag_block('Impossible to delete', 'error') == \
        '<div class="error">Impossible to delete</div>'
    print(tag_block('block'))
