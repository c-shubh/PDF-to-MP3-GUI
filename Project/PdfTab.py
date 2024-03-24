import os
import textwrap
from tkinter import E, W, filedialog, messagebox, ttk

from Controller import Controller
from PdfViewer import PdfViewer
from Widgets import Widgets


class PdfTab:
    def __init__(self, tabs):
        self.c = Controller()

        self.leftTabFrame = ttk.Frame(tabs)
        tabs.add(self.leftTabFrame, text="PDF to MP3")

        self.w = Widgets(self.leftTabFrame)

        self.pdfViewer = PdfViewer(self.w.rightFrame)

        self.w.leftFrame.pack(side="left", anchor="nw")
        self.w.rightFrame.pack()

        # self.w.leftFrame.grid(row=0, column=0, sticky='n')
        # self.w.rightFrame.grid(row=0, column=1)
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

        self.w.selectButton["command"] = self.selectPdf
        self.w.saveMp3Button["command"] = self.saveMp3
        self.w.saveTextButton["command"] = self.saveText
        self.w.playMp3Button["command"] = self.playMp3

        self.filePathList = []

        self.pdfViewer.imageHolder.bind(
            "<Button-1>", lambda event: self.pdfViewer.parent.focus_set()
        )

    def selectPdf(self):
        self.selectedPdfPath = filedialog.askopenfilename(
            title="Select file", filetypes=(("PDF files", "*.pdf"),)
        )
        if self.selectedPdfPath != "":

            self.pdfViewer.showPdf(self.selectedPdfPath)

            self.filePathList.append(self.selectedPdfPath)
            self.toggleState(
                "!disabled",
                self.w.saveMp3Button,
                self.w.saveTextButton,
                self.w.playMp3Button,
            )
            self.w.selectedFileDisplayVar.set(
                textwrap.fill(os.path.basename(self.selectedPdfPath), width=19)
            )
            self.filePathToSaveMp3 = ""

        else:
            if len(self.filePathList) == 0:
                pass
            else:
                self.selectedPdfPath = self.filePathList[-1]
                self.toggleState(
                    "!disabled",
                    self.w.saveMp3Button,
                    self.w.saveTextButton,
                    self.w.playMp3Button,
                )

    def saveMp3(self):
        self.filePathToSaveMp3 = filedialog.asksaveasfilename(
            filetypes=[("MP3 files", "*.mp3")],
            defaultextension=".mp3",
            initialfile="myfile",
        )
        if self.filePathToSaveMp3 != "":
            messagebox.showinfo(
                "Information",
                f"Please wait while {os.path.basename(self.filePathToSaveMp3)} is being saved",
            )
            self.c.saveMp3FromPdf(
                self.w.maleFemaleRadioButtonVar.get(),
                self.w.normalSlowFastRadioButtonVar.get(),
                self.selectedPdfPath,
                self.filePathToSaveMp3,
            )
            messagebox.showinfo(
                "Information", f"{os.path.basename(self.filePathToSaveMp3)} saved!!!"
            )

    def saveText(self):
        self.filePathToSaveText = filedialog.asksaveasfilename(
            filetypes=[("TEXT files", "*.txt")],
            defaultextension=".txt",
            initialfile="myfile",
        )
        if self.filePathToSaveText != "":
            messagebox.showinfo(
                "Information",
                f"Please wait while {os.path.basename(self.filePathToSaveText)} is being saved",
            )
            self.c.saveTextFromPdf(self.selectedPdfPath, self.filePathToSaveText)
            messagebox.showinfo(
                "Information", f"{os.path.basename(self.filePathToSaveText)} saved!!!"
            )

    def playMp3(self):
        self.c.playMp3(self.filePathToSaveMp3)

    def toggleState(self, state, *args):
        if state in ("disabled", "!disabled"):
            for ele in args:
                ele["state"] = state
