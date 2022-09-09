class Utils:

    @staticmethod
    def showOrHidePassword(widget, button, model):
        if widget.cget('show') == '*':
            widget.config(show="")
            button.config(image=model.showPassword)
        else:
            widget.config(show="*")
            button.config(image=model.hidePassword)

    @staticmethod
    def deleteFromEntry(buttonClicked, value):
        if buttonClicked == 1:
            value.set("")
        if buttonClicked == 2:
            value.set("")
        if buttonClicked == 3:
            value.set("")
        if buttonClicked == 4:
            value.set("")
        if buttonClicked == 5:
            value.set("")
        if buttonClicked == 6:
            value.set("")