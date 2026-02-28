from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1100, 1100)

 #       self.widgetSvg = QSvgWidget(parent=self)
  #      self.widgetSvg.setGeometry(10, 10, 1080, 1080)
        svgWidget = QSvgWidget('svgs/svgwrite-example3.svg')
        svgWidget.setGeometry(50,50,759,668)


def view_svg_file(filename,x=0,y=0,width=1000,height=1000):
    app = QApplication(sys.argv) 
    svgWidget = QSvgWidget(filename)
    svgWidget.setGeometry(x,y,width,height)
    svgWidget.show()       
    sys.exit(app.exec_())            

if __name__ == "__main__":
    if False:
        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec()
    else:
        app = QApplication(sys.argv) 
        svgWidget = QSvgWidget('svgs/svgwrite-example3.svg')
        svgWidget.setGeometry(0,0,1000,1000)
        svgWidget.show()       
        sys.exit(app.exec_())        