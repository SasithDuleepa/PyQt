import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        #add title 
        self.setWindowTitle("hello world!!")
        
        #layout -verticle
        self.setLayout(qtw.QVBoxLayout())
        
        #label
        my_lable = qtw.QLabel("hello what's your name??")
        #font size
        my_lable.setFont(qtg.QFont('Helvatice', 18))        
        self.layout().addWidget(my_lable)
        
        #entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_filed")
        my_entry.setText("")
        self.layout().addWidget(my_entry)
        
        #button
        my_button = qtw.QPushButton("click me",
                                    clicked = lambda:press_it())
        self.layout().addWidget(my_button)

        self.show()
        
        
        def press_it():
            my_lable.setText(f'Hello {my_entry.text()}')
            my_entry.setText("")  #clear entry box


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
