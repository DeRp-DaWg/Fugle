import wx
import Fugle_GUI as gui
import sqlite3



app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()