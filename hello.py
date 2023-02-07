import sys
from urllib import request
import os
import requests
from PyQt6 import*
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox
from PyQt6.QtCore import QSize, QRect
from PyQt6.QtGui import QPixmap
def fetch_value():
    selected_camera=comboBox2.currentText()
    selected_date = dateEdit.date().toPyDate()
    print(selected_date)
    Api_key='IVq7C5Zg7JhdBNrepSwUsYnjznjHfxSq0PsgQMzT'
    response = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={selected_date}&api_key=IVq7C5Zg7JhdBNrepSwUsYnjznjHfxSq0PsgQMzT&page=1&camera={selected_camera}")
    a=response.json()
    print(a)
    List=[]
    for i in a['photos']:
     x=i['img_src']
     print(x)
     List.append(x)
     for item in range(len(List)):
        img= List[item]
        r = requests.get(img)
        with open(f"image{item}.JPG",'wb') as f:
            f.write(r.content)


        
            
application = QApplication([])
mainWindow = QWidget()
mainWindow.setGeometry(0,0, 500, 400)
mainWindow.setWindowTitle('Mars rover')
pushButton = QPushButton(parent=mainWindow, text='Fetch')
pushButton.move(250, 250)
pushButton.clicked.connect(fetch_value)
label2 = QLabel(mainWindow)
label2.setText("Select Camera :")
label2.move(50, 20)
comboBox2 = QComboBox(mainWindow)
comboBox2.move(250, 300)
comboBox2.setGeometry(QRect(40, 40, 200, 31))
comboBox2.addItems([" ", "fhaz", "rhaz","mast","chemcham","mahli","mardi","navcam"])
label3 = QLabel(text="Select Date:", parent=mainWindow)
label3.move(50, 120)
dateEdit = QDateEdit(parent=mainWindow)
dateEdit.move(250, 400)
dateEdit.setGeometry(QRect(42, 150, 200, 21))
dateEdit.setDisplayFormat("yyyy-MM-dd")
dateEdit.setDate(QDate.currentDate())
pixmap = QPixmap('/Users/kirtisikka/Documents/amfoss/mars/image0.JPG')
mainWindow.show()
application.exec()


    

   

