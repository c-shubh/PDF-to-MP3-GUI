import os
from tkinter import CENTER, LEFT, RIGHT, SOLID, VERTICAL, Canvas, X, Y, ttk

import fitz
from PIL import Image, ImageTk


class PdfViewer:
    def __init__(self, parent):
        self.parent = parent
        self.currentPageNum = 0

        # GUI
        """
        self.parent
            |---> self.mainContainerFrame
                    |---> self.navigationFrame
                            |---> self.fileNameLabel
                            |---> self.frameWithNavigationButtons
                                    |---> self.leftButton
                                    |---> self.pageNumberLabel
                                    |---> self.rightButton
                    |---> self.viewerFrame
                            |---> self.verticalScrollbar
                            |---> self.canvas
                                    |---> self.frameInCanvas
                                            |---> self.imageHolder
        """

        self.mainContainerFrame = ttk.Frame(self.parent)

        self.navigationFrame = ttk.Frame(self.mainContainerFrame)
        self.navigationFrame.pack(fill=X)
        self.viewerFrame = ttk.Frame(self.mainContainerFrame)
        self.viewerFrame.pack()
        self.fileNameLabel = ttk.Label(self.navigationFrame)
        self.fileNameLabel.pack(side=LEFT)
        self.frameWithNavigationButtons = ttk.Frame(self.navigationFrame)
        self.frameWithNavigationButtons.pack(side=RIGHT)
        self.leftButton = ttk.Button(
            self.frameWithNavigationButtons,
            text="🡸",
            takefocus=False,
            command=lambda: self.showPreviousPage(None),
        )
        self.leftButton.pack(side=LEFT)
        self.pageNumberLabel = ttk.Label(
            self.frameWithNavigationButtons, anchor=CENTER, width=8
        )
        self.pageNumberLabel.pack(side=LEFT)
        self.rightButton = ttk.Button(
            self.frameWithNavigationButtons,
            text="🡺",
            takefocus=False,
            command=lambda: self.showNextPage(None),
        )
        self.rightButton.pack(side=LEFT)

        self.isInitiallyHidden = True
        self.canvas = Canvas(self.viewerFrame)
        self.verticalScrollbar = ttk.Scrollbar(self.viewerFrame, orient=VERTICAL)
        self.verticalScrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.verticalScrollbar.set)
        self.verticalScrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT)

        self.frameInCanvas = ttk.Frame(self.canvas)

        self.canvas.create_window((0, 0), window=self.frameInCanvas, anchor="nw")

        self.frameInCanvas.bind(
            "<Configure>",
            lambda event, canvas=self.canvas: canvas.configure(
                scrollregion=canvas.bbox("all")
            ),
        )

        self.imageHolder = ttk.Label(self.frameInCanvas, border=1, relief=SOLID)
        self.imageHolder.pack()

        self.parent.focus_set()
        self.parent.bind("<Left>", self.showPreviousPage)
        self.parent.bind("<Prior>", self.showPreviousPage)

        self.parent.bind("<Right>", self.showNextPage)
        self.parent.bind("<Next>", self.showNextPage)

        self.parent.bind("<Home>", self.showFirstPage)
        self.parent.bind("<End>", self.showLastPage)

    def toPhotoImage(self, page):
        return ImageTk.PhotoImage(self.pageToImage(page))

    def pageToImage(self, page):
        pix = page.get_pixmap()
        # set the mode depending on alpha
        mode = "RGBA" if pix.alpha else "RGB"
        img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        return img

    def show(self):
        image = self.toPhotoImage(self.document.load_page(self.currentPageNum))
        self.imageHolder.configure(image=image)
        self.imageHolder.image = image

        self.pageNumberLabel.config(text=str(self.currentPageNum + 1))

    def showPdf(self, filePath):
        self.filePath = filePath
        self.document = fitz.open(self.filePath)
        self.lastPageNumber = self.document.page_count - 1
        width, height = self.pageToImage(self.document.load_page(0)).size
        if self.isInitiallyHidden:
            self.mainContainerFrame.pack()
            self.isInitiallyHidden = False
        self.canvas.configure(width=width, height=height)
        self.canvas.configure(scrollregion=(0, 0, 0, height))
        fileName = " " * 3 + os.path.splitext(os.path.split(self.filePath)[1])[0]
        self.fileNameLabel.config(
            text=f"{fileName[:50]}..." if len(fileName) > 50 else fileName
        )
        self.show()

    def showNextPage(self, event):
        self.currentPageNum += 1
        if self.currentPageNum > self.lastPageNumber:
            self.currentPageNum = self.lastPageNumber
        else:
            self.show()

    def showPreviousPage(self, event):
        self.currentPageNum -= 1
        if self.currentPageNum < 0:
            self.currentPageNum = 0
        else:
            self.show()

    def showFirstPage(self, event):
        self.currentPageNum = 0
        self.show()

    def showLastPage(self, event):
        self.currentPageNum = self.lastPageNumber
        self.show()
