import numpy as np
import streamlit as st
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Input, Flatten
from tensorflow.random import set_seed
from tensorflow.keras.backend import clear_session

DATASET = np.load("np_dataset.npy")
LABELS = np.load("labels.npy")
NAMES = np.load("names.npy")
