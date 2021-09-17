import requests, signal, sys

def handler(sig, frame):
    sys.exit()

signal.signal(signal.SIGINT, handler)

def is_same_char(char):
    num_of_char = len(char)
    for c in range(1, num_of_char):
        if char[c] != char[0]:
            return False
    return True

def repeat_char(char, num_of_times):
    return (char * (num_of_times//len(char) + 1))[:num_of_times]

def main():
    print("Use hexadecimal.")
    fcolor = input('Foreground color: ').strip()
    bcolor = input('Background color: ').strip()

    # Value if empty input
    if not fcolor: fcolor = '0' * 6
    if not bcolor: bcolor = 'F' * 6

    # If same character and length is less than 6
    # API prints out different result when only having 3
    if is_same_char(fcolor) and len(fcolor) != 6: fcolor = repeat_char(fcolor, 6)
    if is_same_char(bcolor) and len(bcolor) != 6: bcolor = repeat_char(bcolor, 6)

    url = 'https://webaim.org/resources/contrastchecker/?fcolor={}&bcolor={}&api'.format(fcolor, bcolor)

    response = requests.get(url, timeout=1).json()
    for k, v in response.items():
        print(k, ":", v)

if __name__ == '__main__':
    main()
