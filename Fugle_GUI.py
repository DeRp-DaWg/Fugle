# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrameFoedder
###########################################################################

class MyFrameFoedder ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerFoedder = wx.BoxSizer( wx.VERTICAL )

		self.m_staticFoedder = wx.StaticText( self, wx.ID_ANY, u"Hvordan ser fuglens fødder ud?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticFoedder.Wrap( -1 )

		bSizerFoedder.Add( self.m_staticFoedder, 0, wx.ALL, 5 )

		self.m_radioBtnKloeer = wx.RadioButton( self, wx.ID_ANY, u"Kløer", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFoedder.Add( self.m_radioBtnKloeer, 0, wx.ALL, 5 )

		self.m_radioBtnSvoemmefoedder = wx.RadioButton( self, wx.ID_ANY, u"Svømmefødder", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFoedder.Add( self.m_radioBtnSvoemmefoedder, 0, wx.ALL, 5 )

		self.m_buttonNext2 = wx.Button( self, wx.ID_ANY, u"Næste Spørgsmål", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFoedder.Add( self.m_buttonNext2, 0, wx.ALL, 5 )


		self.SetSizer( bSizerFoedder )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonNext2.Bind( wx.EVT_BUTTON, self.ToQuestion2 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ToQuestion2( self, event ):
		event.Skip()


###########################################################################
## Class MyFrameNaeb
###########################################################################

class MyFrameNaeb ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerNaeb = wx.BoxSizer( wx.VERTICAL )

		self.m_staticNaeb = wx.StaticText( self, wx.ID_ANY, u"Hvordan ser fuglen næb ud?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticNaeb.Wrap( -1 )

		bSizerNaeb.Add( self.m_staticNaeb, 0, wx.ALL, 5 )

		self.m_radioBtnNaeb = wx.RadioButton( self, wx.ID_ANY, u"Næb", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerNaeb.Add( self.m_radioBtnNaeb, 0, wx.ALL, 5 )

		self.m_radioBtnAndenaeb = wx.RadioButton( self, wx.ID_ANY, u"Andenæb", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerNaeb.Add( self.m_radioBtnAndenaeb, 0, wx.ALL, 5 )

		self.m_buttonNext3 = wx.Button( self, wx.ID_ANY, u"Næste Spørgsmål", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerNaeb.Add( self.m_buttonNext3, 0, wx.ALL, 5 )


		self.SetSizer( bSizerNaeb )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonNext3.Bind( wx.EVT_BUTTON, self.ToQuestion3 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ToQuestion3( self, event ):
		event.Skip()


###########################################################################
## Class MyFrameStoerrelse
###########################################################################

class MyFrameStoerrelse ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerStoerrelse = wx.BoxSizer( wx.VERTICAL )

		self.m_staticTextStoerrelse = wx.StaticText( self, wx.ID_ANY, u"Hvor stor er fuglen?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextStoerrelse.Wrap( -1 )

		bSizerStoerrelse.Add( self.m_staticTextStoerrelse, 0, wx.ALL, 5 )

		self.m_radioBtnStor = wx.RadioButton( self, wx.ID_ANY, u"Stor", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerStoerrelse.Add( self.m_radioBtnStor, 0, wx.ALL, 5 )

		self.m_radioBtnMellem = wx.RadioButton( self, wx.ID_ANY, u"Mellem", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerStoerrelse.Add( self.m_radioBtnMellem, 0, wx.ALL, 5 )

		self.m_radioBtnLille = wx.RadioButton( self, wx.ID_ANY, u"Lille", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerStoerrelse.Add( self.m_radioBtnLille, 0, wx.ALL, 5 )

		self.m_buttonNext4 = wx.Button( self, wx.ID_ANY, u"Næste Spørgsmål", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerStoerrelse.Add( self.m_buttonNext4, 0, wx.ALL, 5 )


		self.SetSizer( bSizerStoerrelse )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonNext4.Bind( wx.EVT_BUTTON, self.ToQuestion4 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ToQuestion4( self, event ):
		event.Skip()


###########################################################################
## Class MyFrameFarver
###########################################################################

class MyFrameFarver ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerFarver = wx.BoxSizer( wx.VERTICAL )

		self.m_staticTextFarver = wx.StaticText( self, wx.ID_ANY, u"Hvilke farver har fuglen?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextFarver.Wrap( -1 )

		bSizerFarver.Add( self.m_staticTextFarver, 0, wx.ALL, 5 )

		self.m_checkBoxBlaa = wx.CheckBox( self, wx.ID_ANY, u"Blå", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFarver.Add( self.m_checkBoxBlaa, 0, wx.ALL, 5 )

		self.m_checkBoxGul = wx.CheckBox( self, wx.ID_ANY, u"Gul", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFarver.Add( self.m_checkBoxGul, 0, wx.ALL, 5 )

		self.m_checkBoxSort = wx.CheckBox( self, wx.ID_ANY, u"Sort", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFarver.Add( self.m_checkBoxSort, 0, wx.ALL, 5 )

		self.m_checkBoxHvid = wx.CheckBox( self, wx.ID_ANY, u"Hvid", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFarver.Add( self.m_checkBoxHvid, 0, wx.ALL, 5 )

		self.m_checkBoxRoed = wx.CheckBox( self, wx.ID_ANY, u"Rød", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFarver.Add( self.m_checkBoxRoed, 0, wx.ALL, 5 )

		self.m_checkBoxBrun = wx.CheckBox( self, wx.ID_ANY, u"Brun", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFarver.Add( self.m_checkBoxBrun, 0, wx.ALL, 5 )

		self.m_checkBoxGraa = wx.CheckBox( self, wx.ID_ANY, u"Grå", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFarver.Add( self.m_checkBoxGraa, 0, wx.ALL, 5 )

		self.m_buttonNext5 = wx.Button( self, wx.ID_ANY, u"Næste Spørgsmål", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerFarver.Add( self.m_buttonNext5, 0, wx.ALL, 5 )


		self.SetSizer( bSizerFarver )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonNext5.Bind( wx.EVT_BUTTON, self.ToQuestion5 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ToQuestion5( self, event ):
		event.Skip()


###########################################################################
## Class MyFrameMad
###########################################################################

class MyFrameMad ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,750 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerMad = wx.BoxSizer( wx.VERTICAL )

		self.m_staticTextMad = wx.StaticText( self, wx.ID_ANY, u"Hvad spiser fuglen?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMad.Wrap( -1 )

		bSizerMad.Add( self.m_staticTextMad, 0, wx.ALL, 5 )

		self.m_checkBoxInsekter = wx.CheckBox( self, wx.ID_ANY, u"Insekter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxInsekter, 0, wx.ALL, 5 )

		self.m_checkBoxEdderkopper = wx.CheckBox( self, wx.ID_ANY, u"Edderkopper", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxEdderkopper, 0, wx.ALL, 5 )

		self.m_checkBoxFroe = wx.CheckBox( self, wx.ID_ANY, u"Frø", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxFroe, 0, wx.ALL, 5 )

		self.m_checkBoxVandplanter = wx.CheckBox( self, wx.ID_ANY, u"Vandplanter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxVandplanter, 0, wx.ALL, 5 )

		self.m_checkBoxBog = wx.CheckBox( self, wx.ID_ANY, u"Bog", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxBog, 0, wx.ALL, 5 )

		self.m_checkBoxSmaadyr = wx.CheckBox( self, wx.ID_ANY, u"Smådyr", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxSmaadyr, 0, wx.ALL, 5 )

		self.m_checkBoxPlantefroe = wx.CheckBox( self, wx.ID_ANY, u"Plantefrø", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxPlantefroe, 0, wx.ALL, 5 )

		self.m_checkBoxFisk = wx.CheckBox( self, wx.ID_ANY, u"Fisk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxFisk, 0, wx.ALL, 5 )

		self.m_checkBoxPlanter = wx.CheckBox( self, wx.ID_ANY, u"Planter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxPlanter, 0, wx.ALL, 5 )

		self.m_checkBoxMuslinger = wx.CheckBox( self, wx.ID_ANY, u"Muslinger", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxMuslinger, 0, wx.ALL, 5 )

		self.m_checkBoxSnegle = wx.CheckBox( self, wx.ID_ANY, u"Snegle", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxSnegle, 0, wx.ALL, 5 )

		self.m_checkBoxKrebsdyr = wx.CheckBox( self, wx.ID_ANY, u"Krebsdyr", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxKrebsdyr, 0, wx.ALL, 5 )

		self.m_checkBoxKorn = wx.CheckBox( self, wx.ID_ANY, u"Korn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxKorn, 0, wx.ALL, 5 )

		self.m_checkBoxBlade = wx.CheckBox( self, wx.ID_ANY, u"Blade", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxBlade, 0, wx.ALL, 5 )

		self.m_checkBoxRoedder = wx.CheckBox( self, wx.ID_ANY, u"Rødder", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxRoedder, 0, wx.ALL, 5 )

		self.m_checkBoxOrme = wx.CheckBox( self, wx.ID_ANY, u"Orme", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxOrme, 0, wx.ALL, 5 )

		self.m_checkBoxAadsler = wx.CheckBox( self, wx.ID_ANY, u"Ådsler", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxAadsler, 0, wx.ALL, 5 )

		self.m_checkBoxFugleunger = wx.CheckBox( self, wx.ID_ANY, u"Fugleunger", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxFugleunger, 0, wx.ALL, 5 )

		self.m_checkBoxSmaafisk = wx.CheckBox( self, wx.ID_ANY, u"Småfisk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxSmaafisk, 0, wx.ALL, 5 )

		self.m_checkBoxAffald = wx.CheckBox( self, wx.ID_ANY, u"Affald", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxAffald, 0, wx.ALL, 5 )

		self.m_checkBoxAeg = wx.CheckBox( self, wx.ID_ANY, u"Æg", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxAeg, 0, wx.ALL, 5 )

		self.m_checkBoxGraes = wx.CheckBox( self, wx.ID_ANY, u"Græs", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxGraes, 0, wx.ALL, 5 )

		self.m_checkBoxBaer = wx.CheckBox( self, wx.ID_ANY, u"Bær", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxBaer, 0, wx.ALL, 5 )

		self.m_checkBoxFrugt = wx.CheckBox( self, wx.ID_ANY, u"Frugt", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxFrugt, 0, wx.ALL, 5 )

		self.m_checkBoxPlantedele = wx.CheckBox( self, wx.ID_ANY, u"Plantedele", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxPlantedele, 0, wx.ALL, 5 )

		self.m_checkBoxAltaedende = wx.CheckBox( self, wx.ID_ANY, u"Altædende", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_checkBoxAltaedende, 0, wx.ALL, 5 )

		self.m_buttonNextResults = wx.Button( self, wx.ID_ANY, u"Resultater", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMad.Add( self.m_buttonNextResults, 0, wx.ALL, 5 )


		self.SetSizer( bSizerMad )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonNextResults.Bind( wx.EVT_BUTTON, self.ToResult )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ToResult( self, event ):
		event.Skip()


###########################################################################
## Class MyFrameResults
###########################################################################

class MyFrameResults ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerResults = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmapFugl = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerResults.Add( self.m_bitmapFugl, 0, wx.ALL, 5 )


		self.SetSizer( bSizerResults )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


