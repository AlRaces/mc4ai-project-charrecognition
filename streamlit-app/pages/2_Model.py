import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
st.markdown("<h2 style='text-align: center; color: blue;'>LHP Capstone Project - Text Recognition </h2>",
            unsafe_allow_html=True)
st.divider()

st.subheader('Input')
st.caption('_Draw your letter here!_')

# DRAWING
# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "point", "line",
                      "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider(
        "Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")

realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

if st.button('Done!'):
    if canvas_result.image_data is not None:
        result_picture = canvas_result.image_data
        result_picture = Image.fromarray(result_picture)
        result_picture.convert("L")
        result_picture.save("./input_folder/result_picture.png")
        st.write('Image saved!')

st.caption('_or upload a picture:_')
uploaded_files = st.file_uploader("", type=[
                                  'png', 'jpg', 'jpeg'], accept_multiple_files=True, label_visibility="collapsed")
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("Image processed:", uploaded_file.name)
