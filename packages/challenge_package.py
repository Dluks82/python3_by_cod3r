from app.utils.generator import new_name
from app.business import name_exists
from app.business.backend import add_name


def main():
    print('Main')
    while True:
        name = new_name()
        print(name)
        if not name_exists(name):
            add_name(name)
            break
        print(f'New name created: "{name}"')


if __name__ == '__main__':
    main()
