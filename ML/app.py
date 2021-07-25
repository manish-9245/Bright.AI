import streamlit as st
from multiapp import MultiApp
import gloww, acne, allergy, hair, nail, cancer
import base64
from PIL import Image
import keras
from PIL import Image, ImageOps
import numpy as np
from img_classification import teachable_machine_classification # import your app modules here
app = MultiApp()

new_title = '<p style="font-family:sans-serif; color:Black; font-size: 52px;"><b>Bright.AI</b></p>'
st.markdown(new_title, unsafe_allow_html=True)


# Add all your application here
app.add_app("Bright.AI", gloww.app)
app.add_app("Acne", acne.app)
app.add_app("Skin Allergy", allergy.app)
app.add_app("Hairloss", hair.app)
app.add_app("Nail Fungus", nail.app)
app.add_app("Skin cancer", cancer.app)
# The main app
app.run()