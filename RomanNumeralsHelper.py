ROM = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
       'IV': 4, 'I': 1}


class RomanNumerals:
    @staticmethod
    def to_roman(val):
        s = ''
        for key, value in ROM.items():
            while val % value != val:
                val = val - value
                s += key
        return s

    @staticmethod
    def from_roman(roman_num):
        sum = 0
        for key, value in ROM.items():
            while roman_num.startswith(key):
                roman_num = roman_num[len(key):]
                sum += value
        return sum


print(RomanNumerals.to_roman(2000))
print(RomanNumerals.from_roman('MMCM'))