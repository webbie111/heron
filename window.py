import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from pie import *

listOfMovieNames = ['Black Panther', 'The Sound of Water', 'The Greatest Showman'] # To be changed to work with DB
takings = ['1320', '1222', '950']
movieBuffer = []
timeSpan = 'daily'
# global bufferNumber
# bufferNumber = 0

class Window(QScrollArea):
    def removeBuffer(self, button):
        print(button)
        print('Layout',self.bufferScrollLayout)
        #self.bufferScrollLayout.removeWidget(button)
        #button.setParent(None)
        button.setVisible(False)
        print button.text()
        movieBuffer.remove(button.text())
        # def __str__(self):
        #     return "name"
        print movieBuffer

    def movie2Buffer(self,button):
        print(self.bufferScrollLayout)
        if button.text() not in movieBuffer:
            #bufferNumber += 1
            # buff = 'buffer'+str(bufferNumber)
            movieBuffer.append(button.text())
            self.butt = QPushButton(button.text())
            self.make_buffer_button(self.butt)
            #self.butt.clicked.connect(lambda:self.removeBuffer(self.butt))
            self.bufferScrollLayout.addWidget(self.butt)
            self.butt.setVisible(True)
        print movieBuffer
    def make_buffer_button(self,button):
        return button.clicked.connect(lambda:self.removeBuffer(button))

    def make_movie_button(self,button):
        return button.clicked.connect(lambda:self.movie2Buffer(button))
    def selectDaily(self):
        timeSpan = 'daily'
        print timeSpan+'\n'
    def selectWeeky(self):
        timeSpan = 'weekly'
        print timeSpan+'\n'
    def selectOverall(self):
        timeSpan = 'overall'
        print timeSpan+'\n'
    def compare(self):
        print('plot',movieBuffer,'for',timeSpan)
        bufferTakings = []
        for i in range(len(movieBuffer)):
            index = listOfMovieNames.index(movieBuffer[i])
            bufferTakings.append(takings[index])
        print(bufferTakings)
        print(movieBuffer)
        pie_plot_week(movieBuffer,bufferTakings)
        #pie_plot_week(movieBuffer,takings)
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
        self.daily.toggled.connect(lambda:self.selectDaily())
        self.weekly.toggled.connect(lambda:self.selectWeeky())
        self.overall.toggled.connect(lambda:self.selectOverall())

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
            self.make_movie_button(self.movie)
            self.movieScrollLayout.addWidget(self.movie)

        self.compareButton = QPushButton('Compare')
        self.compareButton.clicked.connect(lambda:self.compare())
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
