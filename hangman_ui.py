from PySide6.QtGui import QPixmap
from game import Hangman
from queue import Queue
import random




class HangmanUI(Hangman):
    def __init__(self, mainWindow):
        super().__init__()
        self.window = mainWindow
        self.ui = mainWindow.ui

        self.ui.startBtn.clicked.connect(self.start)
        self.ui.playAgainBtn.clicked.connect(self.start)

        with open("wordlist.txt", "r") as f:
            self.words = f.readlines()

        self.words = [word.replace("\n", "") for word in self.words]
        self.queue = Queue(len(self.words))

        

    def fillQueue(self):
        random.shuffle(self.words)
           
        for word in self.words:
            self.queue.put(word)
            

    def getWord(self):
        if self.queue.empty():
            self.fillQueue()

        return self.queue.get()

    
    def start(self):
        self.reset()
        self.changeStage()
        self.setWord(self.getWord())

        self.ui.wordLabel.setText(self.show())
        self.ui.counterLabel.setText(f"{self.mistakes}/{self.maxMistakes}")

        self.ui.stackedWidget.setCurrentWidget(self.ui.gamePage)



    def guess(self, char):
        if super().guess(char):
            if self.isCorrect():
                self.ui.resultLabel.setText("Win")
                self.ui.stackedWidget.setCurrentWidget(self.ui.finalPage)

            else:
                self.ui.wordLabel.setText(self.show())

        else:
            if self.isGameOver():
                self.ui.resultLabel.setText("Game Over")
                self.ui.stackedWidget.setCurrentWidget(self.ui.finalPage)

            else:
                self.ui.counterLabel.setText(f"{self.mistakes}/{self.maxMistakes}")
                self.changeStage()

        


    def changeStage(self):
        if self.mistakes == 0:
            stage = "./assets/Stage 1"

        elif self.theEndIsClose() <= 1:
            stage = "./assets/Stage 6"

        elif self.theEndIsClose() == 2:
            stage = "./assets/Stage 5"

        elif self.theEndIsClose() == 3:
            stage = "./assets/Stage 4"

        elif self.theEndIsClose() == 4:
            stage = "./assets/Stage 3"

        elif self.theEndIsClose() == 5:
            stage = "./assets/Stage 2"

        elif self.theEndIsClose() >= 6:
            stage = "./assets/Stage 1"
 

        self.ui.hangmanLabel.setPixmap(QPixmap(stage))

