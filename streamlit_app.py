

import streamlit
streamlit.title ('My Mom s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Bolied Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#NewSection  to display frutyvice api response

streamlit.header('Frutyvice Fruit Advice!')
fruit_choice = streamlit.text_input('what fruit would you like information about?','Apple')
streamlit.write('The user entered',fruit_choice)


import requests
frutyvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)






