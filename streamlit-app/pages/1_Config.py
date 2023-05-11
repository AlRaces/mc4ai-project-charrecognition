import streamlit as st
import PIL
import numpy

st.markdown("<h2 style='text-align: center; color: blue;'>LHP Capstone Project - Text Recognition </h2>",
            unsafe_allow_html=True)
st.divider()

st. subheader('Configuration')
st.caption('_Have fun!_')

train_choice = st.slider(
    'Choose the number of train pictures you want to use:', 100, 3410)
test_choice = st.slider('Choose test size:', 100, 3410)
epoch_choice = st.slider('Choose the number of epochs:', 1, 100)
loss_choice = st.radio(
    "Choose the loss model you want to use",
    ('categorical_crossentropy (Recommended)', 'CE', 'MAE', 'MSE'))

config_finish = st.button("Set Config")
if config_finish:
    st.write(test_choice)
    st.write(train_choice)
    st.write(epoch_choice)
    st.write(loss_choice)
