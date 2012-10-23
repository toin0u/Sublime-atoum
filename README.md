# Sublime Text 2 atoum Plugin

[![project status](http://stillmaintained.com/toin0u/Sublime-atoum.png)](http://stillmaintained.com/toin0u/Sublime-atoum)

A simple plugin to test php files with atoum like the [vim-plugin](https://github.com/mageekguy/atoum/wiki/atoum-et-VIM).

## Install

First of all, you need [atoum](https://github.com/mageekguy/atoum).

Intall the [PHAR file](http://downloads.atoum.org/nightly/mageekguy.atoum.phar) in for instance `/usr/local/bin`.

Finally, install the plugin with the [Sublime Package Control](http://wbond.net/sublime_packages/package_control)

## Screenshot

Result in a tab:

!['A simple Sublime Text 2 plugin for atoum, unit testing framework for php'](http://i.imgur.com/0dUgW.png)

Result in a panel

!['A simple Sublime Text 2 plugin for atoum, unit testing framework for php'](http://i.imgur.com/0R2QD.png)

## Config

Change `atoum.sublime-settings` with your parameters which is accessible via the command panel, menu or the context menu. Changes are taken immediately.

You can activate the **light report** which will be shown in a **panel** not a tab.

```
{
    "php_command": "/opt/local/bin/php",
    "atoum_phar_file": "/usr/local/bin/mageekguy.atoum.phar",
    "use_light_report": true
}
```

## Usage

Default shorcuts are:

* `cmd+alt+s` on OSX or `ctrl+alt+a` on Linux and Windows: Test the current file
* `cmd+alt+d` on OSX or `ctrl+alt+d` on Linux and Windows: Test files in the current directory

## Diverse

Tested only on Mac OS X for the moment. [Read more on my blog](http://sbin.dk/2012/05/19/atoum-sublime-text-2-plugin/).

## License

All of Sublime Text 2 Atoum Plugin is licensed under the MIT license.

Copyright (c) 2012 Antoine Corcy, contact < at > sbin.dk

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.