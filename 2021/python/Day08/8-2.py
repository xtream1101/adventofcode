import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        signals = f.read().splitlines()
    return signals


def contains_all_letters(substr, digit):
    for letter in substr:
        if letter not in digit:
            return False
    return True


def run(signals):
    '''
    * known because unique
    - solved for
    -0 has 6 seg and is in 8
    *1 has 2 seg and is in 0,3,4,7,8,9
    -2 has 5 seg and is in 8
    -3 has 5 seg and is in 8,9
    *4 has 4 seg and is in 8,9
    -5 has 5 seg and is in 6,8,9
    -6 has 6 seg and is in 8
    *7 has 3 seg and is in 0,3,8,9
    *8 has 7 seg and is in --
    -9 has 6 seg and is in 8
    '''
    total_output = 0
    for signal in signals:
        unique_code, output_values = signal.split('|')
        unique_code = unique_code.split()
        output_values = output_values.split()
        # Sort to compare later
        for idx, code in enumerate(unique_code.copy()):
            unique_code[idx] = ''.join(sorted(code))
        for idx, code in enumerate(output_values.copy()):
            output_values[idx] = ''.join(sorted(code))

        mapped_unique = ['']*10

        # first pass
        for idx, digit in enumerate(unique_code):
            match len(digit):
                case 2:
                    mapped_unique[idx] = '1'
                case 4:
                    mapped_unique[idx] = '4'
                case 3:
                    mapped_unique[idx] = '7'
                case 7:
                    mapped_unique[idx] = '8'

        # Next passes:
        while '' in mapped_unique:
            for idx, digit in enumerate(unique_code):
                if mapped_unique[idx] != '':
                    # already a known number
                    continue

                if len(digit) == 6:
                    if contains_all_letters(unique_code[mapped_unique.index('4')], digit):
                        # and if 4 is a substr then must be 9
                        mapped_unique[idx] = '9'
                    elif contains_all_letters(unique_code[mapped_unique.index('1')], digit):
                        # if 1 is a substr and 4 is already set by the first if
                        mapped_unique[idx] = '0'
                    else:
                        # only option is 6
                        mapped_unique[idx] = '6'

                elif len(digit) == 5:
                    if '9' in mapped_unique:
                        # check if 2, can go into 8, but not 9
                        in8 = contains_all_letters(digit, unique_code[mapped_unique.index('8')])
                        in9 = contains_all_letters(digit, unique_code[mapped_unique.index('9')])
                        if in8 and not in9:
                            mapped_unique[idx] = '2'
                        else:
                            if '6' in mapped_unique:
                                in6 = contains_all_letters(digit, unique_code[mapped_unique.index('6')])
                                if in6 and in8 and in9:
                                    mapped_unique[idx] = '5'
                                else:
                                    mapped_unique[idx] = '3'
            # print(mapped_unique)

            # Step through to debug
            # if input('...').strip() == 'q':
            #     break

        # Now decode the output
        decoded_output = ''
        for code in output_values:
            decoded_output += mapped_unique[unique_code.index(code)]

        total_output += int(decoded_output)

    return total_output


test_ans = run(['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'])
# print(test_ans)
assert test_ans == 5353

test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 61229

ans = run(load_input('input.txt'))
assert ans == 986163
print(ans)
