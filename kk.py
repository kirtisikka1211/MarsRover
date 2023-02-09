
import sys
import ezgmail
import requests
from PyQt6 import QtWidgets, QtGui, QtCore
from urllib import request
import os
import shutil
import requests
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, QRect, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox, QScrollArea, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QMessageBox, QDateEdit, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.i = 0
        self.w = None
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Mars Rover')
        self.total_images = 0
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 5px;
            }
            QLabel {
                font-size: 18px;
            }
            QComboBox {
                font-size: 18px;
                background-color: #F0F0F0;
            }
            QDateEdit {
                font-size: 18px;
                background-color: #F0F0F0;
            }
        """)

        # Add buttons in a horizontal layout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(30)

        # Create fetch button
        pushButton = QtWidgets.QPushButton(parent=self, text='Fetch')
        button_layout.addWidget(pushButton)
        pushButton.clicked.connect(self.fetch_value)

        # Create send email button
        pushButton = QtWidgets.QPushButton(parent=self, text='Send Email')
        button_layout.addWidget(pushButton)
        pushButton.clicked.connect(self.show_new_window)

        # Add the button layout to the main window
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(button_layout)

        # Add a label for the image
        self.label = QLabel(self)
        self.main_layout.addWidget(self.label)
        self.label.setGeometry(400, 20, 550, 700)

        # Add a horizontal layout for the navigation buttons
        navigation_layout = QHBoxLayout()
        navigation_layout.setSpacing(30)

        # Create previous button
        pushButton = QtWidgets.QPushButton(parent=self, text='Previous')
        navigation_layout.addWidget(pushButton)
        pushButton.clicked.connect(self.previous_value)

        # Create next button
        pushButton = QtWidgets.QPushButton(parent=self, text='Next')
        navigation_layout.addWidget(pushButton)
        pushButton.clicked.connect(self.next_value)

        # Add the navigation layout to the main layout
        self.main_layout.addLayout(navigation_layout)

        # Add a vertical layout for the selection options
        selection_layout = QVBoxLayout()
        selection_layout.setSp

        # button = QPushButton("Get Text")
        # button.clicked.connect(self.get)
        # layout.addWidget(button)

        # button = QPushButton("Clear Text")
        # button.clicked.connect(self.input.clear)
        # layout.addWidget(button)

        # button = QPushButton("Get Text")
        # button.clicked.connect(self.get)
        # layout.addWidget(button)

        # button = QPushButton("Clear Text")
        # button.clicked.connect(self.input.clear)
        # layout.addWidget(button)

        # self.label.setWidgetResizable(True)

        # self.label.setWidget(self.scroll_area_widget_contents)
        # self.label = []
        # self.label = QLabel(self)
        # self.label1.setGeometry(QRect(250, 20, 200, 200))
        # self.image_label2 = QLabel(self)
      #   self.image_label2.setGeometry(QRect(450, 20, 200, 200))
      # self.image_labels = []
      #   for i in range(100):
      #       self.image_labels.append(QLabel(self))
      #       self.image_labels[i].setGeometry(QRect(250, 20 + (i * 200), 200, 200))

    def fetch_value(self):
      selected_camera = self.comboBox2.currentText()
      selected_date = self.dateEdit.date().toPyDate()
      print(selected_date)
      API_KEY = 'IVq7C5Zg7JhdBNrepSwUsYnjznjHfxSq0PsgQMzT'
      response = requests.get(
          f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={selected_date}&api_key={API_KEY}&page=1&camera={selected_camera}")
      a = response.json()
      print(a)
      image_list = []
    #   for i in a['photos']:
    #    img = i['img_src']
    #    image_list.append(img)
    #  folder_name = "IMAGE"
    # if not os.path.exists(folder_name):
    #     os.makedirs(folder_name)
    # for item in range(len(image_list)):
    #   img = image_list[item]
    #   r = requests.get(img)
    #   with open(f"{folder_name}/image{item}.JPG", 'wb') as f:
    #         f.write(r.content)

            # self.pixmap=QPixmap(f'IMAGE/image0.JPG')
            # self.label4.setPixmap(self.pixmap)
      # image = QPixmap(f"{folder_name}/image{item}.JPG")
      # label = QLabel(self.scroll_area_widget_contents)
      # label.setPixmap(image)
      # label.move(20, 20 + item * 150)
      # self.image_labels.append(label)
      # for label in self.image_labels:
      #    label.show()
    def next_value(self):
     self.pixmap = QPixmap(f'IMAGE/image{self.i}.JPG')
     self.label.setPixmap(self.pixmap)
     self.i += 1
     self.label.show()

   def previous_value(self):
    self.pixmap=QPixmap(f'IMAGE/image{self.i}.JPG')
    print(self.pixmap)
    self.label.setPixmap(self.pixmap)
    self.i-=1
    self.label.show()
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
        
        # ezgmail.send("kirtisikka972@gmail.com","Subject","hdouwhcnwercfr")

     

             
                


         
         # self.pixmap = QPixmap(f"image{item}.JPG")
         # if item == 0:
         #    self.image_label1.setPixmap(self.pixmap)
         # if item == 1:
         #    self.image_label2.setPixmap(self.pixmap)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())