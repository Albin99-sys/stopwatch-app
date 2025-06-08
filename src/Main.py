# python PyQt5 stop watch

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt



class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00")
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")


        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)


        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        Hbox = QHBoxLayout()
        Hbox.addWidget(self.start_button)
        Hbox.addWidget(self.stop_button)
        Hbox.addWidget(self.reset_button)


        vbox.addLayout(Hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton {
                font-size:50pt;
            }
            QLabel{
                font-size:120pt;
                background-color:hsl(208, 85%, 71%);
                border-radius:20px;
            }
        """)




    def start(self):
        pass





    def stop(self):
        pass




    def reset(self):
        pass




    def format_time(self,time):
        pass





    def update_display(self):
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
