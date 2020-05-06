import wx
import Fugle_GUI as gui

class MainFrame(gui.MyFrameFoedder):
    def __init__(self, parent):
        gui.MyFrameFoedder.__init__(self, parent)
    def ToQuestion2(self, event):
        gui.MyFrameNaeb.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame(parent=None)
    frame.Show()
    app.MainLoop()