RUS_ALPHABET = 32
ENG_ALPHABET = 26

ENG_UP = ord('A')
ENG_DN = ord('a')

RU_UP = ord('А')
RU_DN = ord('а')

TYPE_ROUTE = 1
TYPE_DIGIT = 2

SYMB = '.,!#$%&*+-=?@^_ '
NUMBERS = '0123456789'


def exit_programm(text, key):
    if key != 0:
        print(f'Here is your {key} text: {text}')
        ask = input('Want to encode or decode more text? Y to continue or anykey to exit.')
        if ask.lower() == 'y':
            config()
    print('Bye!')
    exit()


def validation(data):
    text = data[0].lower()
    key = data[1]

    while True:
        if text == 'q':
            exit_programm(0, 0)

        if key == TYPE_ROUTE:
            if text == 'e' or text == 'd':
                return text
            else:
                text = input('Be sure you use "E" to encode or "D" to decode. Press "Q" to exit programm. ').lower()

        if key == TYPE_DIGIT:
            if text.isdigit():
                return int(text)
            else:
                text = input('Be sure you use digits. Press "Q" to exit programm. ').lower()


# language autodetect. Returns list [text, 'EN'] or list [text, 'RU']
def language_auto_detect(text):
    while True:
        lang_en = False
        lang_ru = False
        other = False
        for c in text:
            if c in SYMB or c in NUMBERS:
                continue
            num = ord(c)
            # detect if there is RU and EN letters
            if 65 <= num <= 122:
                lang_en = True
            elif 1040 <= num <= 1103:
                lang_ru = True
            else:
                other = True

        if (lang_ru and lang_en) or other:
            text = input('Be sure you use letters from either English or Russian. Press "Q" to exit ')
            if text.lower() == 'q':
                exit_programm(0, 0)
        elif lang_en:
            return [text, ENG_UP, ENG_DN, ENG_ALPHABET]
        elif lang_ru:
            return [text, RU_UP, RU_DN, RUS_ALPHABET]


def encode(text, shift):
    # text is list [text, code of first letter, code of last letter, mod of alphabet]
    encode_str = ''
    # setup vars depend on lang
    upper = text[1]
    down = text[2]
    mod = text[3]

    for el in text[0]:
        if el in SYMB or el in NUMBERS:
            encode_str += el
        elif el.isupper():
            cur_n = upper + (ord(el) - upper + mod + shift) % mod
            encode_str += chr(cur_n)
        elif el.islower():
            cur_n = down + (ord(el) - down + mod + shift) % mod
            encode_str += chr(cur_n)
    exit_programm(encode_str, 'encoded')


def decode(text, shift):
    # text is list [text, code of first letter, code of last letter, mod of alphabet]
    decode_str = ''
    # setup vars depend on lang
    upper = text[1]
    down = text[2]
    mod = text[3]

    for el in text[0]:
        if el in SYMB or el in NUMBERS:
            decode_str += el
        elif el.isupper():
            cur_n = upper + (ord(el) - upper + mod - shift) % mod
            decode_str += chr(cur_n)
        elif el.islower():
            cur_n = down + (ord(el) - down + mod - shift) % mod
            decode_str += chr(cur_n)
    exit_programm(decode_str, 'decoded')


def config():
    route = validation(
        [input('What should I do? Press "E" to encode or "D" to decode. Press "Q" to exit programm. '), TYPE_ROUTE])
    shift = validation(
        [input('Enter shift step. Positive digit is required. Press "Q" to exit programm. '), TYPE_DIGIT])
    if route == 'e':
        text = language_auto_detect(input('Type text to encode '))
        encode(text, shift)
    else:
        text = language_auto_detect(input('Type text to decode '))
        decode(text, shift)


if __name__ == '__main__':
    config()
