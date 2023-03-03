# Install dependencies

# Import dependencies
import openai
import streamlit as st

# Set the OpenAI secret key
openai.api_key = st.secrets['pass']

st.header('AI Bias Analyzer')
st.subheader('Current Version: Beta 0.1')

# Set the if, else loop including prompt
article_text = st.text_area('Please enter the text material or URL you would like to extract (potential) bias from')
if len(article_text) > 5:
    temp = st.slider("Temperature", 0.4, 0.6, 0.8)
    if st.button ('Generate Report'):
        prompt = f"Please determine any bias from the following supplied information on a set of gradient scales between 1 to 10 (where 5 equals no bias, and between 1 and 10 are contrasting bias orientations) using these criteria where applicable:\n\n1. Personal bias (1 = negative bias, 5 = neutral, and 10 = positive bias)\n2. Racial bias (detail what race(s) are being referred to, 1 = heavily racially charged, 5 = neutral, 10 = racially progressive)\n3. Gender bias (detail what gender(s) are being referred to, 1 = biased against women, 5 = neutral, 10 = biased against men)\n4. Transgender bias (1 = biased against transgender, 5 = no bias, 10 = supportive of transgender)\n5. Sexual Orientation bias (1 = biased against freedom of orientation, 5 = neutral, 10 = progressive towards freedom of orientation)\n6. Socio-Economic bias (1 = bias towards the lower class, 5 = neutral, 10 = bias towards the upper class)\n7. Religious bias (detail what religion is being referred to, 1 = negative, 5 = neutral, 10 = positive)\n8. Cultural bias (detail what cultural groups are being referred to, 1 = culturally insensitive, 5 = neutral, 10 = culturally supportive)\n9. Political bias (1 = conservative viewpoint, 5 = centrist/neutral, 10 = progressive)\n10. Geopolitical bias (detail what nations are being referred to, 1 = anti-nato, 5 = neutral, 10 = pro-nato)\n11. Profit Interest(s) (detail what companies or industries are being referred to, 1 = negatively impacted, 5 = neutral/no impact, 10 = positively impacted)\n\n For each bias analysis section, please provide slight detail and each metric used per bias analysis section as well ranking criteria used. Use only the text information located here: {article_text}"
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = prompt,
            max_tokens = 2000,
            temperature = temp
        )
        res = response["choices"][0]["text"]
        st.info(res)

        st.download_button("Download Result", res)
else: st.warning("The supplied information is not large enough")
