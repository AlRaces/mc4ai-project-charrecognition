import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sklearn.metrics import confusion_matrix
from keras.models import load_model

dataset = np.load("../np_dataset.npy")
labels = np.load("../labels.npy")
names = np.load("../names.npy")

st.markdown("<h2 style='text-align: center;'><b>Graphs & Confusion Matrix</b></h2>",
            unsafe_allow_html=True)
st.divider()

# KHÔNG HOẠT ĐỘNG
draw_confusion = st.button("Confusion Matrix")
if draw_confusion:
    size = st.slider("Choose size of dataset to train Matrix:",
                     100, dataset.shape[0])
    set_size = st.button("Done!")
    if set_size:
        try:
            model = load_model(
                "../sequential_model.h5")
        except Exception as e:
            st.warning(
                "Something went wrong!, please check if you've set model configurations.")
            st.stop()
        size = int(size)
        x = dataset[:size]
        y = labels[:size]
        y_pred = model.predict(x).argmax(axis=1)
        cm = confusion_matrix(y, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, cmap='Blues',
                    yticklabels=names, xticklabels=names)
        ax.set_title("Confusion Matrix")
        st.pyplot(fig)
