import sys

from PyQt5.QtWidgets import QApplication

from controllers.main_window import MainWindowForm

import RPi.GPIO as GPIO



if __name__ == '__main__':
    app = QApplication(sys.argv)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

    window = MainWindowForm()
    window.show()



    sys.exit(app.exec())