# Roman to Arab convertor

Small exercise for recruitment.

## Problem statement

Write convertor class which translate Roman to Arab number and the opposite.

Create a class called `RomanNumeralConverter` that has two methods:

    int_to_roman(value: int) -> str: Given an integer, the method should return the Roman numeral representation of this value as a string.
    roman_to_int(roman: str) -> int: Given a Roman numeral string, the method should return the integer representation of s.

The class should handle cases where the input is not valid and should raise an appropriate exception.

You must write appropriate unit tests.

## Roman number

A Roman numeral is built using a combination of letters from the Latin alphabet, specifically: I, V, X, L, C, D, and M. These letters represent the values 1, 5, 10, 50, 100, 500 and 1000 respectively. When constructing a Roman numeral, the basic rule is that the numeral should be read and understood as a sum of each symbol's value.

For example, the Roman numeral "X" represents the value of 10, while "XI" represents the value of 11 (10+1). Similarly, "XX" represents the value of 20 (10+10).

Additionally, Roman numerals use a subtractive notation, where a smaller numeral before a larger numeral means to subtract the smaller numeral from the larger numeral. For example, "IV" represents 4 (5-1), "XC" represents 90 (100-10) and "CM" represents 900 (1000-100).
Subtractive notation is used to prevent to have 4 times the same letter: "IV" instead of "IIII".

It's important to note that Roman numerals do not have a symbol for the number 0, and certain combinations of letters are not allowed, such as "IIII" or "VV"

## Examples

| 1 = I | 2 = II | 3 = III | 4 = IV | 5 = V |
| 6 = VI | 7 = VII | 8 = VIII | 9 = IX | 10 = X | 
| 11 = XI | 12 = XII | 13 = XIII | 14 = XIV | 15 = XV |
| 16 = XVI | 17 = XVII | 18 = XVIII | 19 = XIX | 20 = XX |
| 50 = L | 100 = C | 500 = D | 1000 = M | 3428 = MMMCDXXVIII |
