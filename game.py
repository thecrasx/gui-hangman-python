



class Hangman:
    def __init__(self, word = '', maxMistakes = 3):
        self.mistakes = 0
        self.__map = {"valid-indexes": []}

        self.setMaxMistakes(maxMistakes)

        if word:
            self.setWord(word)


    def setWord(self, word: str):
        if word.replace(' ', '') == '':
            raise ValueError("Word must contain characters")

        self.word = word
        self.display = []

        for char in word:
            if char != ' ':
                self.display.append('_')
            else:
                self.display.append(' ')

    
    def setMaxMistakes(self, maxMistakes: int):
        if maxMistakes < 1:
            raise ValueError("'maxMistakes' cannot be 0 or below")

        else:
            self.__maxMistakes = maxMistakes
            self.maxMistakes = maxMistakes


    def guess(self, char) -> bool:
        valid = False

        for i, c in enumerate(self.word):
            if char.lower() == c.lower():
                self.__map['valid-indexes'].append(i)
                self.__map[i] = c

                valid = True

        
        if not valid:
            self.mistakes += 1


        return valid


    def show(self) -> str:
        for i in self.__map['valid-indexes']:
            self.display[i] = self.__map[i]
    
        return "".join(self.display)


    
    def isCorrect(self) -> bool:
        if self.show() == self.word:
            return True
        else:
            return False

    
    def isGameOver(self) -> bool:
        if self.mistakes > self.__maxMistakes:
            return True
        else:
            return False


    def reset(self):
        self.mistakes = 0
        self.__map = {"valid-indexes": []}

    
    def theEndIsClose(self) -> int:
        return self.__maxMistakes - self.mistakes






if __name__ == "__main__":

    h = Hangman(maxMistakes=0)

    #h.setWord("Television")


    #print(h.isCorrect())

    #print(h.show())