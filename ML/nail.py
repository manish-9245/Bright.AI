import streamlit as st
import base64
from PIL import Image
from img_classificationnail import teachable_machine_classification

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

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 52px;"><b>Image Classification for Nail Fungus Prediction</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 32px;"><b>Upload an Image of the Nail to find out</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 30px;"><b>Choose a Skin image ...</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)


    uploaded_file = st.file_uploader(" ", type="jpg",key="nail")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'Nail_model.h5')
        if label == 0:
            st.write("The Image has a Nail fungus")
            
        else:
            st.write("The Image has no Nail fungus")
        st.write(" ")
        result = st.button ("Find out more")
        if result:
            st.write("1.Over-the-counter products aren’t usually recommended to treat nail infections since they don’t provide reliable results. Instead, your doctor may prescribe an oral antifungal medication, such as:\n•	terbinafine (Lamisil)\n•	itraconazole (Sporanox)\n•	fluconazole (Diflucan)\n•	griseofulvin (Gris-PEG)")
            st.write("Your doctor may prescribe other antifungal treatments, such as antifungal nail lacquer or topical solutions. \nThese treatments are brushed onto the nail in the same way that you’d apply nail polish.")
            st.write("Depending on the type of fungus causing the infection, as well as the extent of the infection, you may have to use these medications for several months. \nTopical solutions aren’t generally effective in curing toenail fungal infections.")
            st.write("Treatment isn’t guaranteed Trusted Source to completely rid your body of the fungal infection. Complications from fungal infection are also possible.") 
            st.write("2.Prevent fungal nail infections \n•	washing your hands after touching infected nails\n•	drying your feet well after showering, especially between your toes\n•	getting manicures or pedicures from trustworthy salons\n•	avoiding being barefoot in public places\n•	reducing your use of artificial nails and nail polish")

    