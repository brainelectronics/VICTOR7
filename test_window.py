#!/usr/bin/python
# -*- coding: utf-8 -*-

# center.py

import wx
import wx.py

class Window(wx.Frame):
  
    def __init__(self, parent, title, size):
        super(Window, self).__init__(parent, title=title, 
            size=size)    #size=(300, 200)
        self.size = size
        #self.Centre()
        #self.Show()
        self.InitUI()

    def InitUI(self):    

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')

        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.theShell = wx.py.shell.Shell(self, pos=(0, 300), size=(200, 300), introText="Hello")
        # read about frames and split windows!


        
        wx.StaticText(self, label='Celsius: ', pos=(150, 150))
        self.sc = wx.SpinCtrl(self, value='0', pos=(150, 75), size=(60, -1))

        self.SetSize(self.size)
        #self.SetSize((600, 200))

        self.SetTitle('Simple menu')
        #self.Centre()
        self.Move((0, 25))
        self.Show(True)

    def OnQuit(self, e):
        self.Close()

def main():
    
    ex = wx.App()
    displaySize= wx.DisplaySize()   #(displaySize[0]/2, displaySize[1]/2)
    Window(None, title='Center', size=(displaySize[0]/2, displaySize[1]-100))
    ex.MainLoop()  

if __name__ == '__main__':
    main()
    """
    app = wx.App()
    Window(None, title='Center')
    app.MainLoop()
    """