import streamlit as st
import base64
from PIL import Image
from img_classificationacne import teachable_machine_classification

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

    new_title = '<p style="font-family:Fjord One; color:Black; font-size: 52px;"><b>Image Classification For Skin Acne Prediction</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:Cinzel; color:Black; font-size: 32px;">Upload an Image of the skin to find out</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:Philosopher; color:Black; font-size: 30px;">Choose a Skin image ...</p>'
    st.markdown(new_title, unsafe_allow_html=True)


    uploaded_file = st.file_uploader(" ", type="jpg",key="acne")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'Acne_model.h5')
        if label == 0:
            st.write("The Image has is a acne")
            
        else:
            st.write("The Image has no acne")
        st.write(" ")
        result = st.button ("Find out more")
        if result:
            st.write("1. Anyone can get pimples, no matter their skin type. Oily skin is the most pimple-prone. It’s caused by your skin’s sebaceous glands producing too much oily sebum.\nTo help prevent pimples, \nit’s important to remove excess oil, dirt, and sweat daily. Washing your face \nmore than twice a day may make acne worse, however.Don’t wash your face with harsh cleansers that dry skin.\n Use an alcohol-free cleanser. Moisturizers help skin stay hydrated. But many moisturizers contain oil, synthetic fragrance, \nor other ingredients that may irritate skin and cause pimples.")
            st.write("2. If you’re dehydrated, your body may signal your skin’s oil glands to produce more oil.\n Dehydration also gives your skin a dull appearance and promotes inflammation and redness.\nTo keep your body well-hydrated, drink at least eight 8-ounce glasses of water each day") 
            st.write("3. It’s tempting to use makeup to cover up pimples. However, doing so may clog pores and trigger outbreaks.\n Your hands encounter grime and bacteria constantly throughout the day. \nAnd each time you touch your face, some of those pore-clogging impurities may get transferred to your skin. \nHigh glycemic foods and beverages such as chips, baked goods made with white flour, \nand soft drinks spike blood sugar levels and are often less nutritious than low glycemic foods.\nThe study also found eating dairy may trigger pimples.")
            st.write("4. Catching some rays may dry out pimples in the short term, but it causes major problems in the long run.\n Frequent sun exposure dehydrates the skin, which over time causes it to produce more oil and block pores.")
    