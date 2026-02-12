import pytest
from string_utils import StringUtils

stringutils = StringUtils

# Список проверок:
# Позитив:
# fff
# ппп
# FFFF ППП
# п-п

# Негатив:
# "   "
# ""
# "!№;%:?*()-=_+<>?,./[]\{}|#$^&"
# "123"

@pytest.mark.positive
@pytest.mark.parametrize(
    'text, result', 
    [
        ("pony", "Pony"), 
        ("пони", "Пони"),
        ("PONY ПОНИ", "PONY ПОНИ"), 
        ("по-ни", "По-ни")
        ]
    )
def test_capitalize_positive(text, result):
    res = stringutils.capitalize(str, text)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize(
    'text, result', 
    [
        ("",""),
        ("   ", "   "),
        ("!№;%:?*()-=_+<>?,./[]\{}|#$^&", "!№;%:?*()-=_+<>?,./[]\{}|#$^&"),
        ("123", "123")
    ]
)
def test_capitalize_negative(text, result):
    res = stringutils.capitalize(str, text)
    assert res == result

@pytest.mark.positive
@pytest.mark.parametrize(
    'text, result', 
    [
        ("   sun", "sun"),
        ("sun", "sun")
    ]
)
def test_trim_positive(text, result):
    res = StringUtils.trim(str, text)
    assert res == result
    
@pytest.mark.negative
@pytest.mark.parametrize(
    'text, result', 
    [
        ("   ", ""),
        ("", "")
    ]
)
def test_trim_negative(text, result):
    res = StringUtils.trim(str, text)
    assert res == result

# Список проверок:
# Позитив:
# Vhhj - V
# VVV - v
# . - .
# " " - " "
# "ggh-ghj" - "ggh-ghj"
# Fgh - Fgh
# 123 - 123
# "" - ""
# Негатив:
# DFG - d
# Fggh - G
# "" - ""
# F - FF

@pytest.mark.positive
@pytest.mark.parametrize(
    'text, symb, result',
    [
        ("Miro", "M", True),
        ("MMM", "M", True),
        ("Miro.", ".", True),
        (" ", " ", True),
        ("Народно-бытовой", "-", True),
        ("Miro", "Miro", True),
        ("123", "123", True),
        ("", "", True)
    ]
)
def test_contains_positive(text, symb, result):
    res = StringUtils.contains(str, text, symb)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize(
    'text, symb, result',
    [
        ("Miro", "m", False),
        ("Miro", "I", False),
        ("M", "MM", False)
    ]
)
def test_contains_negative(text, symb, result):
    res = StringUtils.contains(str, text, symb)
    assert res == result

@pytest.mark.positive
@pytest.mark.parametrize(
    'text, symb, result',
    [
        ("Четвертое задание", " задание", "Четвертое"),
        ("Четвертое задание", " ", "Четвертоезадание"),
        ("Четвертое задание", "Четвертое задание", ""),
        ("Четвертое-задание", "-", "Четвертоезадание"),
        ("Четвертое задание", "е", "Чтврто задани"),
        ("123", "12", "3"),
        ("...", ".", "")
    ]
)
def test_delete_symbol_positive(text, symb, result):
    res = StringUtils.delete_symbol(str, text, symb)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize(
    'text, symb, result',
    [
        ("Четвертое задание", "задание задание", "Четвертое задание"),
        ("Четвертое задание", "", "Четвертое задание")
    ]
)
def test_delete_symbol_negative(text, symb, result):
    res = StringUtils.delete_symbol(str, text, symb)
    assert res == result