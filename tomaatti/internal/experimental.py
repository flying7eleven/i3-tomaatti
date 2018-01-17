# Copyright (C) 2017 - 2018 Tim Hütz
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.


class ScreenOverlay(object):
	def is_coposite_manager_running(self):
		from subprocess import Popen, PIPE
		child = Popen(['pgrep', 'xcompmgr'], stdout=PIPE)
		child.communicate()
		if 0 == child.returncode:
			return True
		else:
			return False

	def show_overlay(self):
		from tkinter import Canvas, Tk

		vw, vh = 600, 350

		self.root = Tk()
		self.w = Canvas(width=vw, height=vh, highlightthickness=0)
		self.w.configure(background='black')
		self.w.master.overrideredirect(True)
		self.w.master.geometry('+0+0')
		self.w.master.lift()
		self.w.master.wm_attributes('-topmost', True)
		self.w.master.wm_attributes('-fullscreen', True)
		self.w.master.wm_attributes('-zoomed', True)
		self.w.master.wm_attributes('-alpha', 0.5)
		self.w.create_rectangle(0, 0, vw, vh, fill='black')
		self.w.bind('<Button-1>', self._close_callback)
		self.w.pack()
		self.w.mainloop()

	def _close_callback(self, event):
		self.root.destroy()
