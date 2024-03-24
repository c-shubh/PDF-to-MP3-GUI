from tkinter import IntVar, StringVar, ttk

import Constants


class Widgets:
    def __init__(self, tabFrame):

        s = ttk.Style()
        s.configure("all.TButton", font=("arial", 15))
        # this style is applied only to 2 labels
        s.configure("all.TLabel", font=("arial", 10))
        s.configure("two.TLabel", font=("arial", 18, "bold"))
        s.configure("all.TRadiobutton", font=("arial", 15))

        self.tabFrame = tabFrame

        self.leftFrame = ttk.Frame(tabFrame, borderwidth=1, relief="groove")
        self.rightFrame = ttk.Frame(tabFrame, borderwidth=1, relief="groove")

        self.selectButton = ttk.Button(
            self.leftFrame, text="Select File", style="all.TButton"
        )

        self.selectedFileDisplayVar = StringVar()
        self.selectedFileDisplayLabel = ttk.Label(
            self.leftFrame,
            textvariable=self.selectedFileDisplayVar,
            style="all.TLabel",
            wraplength=500,
        )

        self.separatorAfterSelectedFileDisplayLabel = ttk.Separator(self.leftFrame)

        self.voiceHeadingLabel = ttk.Label(
            self.leftFrame, text="Voice:", style="two.TLabel"
        )

        self.maleFemaleRadioButtonVar = IntVar()
        self.maleFemaleRadioButtonVar.set(Constants.FEMALE_VOICE)

        self.maleRadioButton = ttk.Radiobutton(
            self.leftFrame,
            text="Male",
            variable=self.maleFemaleRadioButtonVar,
            value=Constants.MALE_VOICE,
            style="all.TRadiobutton",
        )
        self.femaleRadioButton = ttk.Radiobutton(
            self.leftFrame,
            text="Female",
            variable=self.maleFemaleRadioButtonVar,
            value=Constants.FEMALE_VOICE,
            style="all.TRadiobutton",
        )

        self.separatorAfterFemaleRadioButton = ttk.Separator(self.leftFrame)

        self.speedHeadingLabel = ttk.Label(
            self.leftFrame, text="Speed:", style="two.TLabel"
        )

        self.normalSlowFastRadioButtonVar = IntVar()
        self.normalSlowFastRadioButtonVar.set(Constants.NORMAL_SPEED)

        self.normalRadioButton = ttk.Radiobutton(
            self.leftFrame,
            text="Normal",
            variable=self.normalSlowFastRadioButtonVar,
            value=Constants.NORMAL_SPEED,
            style="all.TRadiobutton",
        )
        self.slowRadioButton = ttk.Radiobutton(
            self.leftFrame,
            text="Slow",
            variable=self.normalSlowFastRadioButtonVar,
            value=Constants.SLOW_SPEED,
            style="all.TRadiobutton",
        )
        self.fastRadioButton = ttk.Radiobutton(
            self.leftFrame,
            text="Fast",
            variable=self.normalSlowFastRadioButtonVar,
            value=Constants.FAST_SPEED,
            style="all.TRadiobutton",
        )

        self.separatorAfterFastRadioButton = ttk.Separator(self.leftFrame)

        self.saveMp3Button = ttk.Button(
            self.leftFrame, text="Save MP3", style="all.TButton", state="disabled"
        )

        self.saveTextButton = ttk.Button(
            self.leftFrame, text="Save Text", style="all.TButton", state="disabled"
        )

        self.playMp3Button = ttk.Button(
            self.leftFrame, text="Play MP3", style="all.TButton", state="disabled"
        )
