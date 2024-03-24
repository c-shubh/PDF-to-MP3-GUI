from Model import Model


class Controller:
    model = None

    def __init__(self):
        self.model = Model()

    def saveMp3FromPdf(self, voice, rate, filePath, targetPath):
        """
        voice: String
        rate: int
        filePath: String
        targetPath: String

        returns: void
        """
        self.model.saveMp3(
            self.model.extractTextFromPdf(filePath).replace("\n", " "),
            voice,
            rate,
            targetPath,
        )

    def saveMp3FromTextFile(self, voice, rate, filePath, targetPath):
        self.model.saveMp3(
            self.model.extractTextFromTextFile(filePath), voice, rate, targetPath
        )

    def saveMp3FromInputText(self, voice, rate, textData, targetPath):
        self.model.saveMp3(textData, voice, rate, targetPath)

    def saveTextFromPdf(self, filePath, targetPath):
        """
        filePath: String
        targetPath: String

        returns: void
        """
        self.model.saveText(self.model.extractTextFromPdf(filePath), targetPath)

    def saveTextFromInput(self, textData, targetPath):
        self.model.saveText(textData, targetPath)

    def playMp3(self, filePath):
        """
        filePath: String

        returns: void
        """
        self.model.playMp3(filePath)
