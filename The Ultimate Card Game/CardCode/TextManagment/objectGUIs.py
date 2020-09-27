class textObject():
    def __init__(self,Text,Line:int,Offset=0):
        self.Text = str(Text)
        self.Line = Line
        self.Offset = Offset
    def __repr__(self):
        return "TextObject"

class dividerObject():
    def __init__(self,Line):
        self.Line = Line
    def __repr__(self):
        return "Divider"

class textPanel():
    def __init__(self, Width, Height):
        self.Width = Width
        self.Height = Height
        self.Contents = []

    def addObjects(self, Objects:list):
        for x in range(len(Objects)):
            self.Contents.append(Objects[x])

    def drawPanel(self, end="\n"):
        Stuff = self.Contents
        FinishedText = ""
        FinishedText += str("+"+"-"*self.Width+"+" + "\n")

        for y in range(self.Height):
            NoText = False
            for c in range(len(Stuff)):
                if(Stuff[c].Line == y):
                    if repr(Stuff[c]) == "TextObject":
                        FinishedText += "|" + str((" " * Stuff[c].Offset) + Stuff[c].Text + " " * ((self.Width - len(Stuff[c].Text) - Stuff[c].Offset ))) + "|\n"
                        NoText = True
                        break
                    elif repr(Stuff[c] == "Divider"):
                        FinishedText += "+" + "-"*self.Width + "+\n"
                        NoText = True


            if(NoText == False):
                FinishedText += "|" + str(" "*self.Width) + "|\n"

        FinishedText += str("+"+"-"*self.Width+"+" + str(end))
        return FinishedText
