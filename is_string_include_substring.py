from random import choice, randint

base_string = 'abcd'

string = [choice(base_string) for i in range(10000)]
string = ''.join(string)

offset = randint(5, 20)
start_slice = randint(0, int(len(string) / 10 ))

substring = string[start_slice:start_slice + offset]
print(f'Substring is: {substring}')

total_matches = 0

for char_index in range(len(string) - len(substring)):
    if string[char_index] == substring[0]:
        if string[char_index:(char_index+len(substring))] == substring:
            print(string[char_index:(char_index+len(substring))])
            print('Match\n')
            total_matches += 1

print(f'Total matches: {total_matches}')
