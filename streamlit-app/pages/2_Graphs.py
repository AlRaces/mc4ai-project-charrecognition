import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sklearn.metrics import confusion_matrix
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split

dataset = np.load("../np_dataset.npy")
labels = np.load("../labels.npy")
names = np.load("../names.npy")
try:
    model = load_model(
        "./sequential_model.h5")
except Exception as e:
    st.warning(
        "Something went wrong!, please check if you've set model configurations.")
    st.stop()

st.markdown("<h2 style='text-align: center;'><b>Graphs & Confusion Matrix</b></h2>",
            unsafe_allow_html=True)
st.divider()

st.subheader("***CONFUSION MATRIX***")
size = st.slider("Choose size of dataset for __Confusion Matrix__",
                 100, dataset.shape[0] - 100)
set_train_size = st.button("Set train size!")
if set_train_size:
    size = int(size)
    X_train, X_test, y_train, y_test = train_test_split(
        dataset, labels, test_size=size)
    y_pred = model.predict(X_test).argmax(axis=1)
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(62, 62))
    sns.heatmap(cm, annot=True, cmap='Blues',
                yticklabels=names, xticklabels=names)
    ax.set_title("Confusion Matrix")
    st.pyplot(fig)

st.subheader("***DATASET***")
with st.spinner("Please wait for dataset to load"):
    fig, axs = plt.subplots(62, 3)
    X_train, X_test, y_train, y_test = train_test_split(dataset, labels)
    fig.set_figheight(20)
    fig.set_figwidth(20)
    for i in range(62):
        for j in range(3):
            target = np.random.choice(np.where(y_train == i)[0])
            axs[i][j].axis("off")
            axs[i][j].imshow(X_train[target].reshape(28, 28), cmap="gray")
    st.pyplot(fig)
