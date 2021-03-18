"""Test Functions for school planner chatbot."""

from functions import *

def test_remove_punctuation():
    """Tests for the `remove punctuation` function."""
    
    # Check string with punctuation
    assert string.punctuation not in remove_punctuation('8:00')
    
    # Check string without punctuation
    assert remove_punctuation('MATH18') == 'MATH18'
    
def test_prepare_text():
    """Tests for the `prepare_text` function."""
    
    # Check that output is list
    assert isinstance(prepare_text('COGS18, DSGN1, COGS9'), list)
    
    # Check for lowercase letters
    assert prepare_text('Monday') == ['monday']
    
    # Check for punctuation
    assert string.punctuation not in prepare_text('3:00')

    
def test_end_chat():
    """Tests for the `end_chat` function."""
    
    # Check for input with 'quit'
    assert end_chat(['quit']) == True
    
    # Check for input without 'quit'
    assert end_chat(['monday', 'wednesday']) == False
    
def test_greeting():
    """Tests for the `greeting` function."""
    
    # Check that output is string
    assert isinstance(greeting(['tracey']), str)
    
    # Check for capitalization in first name
    assert greeting(['tracey'])[6].isupper() 
    
def test_get_days():
    """Tests for the `get_days` function."""
    
    # Check that function can be called
    assert callable(get_days)
    
    assert get_days('dsgn1') == 'On what days do you have DSGN1?' + \
                            ' (ex: Monday, Wednesday)'
    
def test_get_time():
    """Tests for the `get_time` function."""
    
    # Check that function can be called
    assert callable(get_time)
    
    assert get_time('cogs18') == 'What time do you have COGS18?' + \
                             ' (in military time, ex: 1:00 pm is 13:00)'
    
def test_make_day_df():
    """Tests for the `make_day_df` function."""
    
    # Check that output is list
    assert isinstance(make_day_df(['monday', 'tuesday'], 'COGS18'), list)
    
    # Check length of list
    assert len(make_day_df(['monday', 'tuesday'], 'COGS18')) == 5

def test_make_dict():
    """Tests for the `make_dict` function."""
    
    # Check that output is dictionary
    assert isinstance(make_dict('300', 'COGS9'), dict)
    
    assert make_dict('300', 'COGS9') == {'COGS9': 300}
    
def test_make_time_df():
    """Tests for the `make_time_df` function."""
   
    # Check that output is list
    assert isinstance(make_time_df({'dsgn1': 930}, [pd.DataFrame({'Monday': ['dsgn1']}),
                                                    pd.DataFrame(), pd.DataFrame(), pd.DataFrame(),
                                                    pd.DataFrame(), pd.DataFrame()]), list)
    
    # Check length of list
    assert len(make_time_df({'dsgn1': 930}, [pd.DataFrame({'Monday': ['dsgn1']}), pd.DataFrame(),
                                             pd.DataFrame(), pd.DataFrame(), pd.DataFrame(),
                                             pd.DataFrame()])) == 5
    
def test_combine_col():
    """Tests for the `combine_col` function."""
    
    # Check that output is dataframe
    assert isinstance(combine_col([pd.DataFrame({'Monday': []}),
                                   pd.DataFrame({'Tuesday': []})]), pd.DataFrame)
    
    # Check that function can be called
    assert callable(combine_col)
    
def test_make_sorting_col():
    """Tests for the `make_sorting_col` function."""
    
    # Check that output is list
    assert isinstance(make_sorting_col([pd.DataFrame({'Monday': ['dsgn1']})],
                                       [pd.DataFrame({'Time1': [930]})]), list)
    
    # Check that function can be called
    assert callable(make_sorting_col)

    
def test_sort_col():
    """Tests for the `sort_col` function."""
    
    # Check that output is list
    assert isinstance(sort_col([pd.DataFrame({'Monday': ['dsgn1'],
                                              'Time1': [930]})]), list)
    
    # Check that function can be called
    assert callable(sort_col)
    
def test_start_chat():
    """Tests for the `start_chat` function."""
    
    # Check that funcation can be called
    assert callable(start_chat)
    