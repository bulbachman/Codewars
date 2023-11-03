def parse_int(string):
    word_to_number = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
        'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100,
        'thousand': 1000, 'million': 1000000
    }

    words = string.split()
    total = 0
    current_number = 0

    for word in words:
        if word == 'and':
            continue
        if word in word_to_number:
            if word == 'hundred':
                current_number *= word_to_number[word]
            elif word == 'thousand':
                current_number *= word_to_number[word]
                total += current_number
                current_number = 0
            elif word == 'million':
                current_number *= word_to_number[word]
                total += current_number
                current_number = 0
            else:
                current_number += word_to_number[word]
        else:
            # Handle cases like "twenty-three" or "ninety-nine"
            if '-' in word:
                parts = word.split('-')
                for part in parts:
                    current_number += word_to_number[part]
            else:
                total += current_number
                current_number = 0

    total += current_number
    return total


print(parse_int('two thousand'))
