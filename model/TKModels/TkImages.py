from PIL import Image, ImageTk

class TkImages():

    def __init__(self):
        self.headerBkg: ImageTk = None
        self.logo: ImageTk = None
        self.rhodo: ImageTk = None
        self.rhodoBig: ImageTk = None
        self.showPassword: ImageTk = None
        self.hidePassword: ImageTk = None
        self.bin: ImageTk = None
        self.emptyPot: ImageTk = None
        self.fullPot: ImageTk = None
        self.potBkg: ImageTk = None
        self.potBkgBig: ImageTk = None
        self.loadContent()

    def loadContent(self):
        headerBkg = Image.open(r"./images/utilityImages/florabkg.jpg").resize((1505, 120), Image.ANTIALIAS)
        self.headerBkg = ImageTk.PhotoImage(headerBkg)

        logoImg = Image.open(r"./images/utilityImages/floraLogo.png").resize((100, 100))
        self.logo = ImageTk.PhotoImage(logoImg)

        picShow = Image.open(r"./images/utilityImages/show.png")
        self.showPassword = ImageTk.PhotoImage(picShow)

        picHide = Image.open(r"./images/utilityImages/hide.png")
        self.hidePassword = ImageTk.PhotoImage(picHide)

        bin = Image.open(r"./images/utilityImages/bin.png")
        self.bin = ImageTk.PhotoImage(bin)

        emptyPot = Image.open(r"./images/utilityImages/emptyPot.png")
        self.emptyPot = ImageTk.PhotoImage(emptyPot)

        fullPot = Image.open(r"./images/utilityImages/plantInPot.png")
        self.fullPot = ImageTk.PhotoImage(fullPot)

        potImg = Image.open(r"./images/utilityImages/potBkg.jpg").resize((150, 250))
        self.potBkg = ImageTk.PhotoImage(potImg)

        potImgBig = Image.open(r"./images/utilityImages/potBkg.jpg").resize((300, 300))
        self.potBkgBig = ImageTk.PhotoImage(potImgBig)