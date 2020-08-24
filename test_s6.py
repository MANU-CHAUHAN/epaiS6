import pytest
import s6
import os
import inspect
import re
import itertools

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

CHECK_FOR_FUNCT_IMPL = [
    'vals',
    'create_deck_cards_normal_function',
    'create_deck_cards_using_lambda',
    'suits'
]

cards_combination = list(itertools.product(vals, suits))

README_CONTENT_CHECK_FOR = [
    'vals',
    'create_deck_cards_normal_function',
    'create_deck_cards_using_lambda',
    'suits'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD is True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "Readme is not formatted properly"


# --------------------------------------------------------------------------------------
# Tests related Contents in session 4 file

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(s6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(s6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_all_functions_implemented():
    code_lines = inspect.getsource(s6)
    FUNCS_IMPL = True
    for c in CHECK_FOR_FUNCT_IMPL:
        if c not in code_lines:
            print(c)
            FUNCS_IMPL = False
            pass
    assert FUNCS_IMPL is True, 'You forgot to implement all functions! Try again!'


def test_create_deck_cards_single_expression_docstring():
    docstring = s6.create_deck_cards_using_lambda().__doc__
    assert docstring, "Beware, You have not written docstring for a function!"


def test_create_deck_cards_single_expression_docstring_content():
    docstring = s6.create_deck_cards_using_lambda().__doc__
    assert len(docstring) > 50, "Beware, You have not written proper docstring for a function!"


def test_create_deck_cards_single_expression_total_cards():
    result = s6.create_deck_cards_using_lambda()
    assert len(result) == 52, "There should be total of 52 cards"


def test_create_deck_cards_single_expression_compare_cards():
    result = s6.create_deck_cards_using_lambda()
    for card in cards_combination:
        if card not in result:
            assert False, "Not all the combinations of cards present"


def test_create_deck_cards_normal_function_docstring():
    docstring = s6.create_deck_cards_normal_function.__doc__
    assert docstring, "Beware, You have not written docstring for a function!"


def test_create_deck_cards_normal_function_docstring_content():
    docstring = s6.create_deck_cards_normal_function.__doc__
    assert len(docstring) > 50, "Beware, You have not written proper docstring for a function!"


def test_play_royal_flush():
    Card1 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Royal Flush"


def test_play_straight_flush():
    Card1 = [('ace', 'clubs'), ('king', 'clubs'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    Card2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Straight Flush"


def test_play_4_Of_A_Kind():
    Card1 = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('2', 'spades'), ('2', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Four Of A Kind"


def test_play_full_house():
    Card1 = [('2', 'spades'), ('3', 'clubs'), ('7', 'hearts'), ('8', 'diamonds'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('2', 'spades'), ('2', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Full House"


def test_play_flush():
    Card1 = [('2', 'spades'), ('3', 'spades'), ('7', 'spades'), ('8', 'spades'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('4', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('2', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Flush"


def test_play_Straight():
    Card1 = [('2', 'spades'), ('3', 'hearts'), ('7', 'diamonds'), ('8', 'hearts'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('4', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a Straight"


def test_play_3_Of_A_Kind():
    Card1 = [('2', 'spades'), ('2', 'hearts'), ('2', 'diamonds'), ('8', 'hearts'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Three Of A Kind"


def test_play_2_Pair():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('2', 'diamonds'), ('8', 'hearts'), ('4', 'spades')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a Two Pair"


def test_play_1_Pair():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('2', 'diamonds'), ('8', 'hearts'), ('7', 'spades')]
    Card2 = [('3', 'clubs'), ('8', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 1 won! He has a One Pair"


def test_play_high_card():
    Card1 = [('2', 'spades'), ('4', 'hearts'), ('3', 'diamonds'), ('8', 'hearts'), ('7', 'spades')]
    Card2 = [('3', 'clubs'), ('10', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('7', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert result == "Player 2 won! He has a High Card"


def test_create_deck_cards_normal_function_total_cards():
    result = s6.create_deck_cards_normal_function()
    assert len(result) == 52, "There should be total of 52 cards"


def test_create_deck_cards_normal_function_compare_cards():
    result = s6.create_deck_cards_normal_function()
    for card in cards_combination:
        if card not in result:
            assert False, "Not all the combinations of cards present"


def test_play_poker_game():
    Card1 = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades')]
    Card2 = [('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('2', 'spades'), ('2', 'clubs')]
    result = s6.play_poker_game(Card1, Card2)
    assert "Player 1 won" in result
