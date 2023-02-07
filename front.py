import sys
import requests
from PyQt6 import QtWidgets, QtGui, QtCore
from urllib import request
import os
import requests
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, QRect
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox

class MainWindow(QMainWindow):
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(0, 0, 600, 6000)
        self.setWindowTitle('Mars Rover')
        self.setFixedSize(1000, 800)

        pushButton = QtWidgets.QPushButton(parent=self, text='Fetch')
        pushButton.move(250, 250)
        pushButton.clicked.connect(self.fetch_value)
        pushButton=QtWidgets.QPushButton(parent=self, text='Next')
        pushButton.move()
        pushButton.clicked.connect(self.)


        label2 = QtWidgets.QLabel(self)
        label2.setText("Select Camera:")
        label2.move(50, 20)

        self.comboBox2 = QtWidgets.QComboBox(self)
        self.comboBox2.move(250, 300)
        self.comboBox2.setGeometry(QRect(40, 40, 200, 31))
        self.comboBox2.addItems([" ", "fhaz", "rhaz", "mast", "chemcam", "mahli", "mardi", "navcam"])

        label3 = QtWidgets.QLabel(text="Select Date:", parent=self)
        label3.move(50, 120)

        self.dateEdit = QtWidgets.QDateEdit(parent=self)
        self.dateEdit.move(250, 400)
        self.dateEdit.setGeometry(QRect(42, 150, 200, 21))
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
      #   self.image_label1 = QLabel(self)
      #   self.image_label1.setGeometry(QRect(250, 20, 200, 200))
      #   self.image_label2 = QLabel(self)
      #   self.image_label2.setGeometry(QRect(450, 20, 200, 200))
      self.image_labels = []
        for i in range(100):
            self.image_labels.append(QLabel(self))
            self.image_labels[i].setGeometry(QRect(250, 20 + (i * 200), 200, 200))
        
   def fetch_value(self):
      selected_camera = self.comboBox2.currentText()
      selected_date = self.dateEdit.date().toPyDate()
      print(selected_date)
      API_KEY = 'IVq7C5Zg7JhdBNrepSwUsYnjznjHfxSq0PsgQMzT'
      response = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={selected_date}&api_key={API_KEY}&page=1&camera={selected_camera}")
      a = response.json()
      print(a)
      image_list = []
      for i in a['photos']:
        img = i['img_src']
        print(img)
        image_list.append(img)
        for item in range(len(image_list)):
         img = image_list[item]
         r = requests.get(img)
         with open(f"image{item}.JPG", 'wb') as f:
                f.write(r.content)
         
         self.pixmap = QPixmap(f"image{item}.JPG")
         if item == 0:
            self.image_label1.setPixmap(self.pixmap)
         if item == 1:
            self.image_label2.setPixmap(self.pixmap)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
