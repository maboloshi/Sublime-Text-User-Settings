# coding=utf8

import sublime
import sublime_plugin
import os
import datetime

class CopyFilenameCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if len(self.view.file_name()) > 0:
			filename = os.path.basename(self.view.file_name())
			sublime.set_clipboard(filename)
			sublime.status_message("Copied file name: %s" % filename)

	def is_enabled(self):
		return self.view.file_name() is not None and len(self.view.file_name()) > 0

class AddCurrentTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("insert_snippet",
			{
			 	"contents": "%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			}
		)
