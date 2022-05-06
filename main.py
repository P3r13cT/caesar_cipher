# Initializing english / russian dictionary
dictionary = []
dictionary.append([chr(i) for i in range(ord('a'), ord('z') + 1)])
dictionary.append([i.upper() for i in dictionary[0]])
dictionary.append([chr(i) for i in range(ord('а'), ord('я') + 1)])
dictionary[2].insert(6, 'ё')
dictionary.append([i.upper() for i in dictionary[2]])
dictionary[3].insert(6, 'Ё')


def decipher(txt, step, dct):
    answer = ''
    for i in txt:
        result = None
        if i.isupper() == i.isalpha() is True:
            result = ord(i) + step
            while result > ord(dct[1][-1]):
                result -= len(dct[1])
            while result < ord(dct[1][0]):
                result += len(dct[1])
        elif i.islower() == i.isalpha() is True:
            result = ord(i) + step
            while result > ord(dct[0][-1]):
                result -= len(dct[0])
            while result < ord(dct[0][0]):
                result += len(dct[0])
        if result is None:
            answer += i
        else:
            answer += chr(result)
    return answer


def caesar_cipher(txt, mode, lang, step):
    if mode == 2:
        step = -step
    if lang == 'en':
        return decipher(txt, step, dictionary[:2])
    if lang == 'ru':
        return decipher(txt, step, dictionary[2:])


lang = input('Choose your language (en/ru): ')
if lang == 'ru':
    text = input('Введите ваш текст: ')
    shift = ''
    while shift.isdigit() is False:
        shift = input('Введите сдвиг: ')
    shift = int(shift)
    mode = ''
    while mode.isdigit() is False:
        mode = input('Режимы:\n 1) Зашифровать\n 2) Расшифровать\nВыберите режим: ')
else:
    text = input('Enter your text: ')
    shift = ''
    while shift.isdigit() is False:
        shift = input('Enter a shift: ')
    shift = int(shift)
    mode = ''
    while mode.isdigit() is False:
        mode = input('Modes:\n 1) Encrypt\n 2) Decrypt\nSelect your mode: ')
print(caesar_cipher(text, mode, lang, shift))
