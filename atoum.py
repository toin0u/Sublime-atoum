# MIT License**
#
# Copyright (c) 2012 Antoine Corcy, contact < at > sbin.dk
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
import sublime
import sublime_plugin
import os
import os.path
import subprocess

''' global vars '''
atoum = "atoum"
syntaxFile = "Packages/atoum/atoum.tmLanguage"
statusMessageFileTest = "Unit testing file [ %s ] with atoum..."
dialogMessageFileTest = "This is not a php file...\n\nAtoum is a unit test framework for php!\nVisit: http://atoum.org"
statusMessageDirectoryTest = "Unit testing directory [ %s ] with atoum..."
dialogMessageDirectoryTest = "Can't find any php file in this directory...\n\nAtoum is a unit test framework for php!\nVisit: http://atoum.org"


class AtoumCommand(object):
    def get_file(self):
        fileName, fileExtension = os.path.splitext(self.view.file_name())
        if(fileExtension == ".php"):
            return os.path.basename(self.view.file_name())
        else:
            return False

    def get_directory(self):
        phpFolder = os.path.dirname(self.view.file_name())
        for files in os.listdir(phpFolder):
            if files.endswith(".php"):
                return phpFolder
            else:
                return False

    def output_window(self, edit, result):
        scratch_file = sublime.active_window().new_file()
        scratch_file.set_name(atoum)
        scratch_file.set_scratch(True)
        scratch_file.insert(edit, 0, result)
        scratch_file.end_edit(edit)
        scratch_file.set_read_only(True)
        scratch_file.set_syntax_file(syntaxFile)

    def output_panel(self, edit, result):
        panel = self.view.window().get_output_panel(atoum)
        panel.set_read_only(False)
        edit = panel.begin_edit()
        panel.insert(edit, panel.size(), result)
        panel.end_edit(edit)
        panel.set_read_only(True)
        panel.set_syntax_file(syntaxFile)
        self.view.window().run_command("show_panel", {"panel": "output." + atoum})

    def execute(self, edit, command, useLightReport):
        if useLightReport:
            command = command + " -ulr"
        result, e = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd=self.get_directory()).communicate()
        if useLightReport:
            self.output_panel(edit, result)
        else:
            self.output_window(edit, result)


class AtoumTestFileCommand(AtoumCommand, sublime_plugin.TextCommand):
    def run(self, edit):
        if self.get_file():
            sublime.status_message(statusMessageFileTest % self.get_file())
            s = sublime.load_settings("atoum.sublime-settings")
            cmd = s.get("php_command") + " " + s.get("atoum_phar_file") + " -f " + self.get_directory() + "/" + self.get_file()
            self.execute(edit, cmd, s.get("use_light_report"))
        else:
            sublime.error_message(dialogMessageFileTest)
            return False


class AtoumTestDirectoryCommand(AtoumCommand, sublime_plugin.TextCommand):
    def run(self, edit):
        if self.get_directory():
            sublime.status_message(statusMessageDirectoryTest % self.get_directory())
            s = sublime.load_settings("atoum.sublime-settings")
            cmd = s.get("php_command") + " " + s.get("atoum_phar_file") + " -d " + self.get_directory()
            self.execute(edit, cmd, s.get("use_light_report"))
        else:
            sublime.error_message(dialogMessageDirectoryTest)
            return False
