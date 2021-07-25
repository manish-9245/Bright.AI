import streamlit as st
import base64
from PIL import Image
from img_classificationallergy import teachable_machine_classification

def app():
    st.title('')
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

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 52px;"><b>Image Classification for Skin Allergy Prediction</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 32px;"><b>Upload an Image of the skin to find out</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 30px;"><b>Choose a Skin image ...</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)


    uploaded_file = st.file_uploader(" ", type="jpg",key="allergy")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'allergy.h5')
        if label == 0:
            st.write("The Image has Skin Allergy ")
            
        else:
            st.write("The Image has no allergy")
        st.write(" ")
    
        result = st.button ("Find out more")
        
        if result:
            st.write("The most common causes of skin allergies include:")
            st.write("•Nickel, a metal used in jewelry and snaps on jeans, makeup, lotions, soaps, and shampoos •Sunscreens and bug sprays •Medications you put on your skin, like antibiotics or anti-itch creams •Fragrances •Cleaning products •Plants, including poison ivy •Latex, which is used in stretchy things like plastic gloves, elastic in clothing, condoms, and balloons") 
            st.write("Treatment :")
            st.write("You may need to wear gloves to protect your skin. When you do have a reaction, try to ease the symptoms and prevent an infection. Don't scratch, even though that's a hard urge to resist. Over-the-counter products and home remedies can help relieve the itching and stop the swelling. Try these:  •Hydrocortisone cream •Ointments like calamine lotion •Antihistamines •Cold compresses •Oatmeal baths •Talk to your doctor about what's best for your specific rash.") 

    