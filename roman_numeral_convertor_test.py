import pytest
from hypothesis import given, strategies as st
from roman_numeral_converter import RomanNumeralConverter

test_cases = (
    (1, "I"), (2, "II"), (3, "III"), (4, "IV"), (5, "V"), (6, "VI"), (7, "VII"), (8, "VIII"),
    (9, "IX"), (10, "X"), (11, "XI"), (12, "XII"), (13, "XIII"), (14, "XIV"), (15, "XV"), (16, "XVI"), (19, "XIX"),
    (20, "XX"), (21, "XXI"), (24, "XXIV"), (29, "XXIX"), (30, "XXX"), (38, "XXXVIII"), (39, "XXXIX"),
    (40, "XL"), (41, "XLI"), (44, "XLIV"), (49, "XLIX"), (50, "L"), (55, "LV"), (59, "LIX"),
    (65, "LXV"), (70, "LXX"), (77, "LXXVII"), (89, "LXXXIX"),
    (98, "XCVIII"), (99, "XCIX"), (100, "C"), (138, "CXXXVIII"), (144, "CXLIV"), (149, "CXLIX"), (150, "CL"),
    (232, "CCXXXII"), (499, "CDXCIX"), (516, "DXVI"), (1549, "MDXLIX"), (1899, "MDCCCXCIX"), (2222, "MMCCXXII"),
    (3457, "MMMCDLVII"), (3999, "MMMCMXCIX")
    )


@pytest.mark.parametrize(
    "value", (-1, 0, 4000, 4150)
)
def test_int_to_roman_invalid(value):
    with pytest.raises(ValueError) as e:
        RomanNumeralConverter.int_to_roman(value)
    assert str(e.value.args[0]) == "Value out of range [1, 3999]"


@pytest.mark.parametrize("arab, roman", test_cases)
def test_int_to_roman(arab, roman):
    computed = RomanNumeralConverter.int_to_roman(arab)
    assert computed == roman


@pytest.mark.parametrize(
    "roman", ("", "foo", "XXXX", "XVi")
)
def test_roman_to_int_invalid(roman):
    with pytest.raises(ValueError) as e:
        RomanNumeralConverter.roman_to_int(roman)
    assert str(e.value.args[0]) == "Invalid roman number"


@pytest.mark.parametrize("arab, roman", test_cases)
def test_roman_to_int(arab, roman):
    computed = RomanNumeralConverter.roman_to_int(roman)
    assert computed == arab


@given(st.integers(min_value=1, max_value=3999))
def test_random(arab):
    """ Random integer to check bijection """
    roman = RomanNumeralConverter.int_to_roman(arab)
    computed = RomanNumeralConverter.roman_to_int(roman)
    assert computed == arab
