
import streamlit as st
import random
import requests
import os 
list_of_styles = os.listdir('style')
st.title("🦄 Reverie")

para = '<p></p>'
intro = '''<p style="font-family:Source Sans Pro,sans-serif; color:Pink; font-weight:600;font-size: 1rem">
Reverie allows you to explore your imaginative world through the lens of different art forms.<br>  
Choose from different fantasy caricatures to visualize yourself and your friends!</p>'''

# st.write(my_list)

st.markdown(intro, unsafe_allow_html=True)

new_title = '<span style="font-family:Source Sans Pro,sans-serif; color:#F5003D; font-weight:800;font-size: 1.4rem;">Create your own fictional character in 3 easy steps!!</span>'
st.markdown(new_title, unsafe_allow_html=True)

# st.write("Create your own fictional character in 3 easy steps!!")
st.code("1. Upload your own character. This can be a selfie/photograph")
st.code("2. Choose a fantasy art form")
st.code("3. Visualize your character in the form of a cartoon")

uploaded_file = st.file_uploader("Choose a file")

# print(r.json())
if uploaded_file is not None:
    st.success("File uploaded!")
    # st.write("File content:", uploaded_file.getvalue())

selectbox = st.selectbox("Choose your art form", ["Cartoon", "Realistic", "DreamLike","Neural Style Transfer"])

if selectbox == "Cartoon":
    if st.button("Create Image: "):
        with st.spinner("Generating Image..."):
            k = uploaded_file.getvalue()
            r = {}
            r = requests.post(
            "https://api.deepai.org/api/toonify",
            files={
                'image':k,
            },
            headers={'api-key': '0ee5a2d4-dcde-4511-b434-b3565e9d0240'})        
            image = requests.get(r.json()['output_url'])
        st.balloons()
        st.image(image.content)

if selectbox == "Realistic":

    if st.button("Create Image: "):
        with st.spinner("Generating Image..."):
            k = uploaded_file.getvalue()
            style_index= random.randint(0,len(list_of_styles))

            r = {}
            r = requests.post(
            "https://api.deepai.org/api/fast-style-transfer",
            files={
                'content': k,
                'style': open(f'./style/{list_of_styles[style_index]}', 'rb'),
            },
                headers={'api-key': '0ee5a2d4-dcde-4511-b434-b3565e9d0240'}

            )
            image = requests.get(r.json()['output_url'])

        st.balloons()    
        st.image(image.content)

if selectbox == "DreamLike":
    if st.button("Create Image: "):
        with st.spinner("Generating Image..."):

            k = uploaded_file.getvalue()
            r = requests.post(
            "https://api.deepai.org/api/deepdream",
            files={
                'image': k,
            },
                headers={'api-key': '0ee5a2d4-dcde-4511-b434-b3565e9d0240'}

            )
            
            image = requests.get(r.json()['output_url'])
        
        st.balloons()
        st.image(image.content)


if selectbox == "Neural Style Transfer":
    if st.button("Create Image: "):
        with st.spinner("Generating Image..."):
            k = uploaded_file.getvalue()
            style_index= random.randint(0,len(list_of_styles))

            r = requests.post(
                "https://api.deepai.org/api/neural-style",
                files={
                    'style': open(f'./style/{list_of_styles[style_index]}', 'rb'),
                    'content': k,
                },
                    headers={'api-key': '0ee5a2d4-dcde-4511-b434-b3565e9d0240'}

            )
            print(r.json())
            image = requests.get(r.json()['output_url'])
        st.balloons()
        st.image(image.content)        