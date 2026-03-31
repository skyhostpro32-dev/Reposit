import streamlit as st
import requests
import io

st.title("✨ AI Object Remover")

image = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])
mask = st.file_uploader("Upload Mask (white = remove)", type=["png","jpg"])

API_KEY = "YOUR_CLIPDROP_API_KEY"

if image and mask:
    if st.button("🚀 Remove Object"):
        with st.spinner("Processing..."):
            response = requests.post(
                "https://clipdrop-api.co/cleanup/v1",
                files={
                    "image_file": image,
                    "mask_file": mask
                },
                headers={"x-api-key": API_KEY}
            )

            result = response.content

            st.image(result, caption="Result")

            st.download_button(
                "📥 Download",
                result,
                "output.png"
            )
