# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hemg2c3vbh9VlCk81-ffHkBU6MgJI2Ks
"""

import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
  marks_in_percentage=[]
  days_present=[]

  with open(data_path)as csv_file:
    csv_reader=csv.DictReader(csv_file)

    for row in csv_reader:
      marks_in_percentage.append(float(row['Marks In Percentage']))
      days_present.append(float(row['Days Present']))
  
  return{'x':marks_in_percentage,'y':days_present}

def findCorrelation(datasource):
  correlation=np.corrcoef(datasource['x'],datasource['y'])
  print('Correlation between Marks in percentage and Days present :- \n--->',correlation[0,1])

data_path='Student Marks vs Days Present.csv'
datasource=getDataSource(data_path)
findCorrelation(datasource)