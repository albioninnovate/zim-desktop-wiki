# -*- coding: utf8 -*-

# Copyright 2008 Jaap Karssenberg <pardus@cpan.org>

'''FIXME'''

import gtk
from zim.gui import Dialog

class ExportDialog(Dialog):
	'''FIXME'''

	def __init__(self, ui):
		Dialog.__init__(self, ui, 'Export')
		self.vbox.add(gtk.Label('TODO'))

	def do_response_ok(self):
		return True
