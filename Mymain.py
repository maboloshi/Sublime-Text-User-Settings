# coding=utf8

import sublime
import sublime_plugin
import os

class CopyFilenameCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if len(self.view.file_name()) > 0:
			filename = os.path.basename(self.view.file_name())
			sublime.set_clipboard(filename)
			sublime.status_message("Copied file name: %s" % filename)

	def is_enabled(self):
		return self.view.file_name() is not None and len(self.view.file_name()) > 0

