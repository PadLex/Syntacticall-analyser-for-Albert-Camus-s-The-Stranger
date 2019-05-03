import re
import enchant


input_path = "book.txt"
output_path = "clean.txt"

d = enchant.Dict("en_US")


def fix_words():
    with open(input_path, 'r') as input_file:

        words = input_file.read().split(' ')

        out = ""

        for i, dirty in enumerate(words):
            word = re.sub(r'[^a-zA-Z0-9_\']', '', dirty)

            combo = word + re.sub(r'[^a-zA-Z0-9_\']', '', words[i+1]) if i < len(words)-1 else False

            if combo and d.check(combo):
                out += " " + combo
                print(combo, "fixed")
                continue
            elif d.check(word):
                out += " " + word
            else:
                out += " " + word + "----"
                print(word, "is not a word")

        print(out)

        with open(output_path, 'w') as output_file:
            output_file.write(out)


count = 0
def filter_stuff(line):
    global count

    if ('0' in line or 'o' in line) and ('THE' in line or 'NGER' in line):
        print(line)
        count += 1
        return False

    if re.match('\d', line):
        print(line)
        count += 1
        return False

    if len(line) < 10:
        print(line)
        count += 1
        return False

    return True


def fix_stuff():
    with open(input_path, 'r') as input_file:

        lines = input_file.readlines()

        out = ''.join(filter(filter_stuff, lines))
        #print(out)

        with open(output_path, 'w') as output_file:
            output_file.write(out)


def check_stuff():
    with open(input_path, 'r') as input_file:
        lines = input_file.read().replace('\n', ' ').replace('  ', ' ').replace('*\n', '').replace('.', '.').split('.')

        for line in lines:
            if len(line.split()) > 40:
                print(line)
                print('\n\n\n')

        '''
        words = re.sub("[^a-zA-Z' ]", '', line).split(' ')

        for word in words:
            word.strip()
            if word and not (ord(word[0]) >= 65 and ord(word[0]) <= 90) and not d.check(word):
                print(word + " - " + line)
        '''


check_stuff()

