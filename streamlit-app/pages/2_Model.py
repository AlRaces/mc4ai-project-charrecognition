import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
from keras.models import load_model
import os

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
        result_picture = result_picture.convert("L")
        result_picture = result_picture.resize((28, 28))
        result_picture.save(
            "D:\CAPSTONE_AI\mc4ai-project-charrecognition\streamlit-app\pages\input_folder\img_from_canvas.png")
        st.success('Image saved!')

st.caption('_or upload a picture:_')
uploaded_files = st.file_uploader("", type=[
                                  'png', 'jpg', 'jpeg'], accept_multiple_files=True, label_visibility="collapsed")

please_predict = st.button("***PREDICT***")
if please_predict:
    names = np.load("D:/CAPSTONE_AI/mc4ai-project-charrecognition/names.npy")
    try:
        model = load_model(
            "D:\CAPSTONE_AI\mc4ai-project-charrecognition\streamlit-app\sequential_model.h5")
    except Exception as e:
        st.write(
            "Something went wrong, please check if you've set model configurations")
        st.stop()

    # CONVERT UPLOADED IMAGES INTO FILES WITH CORRECT SPECS
    for i, uploaded_file in enumerate(uploaded_files):
        bytes_data = uploaded_file.read()
        image = Image.open(io.BytesIO(bytes_data))
        image = image.convert('L')
        image.save(
            f"D:\CAPSTONE_AI\mc4ai-project-charrecognition\streamlit-app\pages\input_folder\{str(i)}.png")
    path = "D:\CAPSTONE_AI\mc4ai-project-charrecognition\streamlit-app\pages\input_folder"

    # PREDICT UPLOADED IMAGES
    result = []
    inputname = []
    for i, filename in enumerate(os.listdir(path)):
        filename = str(filename)
        image = Image.open(f"{path}\{filename}")
        image = np.array(image)
        image = image.astype(np.float32) / 255.0
        iamge = image.reshape(1, 28 * 28)
        r = int(model.predict(image))
        result.append(names[r])
        inputname.append(f"Picture Uploaded no: {i}")

    # CHECK AND PREDICT DRAWN IMAGES
    if os.path.isfile("D:\CAPSTONE_AI\mc4ai-project-charrecognition\streamlit-app\pages\input_folder\img_from_canvas.png"):
        image = Image.open(
            "D:\CAPSTONE_AI\mc4ai-project-charrecognition\streamlit-app\pages\input_folder\img_from_canvas.png")
        image = np.array(image)
        image = image.astype(np.float32) / 255.0
        iamge = image.reshape((1, 28, 28, 1))
        r = model.predict(image)
        result.append(names[r])
        inputname.append("Image drawn from canvas")
    st.write(result)
    st.write("Corresponding image order:")
    st.write(inputname)

    # VALIDATE OUTPUT
    correctness = st.radio("Does the answer satisfy you ?",
                           "All Correct", options=("Something Wrong"))
    if correctness == "Something Wrong":
        st.write(
            "We are sorry for the inaccuracy of our model, could you give us the answer so we can improve next time?")
