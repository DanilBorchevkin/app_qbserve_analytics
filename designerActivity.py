# -*- coding: utf-8 -*-
"""
Designer activity
"""

import matplotlib.pyplot as plt
import csv 
from tkinter import filedialog
from tkinter import *

CSV_FIELDS = ['Minutes', 'Name', 'App', 'Category']

def parseLogData(filepath):
    logdata = {}
    
    dictReader = csv.DictReader(open(filepath, 'r', encoding='utf-8'),
                                fieldnames = CSV_FIELDS,
                                delimiter = ',')
    
    for row in dictReader:
        appName = row['App']

        minutes = row['Minutes']

        try:
            minutes = float(minutes)
        except:
            continue
                
        if appName in logdata:
            logdata[appName] += minutes
        else:
            logdata[appName] = minutes
            
    return logdata

def filterLogData(logdata):
    communication = ['Telegram', 'WhatsApp', 'Битрикс24', 'Skype', 'Spark']
    ux = ['XMind', 'Notion']
    sketch = ['Sketch']
    photoshop = ['Photoshop CC']
    illustrator = ['Adobe Illustrator CC 2018']
    prototype = ['Axure RP 8']
    frontend = ['Zeplin']
    research = ['Google Chrome']
    
    newLogdata = {}
    newLogdata['Communication'] = 0
    newLogdata['UX'] = 0
    newLogdata['Sketch'] = 0
    newLogdata['Photoshop'] = 0
    newLogdata['Illustrator'] = 0
    newLogdata['Prototype'] = 0
    newLogdata['Frontend'] = 0
    newLogdata['Research'] = 0
    
    for key in logdata:
        if key in communication:
            newLogdata['Communication'] += logdata[key]
        if key in ux:
            newLogdata['UX'] += logdata[key]
        if key in sketch:
            newLogdata['Sketch'] += logdata[key]
        if key in photoshop:
            newLogdata['Photoshop'] += logdata[key]
        if key in illustrator:
            newLogdata['Illustrator'] += logdata[key]
        if key in prototype:
            newLogdata['Prototype'] += logdata[key]
        if key in frontend:
            newLogdata['Frontend'] += logdata[key]
        if key in research:
            newLogdata['Research'] += logdata[key]
    
    return newLogdata

def showPieChart(logdata):
    labels = logdata.keys()
    sizes = logdata.values()
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, 
            labels=labels, 
            autopct='%1.1f%%',
            shadow=True, 
            startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

if __name__ == "__main__":
    print('Script is started')

    root = Tk()
    root.filename =  filedialog.askopenfilename(title = "Select file")
    filepath = root.filename

    logdata = parseLogData(filepath)
    
    logdata = filterLogData(logdata)
    
    showPieChart(logdata)
    
    print('Script is ended')