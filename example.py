import streamlit as st
from PIL import Image, ImageFilter


# File upload
uploaded_file = st.file_uploader("Bir fotoğraf yükleyin")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    filteres=['Original','Blur','Emboss','Sharpness','Find Edges']
    filter_choice=st.selectbox("Filter",filteres) 

    # buttons
    if filter_choice=='Blur':
        image = image.filter(ImageFilter.BLUR)

    elif filter_choice=='Emboss':
        image = image.filter(ImageFilter.EMBOSS)

    elif filter_choice=='Sharpness':
        image = image.filter(ImageFilter.SHARPEN)
       
    elif filter_choice=='Find Edges':
        image=image.filter(ImageFilter.FIND_EDGES)    

    # show new pic
    st.image(image, caption='Your processed image', use_column_width=True)
