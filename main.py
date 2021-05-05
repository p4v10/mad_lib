# Imports
import streamlit as st
from PIL import Image
import pandas as pd

# Page expands to full width
st.set_page_config(layout="wide")

# Logo
image = Image.open('img/img.png')
st.image(image, width = 300)
# TITLE
st.title('MAD LIB APPLICATION')

st.write("""
#### You can find this project on GitHub.
[[Project](https://github.com/p4v10)]
[[Original MAD LIB](http://www.redkid.net/cgi-bin/madlibs/videogames.pl)]
"""

st.markdown("""
This app is a simple MAD Lib.
Provide some information and read a fun story!
""")

# Sidebar header
st.sidebar.header("Please provide your data")

# User imputs function
def user_input_features():
    adjective_one = st.sidebar.text_input(label='Adjective #1', value='Adjective')
    adjective_two = st.sidebar.text_input(label='Adjective #2', value='Adjective')
    adjective_three = st.sidebar.text_input(label='Adjective #3', value='Adjective')
    adjective_four = st.sidebar.text_input(label='Adjective #4', value='Adjective')
    noun_one = st.sidebar.text_input(label='Noun #1', value='Noun')
    noun_two = st.sidebar.text_input(label='Noun #2', value='Noun')
    noun_three = st.sidebar.text_input(label='Noun #3', value='Noun')
    noun_four = st.sidebar.text_input(label='Noun #4', value='Noun')
    number = st.sidebar.number_input('Number', 1,100,17)
    body_part_one = st.sidebar.selectbox('Select the part of Body #1',('Head','Neck','Arm','Shoulder','Leg','Wrist'))
    body_part_two = st.sidebar.selectbox('Select the part of Body #2',('Head','Neck','Arm','Shoulder','Leg','Wrist'))
    plural_noun_one = st.sidebar.text_input(label='Plural Noun #1', value="Plural Noun")
    plural_noun_two = st.sidebar.text_input(label='Plural Noun #2', value="Plural Noun")
    plural_noun_three = st.sidebar.text_input(label='Plural Noun #3', value="Plural Noun")
    plural_noun_four = st.sidebar.text_input(label='Plural Noun #4', value="Plural Noun")
    verb = st.sidebar.text_input(label='Verb', value='Verb')
    verb_ing = st.sidebar.text_input(label='Verb Ending in ING', value='fishing')
    # Last 3 digits of verb_ing variable
    last_char = verb_ing[-3:]
    # IF statement to check if the verb ends in ING
    if last_char == 'ing' or last_char == 'ING':
        st.sidebar.write('Right ending')
    else:
        st.sidebar.write('The verb is not ending in ING')
    # Creating dictionary for a DataFrame
    data = {'adjective_one': adjective_one,
            'adjective_two': adjective_two,
            'adjective_three': adjective_three,
            'adjective_four': adjective_four,
            'noun_one': noun_one,
            'noun_two': noun_two,
            'noun_three': noun_three,
            'noun_four': noun_four,
            'number': number,
            'body_part_one': body_part_one,
            'body_part_two': body_part_two,
            'plural_noun_one': plural_noun_one,
            'plural_noun_two': plural_noun_two,
            'plural_noun_three': plural_noun_three,
            'plural_noun_four': plural_noun_four,
            'verb': verb,
            'verb_ing': verb_ing}
    # Creating a DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Assigning a DataFrame to variable
df = user_input_features()

# Creating a button to submit & show inputs
if st.sidebar.button('Submit'):
    st.write('This is the information that you have provided, please check if everything is correct!')
    st.write(df)
# Convert DataFrame to ndArray
new_df = df.to_numpy()

# Story
story = ('I love to ' + new_df[0][15] + " video games. I can play them day and   \n"  + new_df[0][12] + '! My mom and ' + new_df[0][5] + ' are not too happy with my  \n' + new_df[0][16] + 'so much time in front of the television ' + new_df[0][13] + '.  \n' + 'Although Dad believes that these ' + new_df[0][0] + ' games help children   \n develop hand-' + new_df[0][9] + ' coordination and improve their  \n learning ' + new_df[0][11] + ', he also seems to think they have ' + str(new_df[0][1]) + "  \n  side effects on one's " + new_df[0][10] + '. Both of my ' + new_df[0][4] + '  \n think this is due to an ' + new_df[0][2] + ' use of violance in the majority  \n of the ' + new_df[0][13] + '. Finally, we all arrived at a ' + new_df[0][3] + '  \n compromise: After dinner I can play ' + new_df[0][14] + ' hours of video games,  \n provided I help clear the ' + new_df[0][7] + ' and wash the ' + new_df[0][14] + '.')

# IF statement to show the story
if st.button('Show the Story'):
    st.write(story)
