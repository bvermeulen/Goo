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
MAX_SYMBOL_SIZE = 100
DEFAULT_SYMBOL_SIZE = 7

LATITUDE = 13.8135822
LONGITUDE = 99.7146769
# LATITUDE = -33.8566
# LONGITUDE = 151.2153
# LATITUDE = 0
# LONGITUDE = 0

ZOOM = 10
MAPTYPE = 'roadmap'


class UI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry(f'{WIDTH}x{HEIGHT}')
        self.title('GooMPy')

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill='both')

        self.bind("<Key>", self.check_quit)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<Button-1>', self.click)

        self.radiogroup = tk.Frame(self.canvas)
        self.radiovar = tk.IntVar()
        self.maptypes = ['roadmap', 'terrain', 'satellite', 'hybrid']
        self.add_radio_button(0)
        self.add_radio_button(1)
        self.add_radio_button(2)
        self.add_radio_button(3)

        self.zoom_in_button = self.add_zoom_button('+', +1)
        self.zoom_out_button = self.add_zoom_button('-', -1)

        self.zoomlevel = ZOOM
        self.radiovar.set(0)

        self.goompy = GooMPy(
            WIDTH, HEIGHT, LATITUDE, LONGITUDE, ZOOM, radius_meters=50_000)

        self.goompy.use_map_type(MAPTYPE)
        self.redraw()

    def add_zoom_button(self, text, sign):
        button = tk.Button(
            self.canvas, text=text, width=1, command=lambda: self.zoom(sign))
        return button

    def set_cursor_to_normal(self):
        self.config(cursor='')
        self.update_idletasks()

    def set_cursor_to_wait(self):
        # A little trick to get a watch cursor along with loading
        self.config(cursor='watch')
        self.update_idletasks()

    def add_radio_button(self, index):
        maptype = self.maptypes[index]
        tk.Radiobutton(self.radiogroup, text=maptype, variable=self.radiovar, value=index,
                       command=lambda: self.usemap(maptype)).grid(row=0, column=index)

    def click(self, event):
        self.coords = event.x, event.y
        lon = self.goompy.get_lon_from_x(self.coords[0])
        lat = self.goompy.get_lat_from_y(self.coords[1])

        # TODO debug print statement
        print(f'x: {self.coords[0]}, y: {self.coords[1]} '
              f'lon: {lon:.4f}, lat: {lat:.4f}')

    def drag(self, event):
        self.goompy.move(self.coords[0] - event.x, self.coords[1] - event.y)
        self.redraw()
        self.coords = event.x, event.y

    def redraw(self):
        # clear the canvas
        self.canvas.delete('all')

        image = self.goompy.get_image()
        self.my_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.my_image, anchor='nw')

        self.radiogroup.place(x=0, y=0)

        x = int(self.canvas['width']) - 50
        y = int(self.canvas['height']) - 80
        self.zoom_in_button.place(x=x, y=y)
        self.zoom_out_button.place(x=x, y=y + 30)

        self.draw_point(LATITUDE, LONGITUDE, fill='blue')

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

    def draw_point(self, lat, lon, size=None, **kwargs):
        x = self.goompy.get_xwin_from_lon(lon)
        y = self.goompy.get_ywin_from_lat(lat)

        if size is None:
            size = int(DEFAULT_SYMBOL_SIZE / 2)

        elif not -1 < size <= MAX_SYMBOL_SIZE:
            raise ValueError(f'size drawing object must be positive and '
                             f'less than {MAX_SYMBOL_SIZE + 1}')

        else:
            size = int(size/2)

        bbox = (x - size, y - size, x + size, y + size)
        self.canvas.create_oval(*bbox, **kwargs)

    def check_quit(self, event):
        if ord(event.char) == 27:  # ESC
            exit(0)


if __name__ == '__main__':
    UI().mainloop()
