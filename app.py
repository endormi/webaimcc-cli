import requests
import signal
import sys
from charred import is_same_char, repeat_char


def handler(sig, frame):
    sys.exit()


def get_input(prompt, default_value):
    value = input(prompt).strip()
    return value or repeat_char(default_value, 6)


def main():
    signal.signal(signal.SIGINT, handler)

    print("Use hexadecimal (without #).")
    fcolor = get_input('Foreground color: ', '0')
    bcolor = get_input('Background color: ', 'F')

    if is_same_char(fcolor) and len(fcolor) < 6:
        fcolor = repeat_char(fcolor, 6)
    if is_same_char(bcolor) and len(bcolor) < 6:
        bcolor = repeat_char(bcolor, 6)

    url = 'https://webaim.org/resources/contrastchecker/?fcolor={}&bcolor={}&api'.format(fcolor, bcolor)

    response = requests.get(url, timeout=1).json()
    for k, v in response.items():
        print(k, ":", v)


if __name__ == '__main__':
    main()
