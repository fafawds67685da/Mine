import streamlit as st
from PIL import Image
import os

# Set page layout
st.set_page_config(page_title="My Everything", layout="centered")

# Title with emojis and heartwarming text
st.markdown(
    "<h1 style='text-align: center; color: #e91e63;'>My Everything ❤️<br> My heart, My love forever 💖</h1>",
    unsafe_allow_html=True
)

# CSS for image frame and scrollable container
st.markdown(
    """
    <style>
    .frame-container {
        display: flex;
        justify-content: center;
        margin-top: 30px;
        max-height: 80vh;
        overflow-y: auto;
    }
    .photo-frame {
        border: 10px solid #e0e0e0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        padding: 10px;
        border-radius: 15px;
        background-color: white;
        width: 80%;
    }
    img {
        width: 100%;
        border-radius: 10px;
    }
    .message {
        text-align: center;
        font-size: 24px;
        color: #e91e63;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

image_path = "assets/WhatsApp Image 2025-05-20 at 13.14.28_27f6efc6.jpg"  # Relative path
if os.path.exists(image_path):
    image = Image.open(image_path)
    # HTML wrapper for the frame
    st.markdown('<div class="frame-container"><div class="photo-frame">', unsafe_allow_html=True)
    st.image(image, use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)
else:
    st.error("❌ Image not found.")
    
# Bottom message
st.markdown('<div class="message">I love you honey ❤️</div>', unsafe_allow_html=True)
