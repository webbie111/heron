import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

listCompare = []
listOfMovieNames = ['Black Panther', 'The Sound of Water', 'The Greatest Showman'] # To be changed to work with DB


class CompareMovies(QWidget):
    def __init__(self, parent = None):
       super(CompareMovies, self).__init__(parent)

       layout = QHBoxLayout()
       self.b1 = QCheckBox('Black Panther')
       self.b1.stateChanged.connect(lambda:self.addRemoveList(self.b1,listCompare,listOfMovieNames))

       self.b2 = QCheckBox('The Sound of Water')
       self.b2.toggled.connect(lambda:self.addRemoveList(self.b2,listCompare,listOfMovieNames))

       self.b3 = QCheckBox('The Greatest Showman')
       self.b3.toggled.connect(lambda:self.addRemoveList(self.b3,listCompare,listOfMovieNames))

       layout.addWidget(self.b1)
       layout.addWidget(self.b2)
       layout.addWidget(self.b3)

       # <GARBAGE START>
       self.model = QStringListModel()
       self.model.setStringList(listOfMovieNames)
       self.completer = QCompleter()
       self.completer.setModel(self.model)
       self.completer.setCaseSensitivity(0) # 0 is insensitive 1 is sensitive
       self.lineedit = QLineEdit()
       self.lineedit.setCompleter(self.completer)
       layout.addWidget(self.lineedit)
       # <GARBAGE END>

       # buttons
       self.search = QPushButton('Search')
       self.search.clicked.connect(lambda:self.searchLineEdit(self.b2))
       layout.addWidget(self.search)

       self.compareMovies = QPushButton('Compare')
       self.compareMovies.clicked.connect(lambda:self.plotListCompare(listCompare))
       layout.addWidget(self.compareMovies)

       self.setLayout(layout)
       self.setWindowTitle("Choose movie tab")
       #self.showMaximized()
    def addRemoveList(self,checkBox,moviesToCompare,listOfName):
        print('addRemoveList')
        # arguments: moviesToCompare = current list of movies in the buffer
        #            checkBox = this is the check box that you are calling this function with
        #            listOfName = list of all movies that have check boxes
        for i in range(len(listOfName)):
              if checkBox.text() == listOfName[i]:
                 if checkBox.isChecked() == True:
                    listCompare.append(listOfName[i])

                    print checkBox.text()+" is selected"
                    print(moviesToCompare)
                 else:
                    print checkBox.text()+" is deselected"
                    if listOfName[i] in listCompare:
                        listCompare.remove(listOfName[i])
                    print(moviesToCompare)
        # returns: newly updated list of movies put into the compare buffer
        return moviesToCompare
    def searchLineEdit(self, whatever_is_currently_in_lineEdit):
        print('search')

    def plotListCompare(self,listCompare):
        print('plot whatever is currently in listCompare',listCompare)
        # matplotlib function

def main():

   app = QApplication(sys.argv)
   ex = CompareMovies()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
