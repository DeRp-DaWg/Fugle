import wx
import Fugle_GUI as gui

class MainFrame(gui.MyFrameFoedder, gui.MyFrameNaeb):
    def __init__(self, parent):
        gui.MyFrameFoedder.__init__(self, parent)
        self.MyFrameNaeb = Naeb(self)
    def ToQuestion2(self, event):
        self.MyFrameNaeb.Show()
        self.Hide()
    

class Naeb(gui.MyFrameNaeb, gui.MyFrameStoerrelse):
    def __init__(self, parent):
        gui.MyFrameNaeb.__init__(self, parent)
        self.MyFrameStoerrelse = Størrelse(self)
    def ToQuestion3(self, event):
        self.MyFrameStoerrelse.Show()
        self.Hide()

class Størrelse(gui.MyFrameStoerrelse, gui.MyFrameFarver):
    def __init__(self, parent):
        gui.MyFrameStoerrelse.__init__(self, parent)
        self.MyFrameFarver = Farver(self)
    def ToQuestion4(self, event):
        self.MyFrameFarver.Show()
        self.Hide()

class Farver(gui.MyFrameFarver, gui.MyFrameMad):
    def __init__(self, parent):
        gui.MyFrameFarver.__init__(self, parent)
        self.MyFrameMad = Mad(self)
    def ToQuestion5(self, event):
        self.MyFrameMad.Show()
        self.Hide()

class Mad(gui.MyFrameMad, gui.MyFrameResults):
    def __init__(self, parent):
        gui.MyFrameMad.__init__(self, parent)
        self.MyFrameResults = Results(self)
    def ToResult(self, event):
        self.MyFrameResults.Show()
        self.Hide()


class Results(gui.MyFrameResults):
    def __init__(self, parent):
        gui.MyFrameResults.__init__(self, parent)


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame(parent=None)
    frame.Show()
    app.MainLoop()