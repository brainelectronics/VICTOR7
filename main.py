#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
	import test_window as aWindow
	import VICTOR_Controller as Controller
	import wx
	from wx.lib.buttons import GenBitmapTextButton
except ImportError:
	raise ImportError, "Required dependency not present"

if __name__ == '__main__':
	ex = wx.App()
	displaySize= wx.DisplaySize()   #(displaySize[0]/2, displaySize[1]/2)
	aWindow.Window(None, title='Center', size=(displaySize[0]/2, displaySize[1]-100))
	Controller.Example(None, title='Center', size=(displaySize[0]/2, displaySize[1]-100))
	ex.MainLoop()