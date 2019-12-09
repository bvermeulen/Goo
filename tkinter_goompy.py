'''
Example of using GooMPy with Tkinter

Copyright (C) 2015 Alec Singer and Simon D. Levy

This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with this code.  If not, see <http://www.gnu.org/licenses/>.

Updated by Bruno Vermeulen @2019
'''
import tkinter as tk
from PIL import ImageTk
from goompy import GooMPy

WIDTH = 640
HEIGHT = 640

# LATITUDE = 13.8135822
# LONGITUDE = 99.7146769
# LATITUDE = -33.8566
# LONGITUDE = 151.2153
LATITUDE = -34.6246
LONGITUDE = -58.4017

ZOOM = 15
MAPTYPE = 'roadmap'


class UI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry('%dx%d+500+500' % (WIDTH, HEIGHT))
        self.title('GooMPy')

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)

        self.canvas.pack()

        self.bind("<Key>", self.check_quit)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<Button-1>', self.click)

        self.label = tk.Label(self.canvas)

        self.radiogroup = tk.Frame(self.canvas)
        self.radiovar = tk.IntVar()
        self.maptypes = ['roadmap', 'terrain', 'satellite', 'hybrid']
        self.add_radio_button('Road Map', 0)
        self.add_radio_button('Terrain', 1)
        self.add_radio_button('Satellite', 2)
        self.add_radio_button('Hybrid', 3)

        self.zoom_in_button = self.add_zoom_button('+', +1)
        self.zoom_out_button = self.add_zoom_button('-', -1)

        self.zoomlevel = ZOOM

        maptype_index = 0
        self.radiovar.set(maptype_index)

        self.goompy = GooMPy(
            WIDTH, HEIGHT, LATITUDE, LONGITUDE, ZOOM, MAPTYPE, radius_meters=None)

        self.goompy.use_map_type(MAPTYPE)
        self.redraw()

    def add_zoom_button(self, text, sign):
        button = tk.Button(
            self.canvas, text=text, width=1, command=lambda: self.zoom(sign))
        return button

    def reload(self):
        self.coords = None
        self.redraw()

    def set_cursor_to_normal(self):
        self.config(cursor='')
        self.update_idletasks()

    def set_cursor_to_wait(self):
        # A little trick to get a watch cursor along with loading
        self.config(cursor='watch')
        self.update_idletasks()

    def add_radio_button(self, _, index):
        maptype = self.maptypes[index]
        tk.Radiobutton(self.radiogroup, text=maptype, variable=self.radiovar, value=index,
                       command=lambda: self.usemap(maptype)).grid(row=0, column=index)

    def click(self, event):
        self.coords = event.x, event.y
        lon = self.goompy.get_lon_from_x(event.x)
        lat = self.goompy.get_lat_from_y(event.y)
        print(f'(x, y): {self.coords} '
              f'(lon, lat): ({lon:0.4f}, {lat:0.4f})')

    def drag(self, event):
        self.goompy.move(self.coords[0] - event.x, self.coords[1] - event.y)
        self.image = self.goompy.get_image()
        self.redraw()
        self.coords = event.x, event.y

    def redraw(self):
        self.image = self.goompy.get_image()
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.label['image'] = self.image_tk

        self.label.place(x=0, y=0, width=WIDTH, height=HEIGHT)

        self.radiogroup.place(x=0, y=0)

        x = int(self.canvas['width']) - 50
        y = int(self.canvas['height']) - 80

        self.zoom_in_button.place(x=x, y=y)
        self.zoom_out_button.place(x=x, y=y + 30)

    def usemap(self, maptype):
        self.set_cursor_to_wait()
        self.goompy.use_map_type(maptype)
        self.set_cursor_to_normal()
        self.redraw()

    def zoom(self, sign):
        self.set_cursor_to_wait()
        newlevel = self.zoomlevel + sign
        if 0 < newlevel < 22:
            self.zoomlevel = newlevel
            self.goompy.use_zoom(newlevel)
            self.redraw()

        self.set_cursor_to_normal()

    def check_quit(self, event):
        if ord(event.char) == 27:  # ESC
            exit(0)


if __name__ == '__main__':
    UI().mainloop()
