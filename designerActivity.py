# -*- coding: utf-8 -*-
"""
Редактор Spyder

Designer activity
"""

import matplotlib.pyplot as plt
import csv
import ast

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
        
        print(minutes)
        
        if appName in logdata:
            logdata[appName] += minutes
        else:
            logdata[appName] = minutes
            
    return logdata

def filterLogData(logdata):
    communication = ['Telegram', 'WhatsApp', 'Битрикс24', 'Skype']
    ux = ['XMind', 'Notion']
    design = ['Photoshop CC', 'Sketch', 'Adobe Illustrator CC 2018']
    prototype = ['Axure RP 8', 'Spark']
    frontend = ['Zeplin']
    
    newLogdata = {}
    newLogdata['Communication'] = 0
    newLogdata['UX'] = 0
    newLogdata['Design'] = 0
    newLogdata['Prototype'] = 0
    newLogdata['Frontend'] = 0
    
    for key in logdata:
        if key in communication:
            newLogdata['Communication'] += logdata[key]
        if key in ux:
            newLogdata['UX'] += logdata[key]
        if key in design:
            newLogdata['Design'] += logdata[key]
        if key in prototype:
            newLogdata['Prototype'] += logdata[key]
        if key in frontend:
            newLogdata['Frontend'] += logdata[key]
    
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
    
    logdata = parseLogData('./testData.csv')
    
    logdata = filterLogData(logdata)
    
    showPieChart(logdata)
    
    print('Script is ended')