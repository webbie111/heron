import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

listOfMovieNames = ['Black Panther', 'The Sound of Water', 'The Greatest Showman'] # To be changed to work with DB
movieBuffer = []
bufferNumber = 0
class Window(QScrollArea):

    def movie2Buffer(self,button):
        if button.text() not in movieBuffer:
            # self.bufferNumber += 1
            # buff = 'buffer'+str(bufferNumber)
            movieBuffer.append(button.text())

            #self.bufferScrollLayout.addWidget()
        print movieBuffer

    def make_button(self,button):
        return button.clicked.connect(lambda:self.movie2Buffer(button))
    def __init__(self):
        super(Window, self).__init__()

        # layout
        layout = QVBoxLayout()

        # heading text
        self.header = QLabel()
        self.header.setText('Select Movies to compare takings')
        layout.addWidget(self.header)

        hbox = QHBoxLayout()

        # check boxes
        self.daily = QRadioButton('daily')
        self.weekly = QRadioButton('weekly')
        self.overall = QRadioButton('overall')

        hbox.addWidget(self.daily)
        hbox.addStretch()
        hbox.addWidget(self.weekly)
        hbox.addStretch()
        hbox.addWidget(self.overall)

        layout.addLayout(hbox)

        self.daily.setChecked(True)
        self.daily.toggled.connect(lambda:self.btnstate(self.daily))
        self.weekly.toggled.connect(lambda:self.btnstate(self.weekly))
        self.overall.toggled.connect(lambda:self.btnstate(self.overall))

        # layout.addWidget(self.daily)
        # layout.addWidget(self.weekly)
        # layout.addWidget(self.overall)

        self.scrollTitle = QLabel('Movies')
        self.bufferTitle = QLabel('Buffer')

        self.movieScroll = QScrollArea()
        self.bufferScroll = QScrollArea()
        #self.movieScroll.setWidget(self.scrollTitle)

        self.movieScrollLayout = QVBoxLayout()
        self.movieScroll.setLayout(self.movieScrollLayout)

        self.bufferScrollLayout = QVBoxLayout()
        self.bufferScroll.setLayout(self.bufferScrollLayout)

        for i in range(len(listOfMovieNames)):
            movie = 'movie'+str(i)
            print movie
            self.movie = QPushButton(listOfMovieNames[i])
            self.make_button(self.movie)
            self.movieScrollLayout.addWidget(self.movie)

        self.compareButton = QPushButton('Compare')
        layout.addWidget(self.compareButton)

        layout.addWidget(self.movieScroll)
        layout.addWidget(self.bufferScroll)
        layout.addWidget(self.compareButton)
        self.setLayout(layout)
        self.setWindowTitle("Choose movie tab")


def main():

   app = QApplication(sys.argv)
   ex = Window()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()