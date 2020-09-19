# coding=utf8

import sublime
import sublime_plugin
import os
from datetime import datetime
from subprocess import Popen


# 复制当前文件的文件名
class CopyFilenameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            filename = os.path.basename(self.view.file_name())
            sublime.set_clipboard(filename)
            sublime.status_message("Copied file name: %s" % filename)

    def is_enabled(self):
        return self.view.file_name() is not None and len(self.view.file_name()) > 0


# 复制当前文件所在文件夹路径
class CopyDirectorynameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            dir_name = os.path.dirname(self.view.file_name())
            sublime.set_clipboard(dir_name)
            sublime.status_message("Copied file directory: %s" % dir_name)

    def is_enabled(self):
        return self.view.file_name() is not None and len(self.view.file_name()) > 0


# 在当前位置插入时间
class AddCurrentTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", {
            "contents": "%s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })


class ReadOnlyStatusListener(sublime_plugin.EventListener):
    # 当载入只读文档时，在状态栏显示"【只读】"标识
    def on_load_async(self, view):
        if view.is_read_only():
            view.set_status("file_status", "【只读】")
            # view.window().status_message('注意：文件 '+ view.file_name() + ' 只读')


class ToggleReadOnlyStatusCommand(sublime_plugin.TextCommand):
    # 对当前文件设置或取消只读, 并在状态栏显示或销毁'只读'标识
    def run(self, edit):
        if self.view.is_read_only():
            # 取消只读
            self.view.set_read_only(False)
            # 毁掉状态栏'只读'标识
            self.view.erase_status("file_status")
            # 状态栏提示
            # sublime.status_message("File unlocked!!")
        else:
            # 设置只读
            self.view.set_read_only(True)
            # 设置状态栏'只读'标识
            self.view.set_status("file_status", '【只读】')
            # sublime.status_message("File is locked!!")

    def is_checked(self):
        return self.view.is_read_only()


# 使用外部工具(默认)打开
class OpenFileWithExternalToolCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        if len(self.view.file_name()) > 0:
            file = self.view.file_name()
            if sublime.platform() == "osx":
                if args['app'] is None:
                    Popen(['open', file])
                else:
                    Popen(['open', '-a', args['app'], file])
            elif sublime.platform() == "windows":
                os.startfile(file)
            elif sublime.platform() == "linux":
                Popen(['xdg-open', file])

    def is_enabled(self):
        return True
