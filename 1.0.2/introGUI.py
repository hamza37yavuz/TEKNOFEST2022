from winreg import QueryValue
from PyQt5 import QtWidgets,QtCore
import sys

def gui():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()

    window.setWindowTitle("First GUI")
    window.setGeometry(500,500,800,800)

    #video 2 QLabel
    """
    sticker = QtWidgets.QLabel(window)
    sticker.setText("Camera control")
    sticker.move(300,150)
    """
    
    #video 3 QLineEdit
    """
    input_ = QtWidgets.QLineEdit(window)
    #example information
    input_.setText("2.4")
    #unchangeable
    
    # input_.setReadOnly(True)
    # input_.move(400,200)

    #video 4 QPushButton
    button = QtWidgets.QPushButton(window)
    button.setText("open cam")
    #you don't want to push button
    
    # button.setEnabled(False)
    
    # button.move(420,250)  11.video icin yorum satiri yapilmistir
    """
    
    #video 5 QRadioButton
    """
    radio1 = QtWidgets.QRadioButton(window)
    radio2 = QtWidgets.QRadioButton(window)
    radio3 = QtWidgets.QRadioButton(window)
    radio1.setText("option 1")
    radio2.setText("option 2")
    radio3.setText("option 3")
    radio3.setCheckable(False)
    radio1.move(50,50)
    radio2.move(50,70)
    radio3.move(50,90)
    """

    #video 6 QCheckBox
    """
    control1= QtWidgets.QCheckBox(window)
    control2= QtWidgets.QCheckBox(window)
    control3= QtWidgets.QCheckBox(window)
    control1.setText("option 1")
    control2.setText("option 2")
    control3.setText("option 3")
    control1.move(100,110)
    control2.move(100,130)
    control3.move(100,150)
    control3.setCheckable(False)
    """

    #video 7 QComboBox
    """
    combo = QtWidgets.QComboBox(window)
    combo.addItem("mode GUIDED")
    combo.addItem("mode STABILIZE")
    combo.addItem("mode LOITER")
    print(combo.count())
    combo.setItemText(2,"mode AUTOTUNE")
    # combo.move(50,25)  11.video icin yorum satiri yapilmistir
    """
    
    #video 8 QSpinbox
    """
    spin = QtWidgets.QSpinBox(window)
    spindouble = QtWidgets.QDoubleSpinBox(window)
    spin.setRange(5,25)
    spin.setSingleStep(5)
    spindouble.move(50,175)
    spindouble.setSingleStep(0.5)
    """

    #video 9 QSlider
    """
    HSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal,window)
    VSlider = QtWidgets.QSlider(QtCore.Qt.Vertical,window)
    HSlider.move(100,200)
    VSlider.move(100,250)
    #horizontal
    HSlider.minimum()
    HSlider.maximum()
    HSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
    HSlider.setTickInterval(2)
    #vertical
    VSlider.minimum()
    VSlider.maximum()
    VSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
    VSlider.setTickInterval(2)
    """
    #video 10 Siganl-Slot
    """
    line = QtWidgets.QLineEdit(window)
    button2 = QtWidgets.QPushButton(window)
    # line.move(300,300)  11.video icin yorum satiri yapilmistir
    # button2.move(300,320)  11.video icin yorum satiri yapilmistir
    button2.setText("Send")
    def update():
        line.setText("6")
    button2.clicked.connect(update)
    """
    #video 11 Layout
    """
    Hlayout = QtWidgets.QHBoxLayout()
    Vlayout = QtWidgets.QVBoxLayout()
    Hlayout.addWidget(button2)
    Hlayout.addWidget(button)
    Vlayout.addWidget(line)
    Vlayout.addWidget(combo)
    """
    window.show()
    sys.exit(object.exec_())
    
def gui2():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()

    window.setWindowTitle("First GUI")
    window.setGeometry(250,100,600,300)
    
    #video 12 QGridLayout (for video 12)
    """
    button1 = QtWidgets.QPushButton(window)
    button2 = QtWidgets.QPushButton(window)
    button3 = QtWidgets.QPushButton(window)
    button4 = QtWidgets.QPushButton(window)
    button1.setText("open cam")
    button2.setText("mission 1")
    button3.setText("mission 2")
    button4.setText("mission 3")
    layout = QtWidgets.QGridLayout()
    layout.addWidget(button1,1,1)
    layout.addWidget(button2,1,2)
    layout.addWidget(button3,2,1)
    layout.addWidget(button4,2,2)
    window.setLayout(layout)
    """
    
    #video 13 QFormLayout
    """
    sticker = QtWidgets.QLabel(window)
    sticker2 = QtWidgets.QLabel(window)
    sticker.setText("Username")
    sticker2.setText("Password")
    line = QtWidgets.QLineEdit(window)
    line2 = QtWidgets.QLineEdit(window)
    layout1 = QtWidgets.QFormLayout()
    layout1.addRow(sticker,line)
    layout1.addRow(sticker2,line2)
    window.setLayout(layout1)
    """
    window.show()
    sys.exit(object.exec_())
    
gui()

# for video 12 and 13
# gui2()