import streamlit as st
import PIL
import numpy

st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>LHP Capstone Project - Text Recognition </h2>",
            unsafe_allow_html=True)
st.divider()

st.markdown("<h3 style='text-align: center; color: #FFFAF4; text-decoration: underline;'>Loss & Accuracy Graph</h3>",
            unsafe_allow_html=True)


image_loss = "D:\CAPSTONE_AI\mc4ai-project-charrecognition\streamlit-app\loss.png"
st.image(image_loss, caption="Loss Graph with Epochs = 1000")
image_accuracy = "D:\CAPSTONE_AI\mc4ai-project-charrecognition\streamlit-app\precise.png"
st.image(image_accuracy, caption="Accuracy Graph with Epochs = 1000")

# Sidebar titles
st.sidebar.subheader('Configuration')
st.sidebar.caption('_Have fun!_')

# sidebar sliders
train_choice = st.sidebar.slider(
    'Choose the number of train pictures you want to use:', 100, 3410)
test_choice = st.sidebar.slider('Choose test size:', 100, 3410)
epoch_choice = st.sidebar.slider('Choose the number of epochs:', 1, 100)

# sidebar checkbox
loss_function_option = [
    "categorical_crossentropy (Recommended)", 'CE', 'MAE', 'MSE']
loss_choice = st.sidebar.selectbox(
    "Choose your loss function: ", loss_function_option)

# validate options
config_finish = st.sidebar.button("Set Config")
if config_finish:
    st.write(test_choice)
    st.write(train_choice)
    st.write(epoch_choice)
    st.write(loss_choice)
