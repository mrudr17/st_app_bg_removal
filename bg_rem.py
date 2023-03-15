
import streamlit as st
import requests
from PIL import Image
from rembg import remove
from io import BytesIO



# ---- SIDEBAR ----
with st.sidebar:
    st.title("Background Removal")
    st.header("Please upload your picture that needs background removal")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    submit = st.button('Submit')

if submit:

    if uploaded_file is not None:
        #response = requests.post(
        #    "https://api.rembg.com/v1/remove",
        #    files={"image": uploaded_file},
        #    headers={"Authorization": "ApiKey YOUR_API_KEY"},
        #)

        #img = Image.open(BytesIO(response.content))
        
        st.header("Image after background removed")

        img  = remove(Image.open(uploaded_file))
        new_image = img.resize((400, 200))

        st.image(new_image, caption="Background Removed Image", use_column_width=True)

        # Download button
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        byte_im = buffered.getvalue()
        btn = st.download_button(
          label="Download Image",
          data=byte_im,
          file_name="output.png",
          mime="image/png",
          )
        #download_button_str = download_button(buffered.getvalue(), "background_removed.png", "Download Image")
        #st.markdown(btn, unsafe_allow_html=True)

