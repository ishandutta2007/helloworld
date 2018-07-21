import signal
from PyQt4.QtGui import QApplication
from pyapp.logicwidget import LogicWidget

def main():
    # Ctrl+C should kill the program
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication([])

    window = LogicWidget()
    window.show()
    window.raise_() 

    app.exec_()

if __name__ == "__main__":
    main()
