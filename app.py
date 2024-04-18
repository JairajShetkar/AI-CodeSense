from openai import OpenAI
import streamlit as st

f = open("keys/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

############################
st.snow()
st.header("🤖AI CodeSense: Your Python Code Companion")
st.subheader("Empower Your Code with AI-Powered Reviews and Fixes!✅")
############################

prompt = st.text_area("Enter your code to review...")

if st.button("Generate") == True:    
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": """You are an experienced and expert python trainer. 
                                            
                                           Given a python code, analyse the correctness of the code and generate responses.
                                           If the code is correct then display a response with message saying: Hey congrats you have entered a working code. No errors found.
                                           If there is an error then display: Sorry you have entered a wrong code. 
                                           And suggest the possible corrections that can fix the error of the code.
                                           Make sure the generated messages look well organised and structured.
                                            """},
            {"role": "user", "content": prompt}
          ]
    )

    #print the response on the webapp!
    st.write(response.choices[0].message.content)

