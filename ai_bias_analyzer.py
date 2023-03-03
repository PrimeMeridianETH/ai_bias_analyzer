# Install dependencies

# Import dependencies
import openai
import streamlit as st

# Set the OpenAI secret key
openai.api_key = st.secrets['pass']

st.header('AI Bias Analyzer')
st.subheader('current version : beta 0.1')

# Set the if, else loop including prompt
article_text = st.text_area('Please enter the text material or URL you would like to extract (potential) bias from')
if len(article_text) > 5:
    temp = st.slider("temperature", 0.4, 0.6, 0.8)
    if st.button ('Generate Report'):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "you are tasked with determining any bias from supplied information on a set of gradient scales between 1 to 10 (where 5 equals no bias, and between 1 and 10 are contrasting bias orientations) using these criteria where applicable: Personal Bias, Racial bias, Gender bias, Sexual Oreintation bias, Socioeconomic bias, Religious bias, Cultural bias, Political bias, Geopolitical bias, Profit Interest(s). Provide slight detail and each metric used per bias analysis section (such as 1 equals racially motivated, whereas 10 equals racially progressive). Use only the text information located here: " + article_text,
            max_tokens = 2000,
            temperature = temp
        )
        res = response["choices"][0]["text"]
        st.info(res)

        st.download_button("Download result", res)
else: st.warning("The supplied information is not large enough")
