import PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.tabs = QTabWidget()

        self.setWindowIcon(QtGui.QIcon('browserIcon.png'))
        self.setWindowTitle('GreenBrow by Shayan')
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        backBtn = QAction('←', self)
        backBtn.triggered.connect(self.browser.back)
        navbar.addAction(backBtn)

        forwardBtn = QAction('→', self)
        forwardBtn.triggered.connect(self.browser.forward)
        navbar.addAction(forwardBtn)

        reloadBtn = QAction('↻', self)
        reloadBtn.triggered.connect(self.browser.reload)
        navbar.addAction(reloadBtn)

        homeBtn = QAction('Home', self)
        homeBtn.triggered.connect(self.homepage)
        navbar.addAction(homeBtn)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.urlpage)
        navbar.addWidget(self.urlBar)

        self.browser.urlChanged.connect(self.updateUrlBar)

    def homepage(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def urlpage(self):
        url = self.urlBar.text()
        if url.count('.')==0:
            url = 'https://www.google.com/search?q=' + url

        elif not(url[0:7] == 'http://' or url[0:8] == 'https://'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))
        
    def updateUrlBar(self, resetUrl):
        self.urlBar.setText(resetUrl.toString())
 
app = QApplication(sys.argv)
QApplication.setApplicationName("mybrowser")
window = Window()
app.exec_()