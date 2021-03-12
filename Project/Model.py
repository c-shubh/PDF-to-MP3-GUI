from pdfminer.high_level import extract_text
import pyttsx3
import os
import Constants


class Model:

    def extractTextFromTextFile(self, filePath):
        with open(filePath, "r") as file:
            return file.read()

    def extractTextFromPdf(self, filePath):
        """
        filepath: String

        returns: String
        """
        return extract_text(filePath)

    def saveMp3(self, textData, voice, rate, targetPath):
        """
        textData: String
        voice: String
        rate: int
        targetPath: String

        returns: void
        """
        engine = pyttsx3.init()

        engine.setProperty('voice', {
            Constants.FEMALE_VOICE: r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',
            Constants.MALE_VOICE: r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
        }[voice])

        engine.setProperty('rate', rate)

        engine.save_to_file(textData, targetPath)
        engine.runAndWait()

    def saveText(self, textData, targetPath):
        """
        textData: String
        targetPath: String

        returns: void
        """
        with open(targetPath, "w+") as file:
            file.write(textData)

    def playMp3(self, filePath):
        """
        filePath: String

        returns: void
        """
        os.startfile(filePath)
