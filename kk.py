import sys
import ezgmail
import requests
from PyQt6 import QtWidgets, QtGui, QtCore
from urllib import request
import os, shutil
import requests
from PyQt6.QtCore import QSize, QRect, QPropertyAnimation,QPoint
from PyQt6.QtGui import QPixmap,QMovie,QFont
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget,QLineEdit,QPushButton,QTextEdit, QMessageBox

class MainWindow(QMainWindow):
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.i=0
        self.w=None
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle('The Martian Chronicles 🚀')
        self.setFixedSize(1000, 900)

        # self.labelani = QLabel("Animated Text", self)
        # self.labelani.setGeometry(100, 100, 200, 50)

        # animation = QPropertyAnimation(self.labelani, b"pos")
        # animation.setDuration(1000)
        # animation.setStartValue(QPoint(100, 100))
        # animation.setEndValue(QPoint(300, 300))
        # animation.start()

        # animation = QPropertyAnimation(self.labelani, b"opacity")
        # animation.setDuration(1000)
        # animation.setStartValue(0.0)
        # # animation.setEndValue(100.0)
        labelmov = QLabel(self)
        labelmov.setScaledContents(True)
        movie = QMovie("20140818_mars_vmcanimation_aug14.gif")
        labelmov.setGeometry(QRect(200, 20, 900, 750))
        labelmov.setMovie(movie)
        movie.start()
        

        self.setStyleSheet("""

            QPushButton {
               
              
                background-color: dark-grey;
                color: white;
                border: 1px solid #FC7300;
        
                font: bold 16px;
                 
                text-align: center;
             
             
             
                border-radius: 10px;
            }
            QMainWindow {
                background-color: black;
            }
            QLabel {
                font-size: 18px;
            }
            QComboBox {
                font-size: 18px;
                border: 1px solid #FC7300;
            }
            QDateEdit {
                font-size: 18px;
                 border: 1px solid #FC7300;
            }
            QPushButton:hover {
            background-color: #FC953F;
             color: dark-grey;
        
    }
        """)
        
        pushButton = QtWidgets.QPushButton(parent=self, text='Fetch')
        pushButton.setGeometry(50, 250, 160, 43)
        pushButton.clicked.connect(self.fetch_value)
        pushButton=QtWidgets.QPushButton(parent=self, text='Next')
        # pushButton.move(650,850)

        pushButton.setGeometry(685, 750, 160, 43)
        pushButton.clicked.connect(self.next_value)
        pushButton=QtWidgets.QPushButton(parent=self, text='Previous')
        # pushButton.move(550,850)
        pushButton.setGeometry(485, 750, 160, 43)
        pushButton.clicked.connect(self.previous_value)
        pushButton=QtWidgets.QPushButton(parent=self, text='Send Email')
        pushButton.setGeometry(50, 310, 160, 43)
        pushButton.clicked.connect(self.show_new_window)
        label2 = QtWidgets.QLabel(self)
        label2.setText("Camera:")
        label2.move(50, 120)
        self.comboBox2 = QtWidgets.QComboBox(self)
        self.comboBox2.move(250, 300)
        self.comboBox2.setGeometry(QRect(40, 150, 200, 21))
        self.comboBox2.addItems(["Select Camera ", "fhaz", "rhaz", "mast", "chemcam", "mahli", "mardi", "navcam"])
        self.dateEdit = QtWidgets.QDateEdit(parent=self)
        self.dateEdit.move(250, 400)
        self.dateEdit.setGeometry(QRect(40, 40, 200, 21))
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        label3 = QtWidgets.QLabel(text="Select Date:", parent=self)
        label3.move(50, 10)
        self.setGeometry(0, 0, 600, 6000)
        self.setWindowTitle('The Martian Chronicles 🚀')
        self.labelpic = QLabel(self)
        self.labelpic.setGeometry(QRect(400, 20, 550, 700))
        # self.labelpic.setStyleSheet("background-color: rgb(255, 255, 255);")

       

        
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
            self.labelpic.setPixmap(self.pixmap)
   def next_value(self):
    self.pixmap=QPixmap(f'IMAGE/image{self.i}.JPG').scaled(700,700)
    self.labelpic.setPixmap(self.pixmap)
    self.i+=1
    self.labelpic.show()
    
   def previous_value(self):
    self.pixmap=QPixmap(f'IMAGE/image{self.i}.JPG')
    # print(self.pixmap)
    self.labelpic.setPixmap(self.pixmap)
    self.i-=1
    self.labelpic.show()
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
    self.setFixedSize(600, 800)
    
    self.image = QLabel(self)
    self.image.setGeometry(QRect(200, 55, 1000, 800))
    self.image.setPixmap(QPixmap("/Users/kirtisikka/Documents/amfoss/mars/mars2222.jpg").scaled(400,400))
    self.logo = QLabel(self)
    self.logo.setGeometry(QRect(65, 30, 500, 300))
    self.logo.setPixmap(QPixmap("/Users/kirtisikka/Documents/amfoss/mars/send-mail-icon-sms-line-260nw-1129600793.png").scaled(200,200))
    self.setStyleSheet("""

            QTextEdit {
                border: 1px solid #FC7300;
                color: #FDEEDC;

 
                text-align: center;
             
                font-size: 18px;
                margin: 4px 2px;
                border-radius: 10px;
            }
            QWidget { background-color: black; }"
            QLabel {
                font-size: 18px;

            }
           

            
           
        """)


         
 


        
    
    self.setWindowTitle("Email Sending")
    self.emailLabel = QLabel(self)
    self.emailLabel.setText('Email: \n\nSeprate by comma for multiple recipeints')
    self.emailLine = QTextEdit(self)
    self.emailLine.move(50, 350)
    self.emailLine.resize(200, 40)
    self.emailLabel.move(50, 270)

    self.subjectLabel = QLabel(self)
    self.subjectLabel.setText('Subject:')
    self.subjectLine =QTextEdit(self)
    self.subjectLine.move(50, 430)
    self.subjectLine.resize(200, 40)
    self.subjectLabel.move(50, 400)

    self.bodyLabel = QLabel(self)
    self.bodyLabel.setText('Body: ')
    self.bodyText = QTextEdit(self)
    self.bodyText.move(50, 520)
    self.bodyText.resize(200, 150)
    self.bodyLabel.move(50, 490)
    self.sendButton = QPushButton('SEND', self)
    self.sendButton.clicked.connect(self.sendEmail)
    self.sendButton.resize(200, 32)
    self.sendButton.move(50, 700)
   
    font = QFont()
    font.setPointSize(16)
    self.bodyLabel.setFont(font)
    self.emailLabel.setFont(font)

    self.subjectLabel.setFont(font)
    self.subjectLine.setFont(font)

    self.sendButton.setStyleSheet("""
    QPushButton {
        background-color: dark-grey;
        color: white;
        border: 2px solid #FC7300;
        border-radius: 10px;
        font: bold 16px;
    }
    QPushButton:hover {
        background-color: #FC953F;
        color: dark-grey;
    }
""")

    
    
  def sendEmail(self):
      mail = self.emailLine.toPlainText().split(',')
      subject = self.subjectLine.toPlainText()
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
            while True:
                try:
                    ezgmail.send(recipient, subject, body, attachments=images)
                    print(f'Email sent to {recipient}')
                    break
                except Exception as e:
                    print(f"Error sending email to {recipient}: {e}")
                    response = QMessageBox.warning(self, "Sent", "The email entered is wrong. Try Again?",
                                                QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
                    if response == QMessageBox.No:
                        break
                    else:
                        continue
      QMessageBox.information(self, "Sent", "The email was sent successfully.")
    
      
      shutil.rmtree('IMAGE')
     
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
