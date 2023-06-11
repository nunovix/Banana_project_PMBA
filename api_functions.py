import numpy as np
from tkinter import filedialog
import tkinter as tk

def get_banana_preference(flags_for_like):
    res = 0.0
    for i in range(flags_for_like.shape[0]):
        res=res+(i%4)*flags_for_like[i]
    return res/np.sum(flags_for_like)

def get_time_prediction(ideal_banana, banana_currently):
    m = 0.21
    return (ideal_banana - banana_currently)/m 

