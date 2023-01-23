
class RomanNumeralConverter:
    """ Integer <-> Roman number convertor """
    letters = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    possible_sub = {1000: "C", 500: "C", 100: "X", 50: "X", 10: "I", 5: "I"}

    @classmethod
    def int_to_roman(cls, value: int):
        """
        Convert integer to roman number
        raise ValueError if impossible
        """
        if value <= 0 or value > 3999:
            raise ValueError("Value out of range [1, 3999]", value)

        result = ""
        for letter, letter_value in cls.letters.items():
            # Additive case, 3 times same letter max
            for nb_letter in (3, 2, 1):
                if value >= letter_value * nb_letter:
                    result += letter * nb_letter
                    value -= letter_value * nb_letter
            # Subtractive case, max one letter to subtract
            sub_letter = cls.possible_sub.get(letter_value)
            if sub_letter:
                sub_value = cls.letters[sub_letter]
                if value >= letter_value - sub_value:
                    result += sub_letter + letter
                    value -= letter_value - sub_value
            # Stop when done
            if value == 0:
                break
        assert value == 0, f"Remaining value {value} at end of conversion"

        return result

    @classmethod
    def roman_to_int(cls, roman: str):
        """
        Convert roman number to integer
        raise ValueError if invalid
        """
        if not roman:
            raise ValueError("Invalid roman number", roman)

        result = 0
        previous_letter_value = 0
        previous_letter = ""
        nb_same_letters = 0
        for letter in roman:
            # Check same letter does not appear 4 times or more (faster than regexp)
            if previous_letter == letter:
                if nb_same_letters >= 3:
                    raise ValueError("Invalid roman number", roman)
                nb_same_letters += 1
            else:
                previous_letter = letter
                nb_same_letters = 1
            # Retrieve letter value and check letter is valid
            try:
                letter_value = cls.letters[letter]
            except KeyError:
                raise ValueError("Invalid roman number", roman)
            if previous_letter_value and letter_value > previous_letter_value:
                # When a letter is greater than previous one, we have a subtraction
                result += letter_value - previous_letter_value
                previous_letter_value = 0
            else:
                # Else we can add it
                result += previous_letter_value
                # And we store new one to check possible subtraction
                previous_letter_value = letter_value
        result += previous_letter_value

        return result
