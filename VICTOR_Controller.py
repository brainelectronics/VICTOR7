#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import wx
    #from wx import glcanvas
    import wx.py
    from wx import glcanvas
    from wx.lib.buttons import GenBitmapTextButton
    from OpenGL.GL import *
    from OpenGL.GLUT import *
    haveOpenGL = True
except ImportError:
    raise ImportError, "Required dependency not present"

class Example(wx.Panel):
    def __init__(self, parent, title, size):
        #super(Example, self).__init__(parent, title=title, size=size)
        wx.Panel.__init__(self, parent, -1)
        
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add((20, 30))

        self.size = size
        self.title = title

        self.email = None
        
        self.yUp = None #8
        self.aDown = None   #1
        self.xLeft = None   #4
        self.bRight = None  #2
        self.leftButton = None  #16
        self.rightButton = None #32

        self.theJoystick = wx.Joystick()
        self.theJoystick.SetCapture(self)

        self.Bind(wx.EVT_JOY_BUTTON_DOWN, self.OnButtonEnter)
        self.Bind(wx.EVT_JOY_BUTTON_UP, self.OnButtonLeave)
        
        self.InitUI()

        if 1:
            c = CubeCanvas(self)
            c.SetMinSize((100, 100))
            box.Add(c, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
    def InitUI(self):   
        print("Number of button: " + str(self.theJoystick.GetNumberButtons()))
        print("Number of axis: " + str(self.theJoystick.GetNumberAxes()))
        #print(self.joy.GetManufacturerId())

        pnl = wx.Panel(self)
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()    # create new Menu item
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        menubar.Append(fileMenu, '&File')

        imp = wx.Menu() # create new Menu item
        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)
        imp.Append(wx.ID_ANY, 'import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')

        help = wx.Menu()    # create new Menu item
        help.Append(100, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id=100)
        menubar.Append(help, '&Help')

        self.SetMenuBar(menubar)

        self.theShell = wx.py.shell.Shell(self, pos=(0, 300), size=(200, 300), introText="Hello")

        wx.StaticText(self, label='Convert Fahrenheit temperature to Celsius', 
            pos=(20,20))
        wx.StaticText(self, label='Fahrenheit: ', pos=(20, 80))
        wx.StaticText(self, label='Celsius: ', pos=(20, 150))
        
        self.celsius = wx.StaticText(self, label='', pos=(150, 150))
        self.sc = wx.SpinCtrl(self, value='0', pos=(150, 75), size=(60, -1))
        self.sc.SetRange(-459, 1000)
        
        btn = wx.Button(self, label='Compute', pos=(70, 230))
        btn.SetFocus()
        cbtn = wx.Button(self, label='Close', pos=(185, 230))

        btn.Bind(wx.EVT_BUTTON, self.OnCompute)
        cbtn.Bind(wx.EVT_BUTTON, self.OnQuit)

        self.yUp = GenBitmapTextButton(
            self, 1, 
            wx.Bitmap('Images/Pfeil Up.png'), '',
            (125, 300), 
            (90, 90))
        self.yUp.SetBezelWidth(1)

        self.aDown = GenBitmapTextButton(
            self, 1, 
            wx.Bitmap('Images/Pfeil Down.png'), '',
            (125, 500), 
            (90, 90))
        self.aDown.SetBezelWidth(1)

        self.bRight = GenBitmapTextButton(
            self, 1, 
            wx.Bitmap('Images/Pfeil Right.png'), '',
            (225, 400), 
            (90, 90))
        self.bRight.SetBezelWidth(1)

        self.xLeft = GenBitmapTextButton(
            self, 1, 
            wx.Bitmap('Images/Pfeil Left.png'), '',
            (25, 400), 
            (90, 90))
        self.xLeft.SetBezelWidth(1)

        self.aDown.Bind(wx.EVT_ENTER_WINDOW, self.OnButtonEnter)
        self.aDown.Bind(wx.EVT_LEAVE_WINDOW, self.OnButtonLeave)
        self.yUp.Bind(wx.EVT_ENTER_WINDOW, self.OnButtonEnter)
        self.yUp.Bind(wx.EVT_LEAVE_WINDOW, self.OnButtonLeave)
        self.bRight.Bind(wx.EVT_ENTER_WINDOW, self.OnButtonEnter)
        self.bRight.Bind(wx.EVT_LEAVE_WINDOW, self.OnButtonLeave)
        self.xLeft.Bind(wx.EVT_ENTER_WINDOW, self.OnButtonEnter)
        self.xLeft.Bind(wx.EVT_LEAVE_WINDOW, self.OnButtonLeave)
           
        self.SetSize(self.size)
        self.SetTitle(self.title)
        #self.Centre()
        self.Move((500, 25))
        self.Show(True)          
        
    def OnQuit(self, e):
        self.Close(True)

    def OnCompute(self, e):
        fahr = self.sc.GetValue()
        cels = round((fahr - 32) * 5 / 9.0, 2)
        self.celsius.SetLabel(str(cels))

    def OnButtonEnter(self, event):
        # obj =  event.GetEventObject()
        # obj.SetBackgroundColour('#ffdf85')
        # obj.Refresh()
        print self.theJoystick.GetButtonState()
        if self.theJoystick.GetButtonState() is 1:    
            self.aDown.SetBackgroundColour('#ffdf85')
            self.aDown.Refresh()

        elif self.theJoystick.GetButtonState() is 8:    
            self.yUp.SetBackgroundColour('#ffdf85')
            self.yUp.Refresh()

        elif self.theJoystick.GetButtonState() is 2:
            self.bRight.SetBackgroundColour('#ffdf85')
            self.bRight.Refresh()

        elif self.theJoystick.GetButtonState() is 4:
            self.xLeft.SetBackgroundColour('#ffdf85')
            self.xLeft.Refresh()

    def OnButtonLeave(self, event):
        # obj =  event.GetEventObject()
        # obj.SetBackgroundColour('#c2e6f8')
        # obj.Refresh()
        print self.theJoystick.GetButtonState()
        self.aDown.SetBackgroundColour('#c2e6f8')
        self.aDown.Refresh()
        self.yUp.SetBackgroundColour('#c2e6f8')
        self.yUp.Refresh()
        self.bRight.SetBackgroundColour('#c2e6f8')
        self.bRight.Refresh()
        self.xLeft.SetBackgroundColour('#c2e6f8')
        self.xLeft.Refresh()

    def OnAboutBox(self, e):
        
        description = '''VICTOR Contoller is'''

        """VICTOR Contoller is an advanced file manager for 
the Unix operating system. Features include powerful built-in editor, 
advanced search capabilities, powerful batch renaming, file comparison, 
extensive archive handling and more"""

        licence = '''VICTOR Contoller is free software; you can redistribute 
it and/or modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation; either version 2 of the License, 
or (at your option) any later version.

VICTOR Contoller is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details. You should have 
received a copy of the GNU General Public License along with VICTOR Contoller'''


        info = wx.AboutDialogInfo()

        #info.SetIcon(wx.Icon('brainelectronics Logo small.png', wx.BITMAP_TYPE_PNG))
        info.SetName('VICTOR Contoller')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2012 - 2015 Jonas Scharpf')
        info.SetWebSite('http://www.brainelectronics.de')
        info.SetLicence(licence)
        info.AddDeveloper('Jonas Scharpf')
        info.AddDocWriter('Jonas Scharpf')
        #info.AddArtist('The Tango crew')
        info.AddTranslator('Jonas Scharpf')

        wx.AboutBox(info)
                

