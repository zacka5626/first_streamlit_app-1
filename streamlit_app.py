import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Ranfe Eggs')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
Fruits_selected = streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
Fruits_to_show = my_fruit_list.loc[Fruits_selected]
streamlit.dataframe(Fruits_to_show)
