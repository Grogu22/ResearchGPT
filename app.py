# Importing dependencies
import streamlit as st
import openai

#Function to generate openai response
def generate_response(prompt):
    completions = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=0.7
    )
    message = completions.choices[0].text
    return message

# interface
st.title('🥼🧪ResearchGPT📃')
st.text('Running out of ideas for writing a research paper?😮‍💨')
st.text('Approaching deadline to submit your research paper?⏲️')
st.text('DO NOT WANT to write a research paper?🙃')
st.caption('Say no more... write the domain of your research and choose the sections you want us to write.. your paper will be ready in less than 2 minutes.. 😌')
api_key = st.text_input("Enter your OpenAI API KEY", type="password")
if(api_key):
    #setting api key
    openai.api_key = api_key
    # getting domain of research
    prompt1 = st.text_input("Enter the domain to write a research paper on :")
    if prompt1:
        prompt1 = f"Suggest me a sample research paper title about {prompt1}"
        # getting title of research paper
        title = generate_response(prompt1)
        st.write("The title is : ")
        st.subheader(title)
        # getting sections of research paper
        request = f"Generate the sections of the research paper having the title {title} separated by a comma without any numbering or bullets"
        respform = generate_response(request)
        respform = respform[2:]
        respform = respform.split(",")
        # getting sections of paper you want us to write
        options = st.multiselect('What section of the paper would you like me to write? 🤓✨',
                                 respform,
                                 respform[:2])
        if(st.button("Submit")):
            for i in options:
                request = f"Generate the {i} section of the paper titled {title}"
                response = generate_response(request)
                st.subheader(f"{i}:")
                st.write(response)
