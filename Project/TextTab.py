import os
import textwrap
from tkinter import END, E, StringVar, W, filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText

from Controller import Controller
from Widgets import Widgets


class TextTab:
    def __init__(self, tabs):
        self.c = Controller()
        self.rightTabFrame = ttk.Frame(tabs)
        tabs.add(self.rightTabFrame, text="Text to MP3")

        self.w = Widgets(self.rightTabFrame)

        self.w.leftFrame.grid(row=0, column=0, sticky="n")
        self.w.rightFrame.grid(row=0, column=1)
        self.w.selectButton.grid(row=0, column=0, padx=5, pady=10)
        self.w.selectedFileDisplayLabel.grid(row=1, column=0, sticky="w")
        self.w.separatorAfterSelectedFileDisplayLabel.grid(
            row=2, column=0, sticky=(W, E), pady=(10, 0)
        )
        self.w.voiceHeadingLabel.grid(row=2, column=0, sticky="w", padx=5, pady=(10, 0))
        self.w.maleRadioButton.grid(row=3, column=0, sticky="w", padx=5)

        self.w.femaleRadioButton.grid(row=4, column=0, sticky="w", padx=5)
        self.w.separatorAfterFemaleRadioButton.grid(
            row=5, column=0, pady=(10, 0), sticky=(W, E)
        )
        self.w.speedHeadingLabel.grid(row=5, column=0, sticky="w", padx=5, pady=(10, 0))

        self.w.normalRadioButton.grid(row=6, column=0, sticky="w", padx=5)
        self.w.slowRadioButton.grid(row=7, column=0, sticky="w", padx=5)
        self.w.fastRadioButton.grid(row=8, column=0, sticky="w", padx=5)

        self.w.separatorAfterFastRadioButton.grid(
            row=9, column=0, sticky=(W, E), pady=(10, 0)
        )

        self.w.saveMp3Button.grid(row=10, column=0, sticky="w", padx=5, pady=(15, 0))

        self.w.saveTextButton.grid(row=11, column=0, sticky="w", padx=5, pady=(10, 0))

        self.w.playMp3Button.grid(row=12, column=0, sticky="w", padx=5, pady=(10, 15))

        # Commands for leftFrame buttons-------------------
        self.w.selectButton["command"] = self.selectText
        self.w.saveMp3Button["command"] = self.saveMp3
        self.w.saveTextButton["command"] = self.saveText
        self.w.playMp3Button["command"] = self.playMp3

        # check box for file select or text----------------
        self.checkBoxForSelectFileOrWriteTextVar = StringVar()
        self.checkBoxForSelectFileOrWriteTextVar.set(1)
        self.checkBoxForSelectFileOrWriteText = ttk.Checkbutton(
            self.w.rightFrame,
            text="From File",
            takefocus=False,
            variable=self.checkBoxForSelectFileOrWriteTextVar,
            command=self.fromFileOrText,
        )

        self.checkBoxForSelectFileOrWriteText.grid(row=0, column=0, sticky="w")

        # TextArea-----------------------------------------
        self.inputTextArea = ScrolledText(self.w.rightFrame)
        self.inputTextArea.grid(row=1, column=0)

        # clearButton style--------------------------------
        self.style = ttk.Style()
        self.style.configure("clearButton.TButton", font=("arial"))

        # clearButton--------------------------------------
        self.clearTextButton = ttk.Button(
            self.w.rightFrame,
            text="Clear Text",
            style="clearButton.TButton",
            command=self.clearTextConfirmAlertBox,
        )
        self.clearTextButton.grid(row=2, column=0, sticky="e", padx=5, pady=(10, 0))

        self.filePathList = []

    def fromFileOrText(self):
        if self.checkBoxForSelectFileOrWriteTextVar.get() == "1":
            self.w.selectButton["state"] = "!disabled"
            self.clearTextButton["state"] = "disabled"
            self.w.saveTextButton["state"] = "disabled"
            self.inputTextArea["state"] = "disabled"
            self.w.saveMp3Button["state"] = "disabled"
            self.w.playMp3Button["state"] = "disabled"

        else:
            self.w.selectButton["state"] = "disabled"
            self.inputTextArea["state"] = "normal"
            self.clearTextButton["state"] = "!disabled"
            self.w.saveMp3Button["state"] = "!disabled"
            self.w.playMp3Button["state"] = "!disabled"
            self.w.saveTextButton["state"] = "!disabled"

    def clearTextConfirmAlertBox(self):
        self.clearTextConfirmAlertBoxReply = messagebox.askquestion(
            "Confirm", "Are you sure you want to delete the text?"
        )
        if self.clearTextConfirmAlertBoxReply == "yes":
            self.inputTextArea.delete("0.0", END)

    def selectText(self):
        self.selectedTextFilePath = filedialog.askopenfilename(
            title="Select file", filetypes=(("Text files", "*.txt"),)
        )
        if self.selectedTextFilePath != "":
            self.filePathList.append(self.selectedTextFilePath)
            self.w.saveMp3Button["state"] = "!disabled"
            self.w.playMp3Button["state"] = "!disabled"
            self.w.selectedFileDisplayVar.set(
                textwrap.fill(os.path.basename(self.selectedTextFilePath), width=19)
            )
            self.filePathToSaveMp3 = ""
        else:
            if len(self.filePathList) == 0:
                pass
            else:
                self.w.saveMp3Button["state"] = "!disabled"
                self.w.playMp3Button["state"] = "!disabled"

    def saveMp3(self):
        if self.checkBoxForSelectFileOrWriteTextVar.get() == "1":
            self.filePathToSaveMp3 = filedialog.asksaveasfilename(
                filetypes=[("MP3 files", "*.mp3")],
                defaultextension=".mp3",
                initialfile="myfile",
            )
            self.infoToUserToWait()
            self.c.saveMp3FromTextFile(
                self.w.maleFemaleRadioButtonVar.get(),
                self.w.normalSlowFastRadioButtonVar.get(),
                self.selectedTextFilePath,
                self.filePathToSaveMp3,
            )
            self.infoToUserForFileSaved()
        else:
            self.filePathToSaveMp3 = filedialog.asksaveasfilename(
                filetypes=[("MP3 files", "*.mp3")],
                defaultextension=".mp3",
                initialfile="myfile",
            )
            self.infoToUserToWait()
            self.c.saveMp3FromInputText(
                self.w.maleFemaleRadioButtonVar.get(),
                self.w.normalSlowFastRadioButtonVar.get(),
                self.inputTextArea.get("1.0", END),
                self.filePathToSaveMp3,
            )
            self.infoToUserForFileSaved()

    def infoToUserToWait(self):
        messagebox.showinfo(
            "Information",
            f"Please wait while {os.path.basename(self.filePathToSaveMp3)} is being saved",
        )

    def infoToUserForFileSaved(self):
        messagebox.showinfo(
            "Information", f"{os.path.basename(self.filePathToSaveMp3)} saved!!!"
        )

    def saveText(self):
        self.filePathToSaveText = filedialog.asksaveasfilename(
            filetypes=[("TEXT files", "*.txt")],
            defaultextension=".txt",
            initialfile="myfile",
        )
        self.c.saveTextFromInput(
            self.inputTextArea.get("1.0", END), self.filePathToSaveText
        )

    def playMp3(self):
        self.c.playMp3(self.filePathToSaveMp3)

    # if (self.checkBoxForSelectFileOrWriteTextVar.get() == '0'):
    #     if (self.inputTextArea.get() == ''):
    #         self.w.saveMp3Button["state"] = "!disabled"
    #         self
