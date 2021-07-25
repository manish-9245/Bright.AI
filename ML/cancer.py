import streamlit as st
import base64
from PIL import Image
from img_classificationcancer import teachable_machine_classification

def app():
    st.title(' ')
    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)

    set_background('Front.jpg')

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 52px;"><b>Image Classification for Skin cancer Prediction</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 32px;">Upload an Image of the skin to find out</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 30px;">Choose a Skin image ...</p>'
    st.markdown(new_title, unsafe_allow_html=True)


    uploaded_file = st.file_uploader(" ", type="jpg",key="cancer")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded MRI.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'keras_model.h5')
        if label == 0:
            st.write("The Image has is a Benign Disease")
            
        else:
            st.write("The Image has is a Malignant Disease")
        st.write(" ")
        result = st.button ("Find out more")
        if result:
            st.write("While many growths and tumors will turn out to be benign,\n it’s still always a good idea to make an appointment \n with your doctor as soon as you detect a \n growth or new symptoms that could indicate a tumor. This includes skin lesions or unusual-looking moles.It’s also important to make an \n appointment with your doctor if you notice any changes in a tumor \n that was previously diagnosed as benign, including growth or a change in symptoms. Some types of benign tumors can \n become cancerous over time, and early detection \n can make all the difference.") 
    