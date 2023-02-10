import sys
import ezgmail
import requests
from PyQt6 import QtWidgets, QtGui, QtCore
from urllib import request
import os, shutil
import requests
from PyQt6.QtCore import QSize, QRect,Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget,QLineEdit,QPushButton,QTextEdit, QMessageBox

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.i=0
    self.w = None 
    self.setGeometry(0, 0, 600, 6000)
    self.setWindowTitle('Mars Rover')
    self.total_images=0
 
      
    self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
               
                font-size: 16px;
                margin: 4px 2px;
          
                border-radius: 5px;
            }
            QLabel {
                font-size: 18px;
            }
            QComboBox {
                font-size: 18px;
                background-color: #4CAF50;
            }
            QDateEdit {
                font-size: 18px;
                background-color: #F0F0F0;
            }
        """)
    pushButton = QtWidgets.QPushButton(parent=self, text='Fetch')
    pushButton.setGeometry(QRect(250, 250, 100, 30))
    pushButton.clicked.connect(self.fetch_value)
    pushButton=QtWidgets.QPushButton(parent=self, text='Next')
    pushButton.setGeometry(QRect(650, 350, 100, 30))
    pushButton.clicked.connect(self.next_value)
    pushButton=QtWidgets.QPushButton(parent=self, text='Previous')
    pushButton.setGeometry(QRect(550, 350, 100, 30))
    pushButton.clicked.connect(self.previous_value)
    pushButton=QtWidgets.QPushButton(parent=self, text='Send Email')
    pushButton.setGeometry(QRect(550, 550, 100, 30))
    pushButton.clicked.connect(self.show_new_window)
    label2 = QtWidgets.QLabel(self)
    label2.setText("Select Camera:")
    label2.setGeometry(QRect(50, 20, 150, 30))
    self.comboBox2 = QtWidgets.QComboBox(self)
    self.comboBox2.setGeometry(QRect(250, 300, 200, 31))
    self.comboBox2.addItems([" ", "fhaz", "rhaz", "mast", "chemcam", "mahli", "mardi", "navcam"])
    self.dateEdit = QtWidgets.QDateEdit(parent=self)
    self.dateEdit.setGeometry(QRect(250, 400, 200, 21))
    self.dateEdit.setDisplayFormat("yyyy-MM-dd")
    self.dateEdit.setDate(QtCore.QDate.currentDate())
    label3 = QtWidgets.QLabel(text="Select Date:", parent=self)
    label3.setGeometry(QRect(50, 120, 150, 30))
    self.label = QLabel(self)
    self.label.setGeometry(QRect(400, 20, 550, 700))
    self.setGeometry(0, 0, 800, 600)
    self.setWindowTitle('Mars Rover')


        # self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
      

       

        
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
      image_list.append(img)
    folder_name = "IMAGE"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for item in range(len(image_list)):
      img = image_list[item]
      r = requests.get(img)
      self.i=0
      with open(f"{folder_name}/image{item}.JPG", 'wb') as f:
            f.write(r.content)
            self.pixmap=QPixmap(f'IMAGE/image{self.i}.JPG')
            self.label.setPixmap(self.pixmap)
  def next_value(self):
    self.pixmap=QPixmap(f'IMAGE/image{self.i}.JPG')
    self.label.setPixmap(self.pixmap)
    self.i+=1
    self.label.show()
    
  def previous_value(self):
    self.pixmap=QPixmap(f'IMAGE/image{self.i}.JPG')
    # print(self.pixmap)
    self.label.setPixmap(self.pixmap)
    self.i-=1
    self.label.show()
  def newwindow(self):
    super().__init__()
    self.button=QPushButton("Push for window")
    self.button.clicked.connect(self.show_new_window)
    self.setAnimated(self.button)
  
  def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()    
class AnotherWindow(QWidget):
  """
  This is the second window.

 
  """
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setWindowTitle("Email Sending")
    self.emailLabel = QLabel(self)
    self.emailLabel.setText('Email: ')
    self.emailLine = QLineEdit(self)
    self.emailLine.move(50, 300)
    self.emailLine.resize(200, 30)
    self.emailLabel.move(50, 270)

    self.subjectLabel = QLabel(self)
    self.subjectLabel.setText('Subject:')
    self.subjectLine = QLineEdit(self)
    self.subjectLine.move(50, 350)
    self.subjectLine.resize(200, 32)
    self.subjectLabel.move(50, 325)

    self.bodyLabel = QLabel(self)
    self.bodyLabel.setText('Body: ')
    self.bodyText = QTextEdit(self)
    self.bodyText.move(50, 450)
    self.bodyText.resize(200, 30)
    self.bodyLabel.move(50, 430)
    self.sendButton = QPushButton('SEND', self)
    self.sendButton.clicked.connect(self.sendEmail)
    self.sendButton.resize(200, 32)
    self.sendButton.move(50, 600)
    
  def sendEmail(self):
      mail = self.emailLine.text().split(',')
      subject = self.subjectLine.text()
      body = self.bodyText.toPlainText()
      folder_path = 'IMAGE'
      images = []
      for image_file in os.listdir(folder_path):
        if image_file.endswith(".JPG"):
          images.append(os.path.join(folder_path, image_file))
          print("To:", ', '.join(mail))
          print("Subject:", subject)
          print("Message Body:", body)
          for recipient in mail:
            ezgmail.send(recipient, subject, body, attachments=images)
            print(f'Email sent to {recipient}')
            QMessageBox.information(self, "Sent", "The email was sent successfully.")
      shutil.rmtree('IMAGE')
      self.close()
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

