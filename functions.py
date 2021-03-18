"""Functions for school planner chatbot."""

import string
import pandas as pd

# Introduction message
introduction = 'Hello, I am your school planner chatbot. \n' + \
'It\'s my job to make sure that you know your weekly class schedule! \n' + \
'Type "quit" at any point if you wish to exit. \n' +\
'But first off... what\'s your name?'

# Pandas dataframe containing class schedule
schedule_df = pd.DataFrame()

# Dataframes of classes for each weekday
df1 = pd.DataFrame(columns = ['Monday'])
df2 = pd.DataFrame(columns = ['Tuesday'])
df3 = pd.DataFrame(columns = ['Wednesday'])
df4 = pd.DataFrame(columns = ['Thursday'])
df5 = pd.DataFrame(columns = ['Friday'])

# List of dataframes of classes for each weekday
list_day_df = []

# Dictionary of classtimes corresponding to each class
class_time_dict = {}

# Dataframes of classtimes for each weekday
time_df1 = pd.DataFrame(columns = ['Time1'])
time_df2 = pd.DataFrame(columns = ['Time2'])
time_df3 = pd.DataFrame(columns = ['Time3'])
time_df4 = pd.DataFrame(columns = ['Time4'])
time_df5 = pd.DataFrame(columns = ['Time5'])

# List of dataframes of classtimes for each weekday
list_time_df = []

# List of dataframes of classes and classtimes for each weekday
list_combined_df = []

# List of ordered dataframes of classes and classtimes for each weekday
list_sorted_df = []

def remove_punctuation(input_string):
    """Removes punctuation from user input.
       Function taken from A3.
    
    Parameters
    ----------
    input_string : string
        User input.
    
    Return
    ------
    out_string : string
        User input after punctuation is removed.
    """    
    
    out_string = ''
    
    # Removes punctuation from string
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
    
    return out_string

def prepare_text(input_string):
    """Converts user input into a list of strings for easy processing.
       Function taken from A3.
      
    Parameters
    ----------
    input_string : string
        User input.
    
    Return
    ------
    out_list : list of strings
        User input, lowercase and no punctuation, in the form of a list.
    """    
    
    # Changes string into lowercase letters
    temp_string = input_string.lower()
    
    # Removes punctuation from string
    temp_string = remove_punctuation(temp_string)
    
    # Splits string into list
    out_list = temp_string.split()
    
    return out_list

def end_chat(input_list):
    """Ends chat when user types quit.
       Function taken from A3.
    
    Parameters
    ----------
    input_list : list
        User input.
    
    Return
    ------
    output : boolean
        Returns True when user input contains 'quit'.
    """    
    
    if 'quit' in input_list:
        output = True
    else:
        output = False
    
    return output

def greeting(msg):
    """Greeting to get user's name and ask about user's current classes.
    
    Parameters
    ----------
    msg : list
        User input.
    
    Return
    ------
    out_msg : string
        Greeting message.
    """    
    
    # Capitalizes first name
    name = msg[0].capitalize()
   
    out_msg = 'Hello ' + name + '! What classes are you taking this quarter?' + \
              ' (ex: COGS18, DSGN1)'
    
    return out_msg

def get_days(item):
    """Asks about what days the user has classes.
    
    Parameters
    ----------
    item : string
        User's class based on user input.
        
    Return
    ------
    question : string
        Question asking about the days of user's classes.
    """    
    
    # Changes string into uppercase letters
    item = item.upper()
    
    question = 'On what days do you have ' + item + '? (ex: Monday, Wednesday)'
        
    return question

def get_time(item):
    """Asks about what time the user has classes.
    
    Parameters
    ----------
    item : string
        User's class based on user input.
        
    Return
    ------
    question : string
        Question asking about the time of user's classes.
    """
    
    # Changes string into uppercase letters
    item = item.upper()
   
    question = 'What time do you have ' + item + '?' + \
               ' (in military time, ex: 1:00 pm is 13:00)'
    
    return question

def make_day_df(msg_day, class_name):
    """Makes dataframes of user's classes for each weekday.
    
    Parameters
    ----------
    msg_day : list
        List of days that user has a class based on user input.
        
    class_name: string
        Name of user's class.
        
    Return
    ------
    list_day_df : list
        List of dataframes containing user's classes for each weekday.
    """    
    
    global df1
    global df2
    global df3
    global df4
    global df5
    global list_day_df
    
    # Changes string into uppercase letters
    class_name = class_name.upper()
    
    # Appends class to dataframe of weekday if user has class on that day
    for day in msg_day:
        if day == 'monday':
            df1 = df1.append({'Monday': class_name}, ignore_index=True)
        elif day == 'tuesday':
            df2 = df2.append({'Tuesday': class_name}, ignore_index=True)
        elif day == 'wednesday':
            df3 = df3.append({'Wednesday': class_name}, ignore_index=True)
        elif day == 'thursday':
            df4 = df4.append({'Thursday': class_name}, ignore_index=True)
        elif day == 'friday':
            df5 = df5.append({'Friday': class_name}, ignore_index=True)
    
    list_day_df = [df1, df2, df3, df4, df5]
    
    return list_day_df

def make_dict(msg_time, class_name):
    """Makes dictionary of user's classes and corresponding classtimes.
    
    Parameters
    ----------
    msg_time : string
        Classtime of user's class based on user input.
        
    class_name: string
        Name of user's class.
        
    Return
    ------
    class_time_dict : dictionary
        Dictionary of user's classes and corresponding classtimes.
    """    
    
    global class_time_dict
    
    # Adds class and corresponding classtime to dictionary
    class_time_dict.update({class_name: int(msg_time)})
    
    return class_time_dict

