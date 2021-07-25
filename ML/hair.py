import streamlit as st
import base64
from PIL import Image
from img_classification import teachable_machine_classification

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

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 52px;"><b>Image Classification for Hair loss Prediction</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:Fjord One; color:Black; font-size: 32px;"><b>Upload an Image of the skin to find out</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:Philosopher; color:Black; font-size: 30px;"><b>Choose a Skin image ...</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)


    uploaded_file = st.file_uploader(" ", type="jpg",key="hair")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'Hair_model.h5')
        if label == 0:
            st.write("The Image has Hair loss")
            
        else:
            st.write("The Image Doesn't have any hair loss")
        st.write(" ")
        result = st.button ("Find out more")
        if result:
            st.write("1.Regular hair washing is a part of preventing hair loss by the way of keeping hair and scalp clean.\n Doing so, you are lowering the risk of infections and dandruff that may lead to hair breakage or loss.") 
            st.write("2.Vitamins are not only healthy for overall wellbeing but also good for your hair.\n Vitamin A encourages healthy production of sebum in the scalp, \nvitamin E betters blood circulation in the scalp to help hair follicles remain productive \nand vitamin B helps hair maintain its healthy colour. \nEating lean meats, fish, soy or other proteins promotes hair health and in turn helps curb hair loss.")
            st.write("3.Those who have been experiencing hair loss for quite some time must massage the scalp with essential oil for couple of minutes.\n When hair is wet, it is in its weakest state. So, avoid brushing wet hair because the chances of hair loss increases.\n But if you must comb wet hair, use a very wide-toothed comb.")
            st.write("4.The hair shaft comprises one quarter water so drink at least four to eight cups of water in a day \nto stay hydrated and for the growth of healthy hair.\n Studies in the past have found medical evidence to link stress with hair loss.\n De-stress yourself. \nThere are many health conditions, particularly skin-related conditions, that causes changes in hormonal balances which in turn lead to hair loss.\n Make sure you see a doctor regularly for your underlying illnesses and conditions.")
    