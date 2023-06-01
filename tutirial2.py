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
        my_lable = qtw.QLabel("pick something")
        #font size
        my_lable.setFont(qtg.QFont('Helvatice', 18))        
        self.layout().addWidget(my_lable)
        
        #combo box
        my_combo = qtw.QComboBox(self,
                 editable =True,
                 insertPolicy = qtw.QComboBox.InsertAtBottom)
        #add items to combo box
        my_combo.addItem("pepperoni0", "something")
        my_combo.addItem("pepperoni1", 2)
        my_combo.addItem("pepperoni2", qtw.QTabWidget)
        my_combo.addItem("pepperoni3")
        
        self.layout().addWidget(my_combo)
        
        
        #button
        my_button = qtw.QPushButton("click me",
                                    clicked = lambda:press_it())
        self.layout().addWidget(my_button)
        
        
        #show app
        self.show()
        
        
        def press_it():
            my_lable.setText(f'you picked {my_combo.currentText()}')
            


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