def make_time_df(class_time_dict, list_day_df):
    """Makes dataframes of user's classtimes for each weekday.
    
    Parameters
    ----------
    class_time_dict : dictionary
        Dictionary of user's classes and corresponding classtimes.
        
    list_day_df: list
        List of dataframes containing user's classes for each weekday.
        
    Return
    ------
    list_time_df : list
        List of dataframes containing user's classtimes for each weekday.
    """    
    
    global time_df1
    global time_df2
    global time_df3
    global time_df4
    global time_df5
    global list_time_df
    
    # Appends classtime to dataframe of weekday if user has class on that day
    if not list_day_df[0].empty:
        for item in list(list_day_df[0].iloc[:, 0]):
            item = item.lower()
            if item in class_time_dict.keys():
                time_df1 = time_df1.append({'Time1': class_time_dict[item]},
                                           ignore_index=True)
    
    if not list_day_df[1].empty:
        for item in list(list_day_df[1].iloc[:, 0]):
            item = item.lower()
            if item in class_time_dict.keys():
                time_df2 = time_df2.append({'Time2': class_time_dict[item]},
                                           ignore_index=True)    
    
    if not list_day_df[2].empty:
        for item in list(list_day_df[2].iloc[:, 0]):
            item = item.lower()
            if item in class_time_dict.keys():
                time_df3 = time_df3.append({'Time3': class_time_dict[item]},
                                           ignore_index=True)

    if not list_day_df[3].empty:
        for item in list(list_day_df[3].iloc[:, 0]):
            item = item.lower()
            if item in class_time_dict.keys():
                time_df4 = time_df4.append({'Time4': class_time_dict[item]},
                                           ignore_index=True)

    if not list_day_df[4].empty:
        for item in list(list_day_df[4].iloc[:, 0]):
            item = item.lower()
            if item in class_time_dict.keys():
                time_df5 = time_df5.append({'Time5': class_time_dict[item]},
                                           ignore_index=True)
    
    list_time_df = [time_df1, time_df2, time_df3, time_df4, time_df5]
    
    return list_time_df

def combine_col(list_df):
    """Combines dataframes.
    
    Parameters
    ----------
    list_df: list
        List of dataframes to be combined.
        
    Return
    ------
    combined_df : dataframe
        Dataframe made from combining other dataframes.
    """
    
    combined_df = pd.concat(list_df, ignore_index=False, axis=1)
    
    return combined_df

def make_sorting_col(list_class, list_time):
    """Makes dataframes of classes and their classtimes for each weekday.
    
    Parameters
    ----------
    list_class: list
        List of classes for each weekday.
    
    list_time: list
        List of classtimes for each weekday.
        
    Return
    ------
    list_combined_df : list
        List of dataframes of classes and their classtimes for each weekday.
    """    
    
    global list_combined_df
    
    # Combines class dataframe and classtime dataframe according to weekday
    for class_df, time_df in zip(list_class, list_time):
        combined_df = combine_col([class_df, time_df])
        list_combined_df.append(combined_df)
        
    return list_combined_df
    
def sort_col(list_combined_df):
    """Orders dataframes of classes for each weekday based on classtime.
    
    Parameters
    ----------
    list_combined_df: list
        List of dataframes of classes and their classtimes for each weekday.
       
    Return
    ------
    list_sorted_df : list
        List of ordered dataframes of classes and classtimes for each weekday.
    """    
    
    global list_sorted_df
    
    # Orders dataframe from earliest class to latest class for each weekday
    for combined_df in list_combined_df:
        if not combined_df.empty:
            combined_df.sort_values(by=[combined_df.columns[1],
                                        combined_df.columns[0]], inplace=True)
            
            combined_df = combined_df.reset_index(drop=True)

            list_sorted_df.append(combined_df)
            
    return list_sorted_df

def start_chat():
    """Main function to run chatbot. Roughly based around A3."""
    
    # Introduction message
    print(introduction)
    
    count = 1
        
    chat = True
    while chat:
        
        # Get message from user
        msg = input('Input: ')
        out_msg = None
                
        # Prepare the input message
        msg = prepare_text(msg)
        
        # End chat
        if end_chat(msg):
            chat = False
        
        # Ask questions
        elif count == 1:
            print(greeting(msg))
            
            count += 1
        
        elif count == 2:
            for item in msg:
                global class_name
                class_name = item
                
                print(get_days(item))
                msg_day = input('Input: ')
                msg_day = prepare_text(msg_day)
                
                if 'quit' in msg_day:
                    break

                else:
                    # Make dataframes of classes for each weekday
                    make_day_df(msg_day, class_name)
                    
                    print(get_time(item))
                    msg_time = input('Input: ')
                    msg_time = remove_punctuation(msg_time)
                    
                    if 'quit' in msg_time:
                        break
                    else:
                        # Make dictionary of classes and classtimes
                        make_dict(msg_time, class_name)
                    
            chat = False
    
    if list_day_df:
        
        # Make dataframes of classtimes for each weekday
        make_time_df(class_time_dict, list_day_df)

        # Make dataframes of classes and classtimes for each weekday
        make_sorting_col(list_day_df, list_time_df)

        # Order dataframes based on classtime
        sort_col(list_combined_df)

        global schedule_df

        # Combine dataframes into main dataframe
        schedule_df = combine_col(list_sorted_df)

        # Remove columns with classtimes
        schedule_df.drop([col for col in schedule_df.columns if 'Time' in col],
                                 axis=1, inplace=True)

    return schedule_df
