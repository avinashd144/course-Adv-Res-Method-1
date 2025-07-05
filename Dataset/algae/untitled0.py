# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 07:24:13 2025

@author: LENOVO
"""
import scipy.io
import pandas as pd

mat_data = scipy.io.loadmat("algae.mat")
df = pd.DataFrame(mat_data['algae'])  # Replace with actual variable name
df.to_excel("algae.xlsx", index=False)

