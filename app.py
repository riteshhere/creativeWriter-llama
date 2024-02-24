import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import streamlit as st


## Function to get response from LLAMA 2 Model
def getLlamaResponse(input_text, no_words, blog_style):
    llm = CTransformers(model = 'models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})
    
    ## PromptTemplate
    template = """Write a  {blog_style} on {input_text} in less than {no_words} words"""

    prompt = PromptTemplate(input_variables = ["input_text", "no_words", "blog_style"],
                            template = template)
    
    ## Generate the reponse from the LLama 2 Model
    respone = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(respone)
    return respone



st.set_page_config(page_title = "Generate Blog",
                    layout='centered',
                    initial_sidebar_state = "collapsed")

st.header("Creative Writer✍️")

input_text = st.text_input("Enter the topic you want to write about")

col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of words')
with col2:
    blog_style = st.selectbox("Category",
                              ('Essays', 'Poem', 'Joke', 'Blog'),
                              index=0)
    
submit = st.button("Generate")

if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))
