# -*- coding: utf-8 -*-
"""Project108

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OTAipDdNOzGiV0ODZ1Ti0HPNrjm8sjQw
"""

from google.colab import files
data_to_load=files.upload()

import pandas as pd
import plotly.figure_factory as ff
import csv
df=pd.read_csv("mobileBrandData.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"])
fig.show()