class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)
        
        # initial mouse position
        self.lastx = self.x = 30
        self.lasty = self.y = 30
        self.size = None
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)


    def OnEraseBackground(self, event):
        pass # Do nothing, to avoid flashing on MSW.


    def OnSize(self, event):
        wx.CallAfter(self.DoSetViewport)
        event.Skip()

    def DoSetViewport(self):
        size = self.size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)
        


    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()


    def OnMouseDown(self, evt):
        self.CaptureMouse()
        self.x, self.y = self.lastx, self.lasty = evt.GetPosition()


    def OnMouseUp(self, evt):
        self.ReleaseMouse()


    def OnMouseMotion(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            self.lastx, self.lasty = self.x, self.y
            self.x, self.y = evt.GetPosition()
            self.Refresh(False)




class CubeCanvas(MyCanvasBase):
    def InitGL(self):
        # set viewing projection
        glMatrixMode(GL_PROJECTION)
        glFrustum(-0.5, 0.5, -0.5, 0.5, 1.0, 3.0)

        # position viewer
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -2.0)

        # position object
        glRotatef(self.y, 1.0, 0.0, 0.0)
        glRotatef(self.x, 0.0, 1.0, 0.0)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)


    def OnDraw(self):
        # clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # draw six faces of a cube
        glBegin(GL_QUADS)
        glNormal3f( 0.0, 0.0, 1.0)
        glVertex3f( 0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5,-0.5, 0.5)
        glVertex3f( 0.5,-0.5, 0.5)

        glNormal3f( 0.0, 0.0,-1.0)
        glVertex3f(-0.5,-0.5,-0.5)
        glVertex3f(-0.5, 0.5,-0.5)
        glVertex3f( 0.5, 0.5,-0.5)
        glVertex3f( 0.5,-0.5,-0.5)

        glNormal3f( 0.0, 1.0, 0.0)
        glVertex3f( 0.5, 0.5, 0.5)
        glVertex3f( 0.5, 0.5,-0.5)
        glVertex3f(-0.5, 0.5,-0.5)
        glVertex3f(-0.5, 0.5, 0.5)

        glNormal3f( 0.0,-1.0, 0.0)
        glVertex3f(-0.5,-0.5,-0.5)
        glVertex3f( 0.5,-0.5,-0.5)
        glVertex3f( 0.5,-0.5, 0.5)
        glVertex3f(-0.5,-0.5, 0.5)

        glNormal3f( 1.0, 0.0, 0.0)
        glVertex3f( 0.5, 0.5, 0.5)
        glVertex3f( 0.5,-0.5, 0.5)
        glVertex3f( 0.5,-0.5,-0.5)
        glVertex3f( 0.5, 0.5,-0.5)

        glNormal3f(-1.0, 0.0, 0.0)
        glVertex3f(-0.5,-0.5,-0.5)
        glVertex3f(-0.5,-0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5,-0.5)
        glEnd()

        if self.size is None:
            self.size = self.GetClientSize()
        w, h = self.size
        w = max(w, 1.0)
        h = max(h, 1.0)
        xScale = 180.0 / w
        yScale = 180.0 / h
        glRotatef((self.y - self.lasty) * yScale, 1.0, 0.0, 0.0);
        glRotatef((self.x - self.lastx) * xScale, 0.0, 1.0, 0.0);

        self.SwapBuffers()

def main():
    
    ex = wx.App()
    displaySize= wx.DisplaySize()
    Example(None, title='Center', size=(displaySize[0]/2, displaySize[1]-100))
    ex.MainLoop()    

if __name__ == '__main__':
    main() 