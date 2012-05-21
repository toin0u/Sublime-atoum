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
syntax_file = "Packages/atoum/atoum.tmLanguage"

''' get configuration vars '''
s = sublime.load_settings("atoum.sublime-settings")
php_command = s.get("php_command")
atoum_phar_file = s.get("atoum_phar_file")
use_light_report = s.get("use_light_report")
command = php_command + " " + atoum_phar_file


class AtoumCommand(object):
    def get_file(self):
        return os.path.basename(self.view.file_name())

    def get_directory(self):
        return os.path.dirname(self.view.file_name())

    def output_window(self, edit, result):
        scratch_file = sublime.active_window().new_file()
        scratch_file.set_name(atoum)
        scratch_file.set_scratch(True)
        scratch_file.insert(edit, 0, result)
        scratch_file.end_edit(edit)
        scratch_file.set_read_only(True)
        scratch_file.set_syntax_file(syntax_file)

    def output_panel(self, edit, result):
        panel = self.view.window().get_output_panel(atoum)
        panel.set_read_only(False)
        edit = panel.begin_edit()
        panel.insert(edit, panel.size(), result)
        panel.end_edit(edit)
        panel.set_read_only(True)
        panel.set_syntax_file(syntax_file)
        self.view.window().run_command("show_panel", {"panel": "output." + atoum})

    def execute(self, edit, command):
        if use_light_report:
            command = command + " -ulr"
        result, e = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd=self.get_directory()).communicate()
        if use_light_report:
            self.output_panel(edit, result)
        else:
            self.output_window(edit, result)


class AtoumTestFileCommand(AtoumCommand, sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.status_message("Testing: %s" % self.get_file())
        cmd = command + " -f " + self.get_directory() + "/" + self.get_file()
        self.execute(edit, cmd)


class AtoumTestDirectoryCommand(AtoumCommand, sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.status_message("Testing: %s" % self.get_directory())
        cmd = command + " -d " + self.get_directory()
        self.execute(edit, cmd)


class AtoumHelpCommand(AtoumCommand, sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.status_message("Opening help page")
        cmd = command + " --help"
        self.execute(edit, cmd)
