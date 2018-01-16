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
	@staticmethod
	def show_overlay():
		from tkinter import Canvas

		vsize = vw, vh = 600, 350

		w = Canvas(width=vw, height=vh, highlightthickness=0)
		w.configure(background='black')
		w.master.overrideredirect(True)
		w.master.geometry('+0+0')
		w.master.lift()
		w.master.wm_attributes('-topmost', True)
		w.master.wm_attributes('-alpha', 0.5)
		w.create_rectangle(0, 0, vw, vh, fill='black')
		w.pack()
		w.mainloop()
