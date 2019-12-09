'''
GooMPy: Google Maps for Python

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
import os
import time
import math as m
from io import BytesIO
import urllib.request
import PIL.Image

try:
    from .key import _KEY

except:  # pylint: disable=bare-except
    print('google api key required')
    exit()

urlopen = urllib.request.urlopen

_EARTHPIX = 268435456  # Number of pixels in half the earth's circumference at zoom = 21
_DEGREE_PRECISION = 4  # Number of decimal places for rounding coordinates
_TILESIZE = 640        # Larget tile we can grab without paying (was 640)
_GRABRATE = 4          # Fastest rate at which we can download tiles without paying

_pixrad = _EARTHPIX / m.pi


def _new_image(width, height):
    return PIL.Image.new('RGB', (width, height))


def _roundto(value, digits):
    return int(value * 10**digits) / 10.**digits


def _zoom_factor(zoom):
    ''' apply factor according to zoom '''
    return 2 ** (21 - zoom)


def _grab_tile(lat, lon, zoom, maptype, _TILESIZE, sleeptime):
    urlbase = 'https://maps.googleapis.com/maps/api/staticmap?center=%f,%f&zoom=%d&maptype=%s&size=%dx%d&format=jpg'  # pylint: disable=line-too-long
    urlbase += '&key=' + _KEY

    specs = lat, lon, zoom, maptype, _TILESIZE, _TILESIZE

    filename = 'mapscache/' + ('%f_%f_%d_%s_%d_%d' % specs) + '.jpg'

    tile = None

    if os.path.isfile(filename):
        tile = PIL.Image.open(filename)

    else:
        url = urlbase % specs

        result = urlopen(url).read()
        tile = PIL.Image.open(BytesIO(result))

        # Some tiles are in mode `RGBA` and need to be converted
        if tile.mode != 'RGB':
            tile = tile.convert('RGB')

        if not os.path.exists('mapscache'):
            os.mkdir('mapscache')

        tile.save(filename)
        time.sleep(sleeptime)  # Choke back speed to avoid maxing out limit

    return tile


def _x_to_lon(x, longitude, zoom):
    longitude = _roundto(longitude, _DEGREE_PRECISION)
    lonpix = _EARTHPIX + longitude * m.radians(_pixrad)

    return m.degrees(
        (lonpix + _zoom_factor(zoom) * x  - _EARTHPIX) / _pixrad)


def _y_to_lat(y, latitude, zoom):
    latitude = _roundto(latitude, _DEGREE_PRECISION)
    sinlat = m.sin(m.radians(latitude))
    latpix = _EARTHPIX - _pixrad * m.log((1 + sinlat)/(1 - sinlat)) / 2

    return m.degrees(
        m.pi/2 - 2 * m.atan(m.exp((latpix + _zoom_factor(zoom) * y -
                                   _EARTHPIX) / _pixrad)))


def _lon_to_x(lon, longitude, ntiles, zoom):
    lonpix = _EARTHPIX + longitude * m.radians(_pixrad)
    lon = m.radians(lon)
    return round((_EARTHPIX + lon * _pixrad - lonpix) / _zoom_factor(zoom)
                 + 0.5 * ntiles * _TILESIZE)


def _lat_to_y(lat, latitude, ntiles, zoom):
    sinlat = m.sin(m.radians(latitude))
    latpix = _EARTHPIX - _pixrad * m.log((1 + sinlat)/(1 - sinlat)) / 2

    lat = m.radians(lat)
    pix = ((_EARTHPIX + _pixrad * m.log(m.tan(m.pi / 4 - lat / 2)) - latpix) /
           _zoom_factor(zoom))
    return round(pix + 0.5 * ntiles * _TILESIZE)


def _fetch_tiles(
        latitude, longitude, zoom, maptype, radius_meters, default_ntiles):
    '''
    Fetches tiles from GoogleMaps at the specified coordinates, zoom level (0-22), and map
    type ('roadmap', 'terrain', 'satellite', or 'hybrid').  The value of radius_meters
    deteremines the number of tiles that will be fetched; if it is unspecified, the number
    defaults to default_ntiles.  Tiles are stored as JPEG images in the mapscache folder.
    '''
    latitude = _roundto(latitude, _DEGREE_PRECISION)
    longitude = _roundto(longitude, _DEGREE_PRECISION)

    # https://groups.google.com/forum/#!topic/google-maps-js-api-v3/hDRO4oHVSeM
    pixels_per_meter = 2**zoom / (156543.03392 * m.cos(m.radians(latitude)))

    # number of tiles required to go from center latitude to desired radius in meters
    ntiles = default_ntiles if radius_meters is None else (
        int(round(2 * pixels_per_meter / (_TILESIZE / 2. / radius_meters))))

    bigsize = ntiles * _TILESIZE
    bigimage = _new_image(bigsize, bigsize)

    for j in range(ntiles):
        lon = _x_to_lon((j - ntiles / 2 + 0.5) * _TILESIZE, longitude, zoom)

        for k in range(ntiles):
            lat = _y_to_lat((k - ntiles / 2 + 0.5) * _TILESIZE, latitude, zoom)

            tile = _grab_tile(lat, lon, zoom, maptype, _TILESIZE, 1./_GRABRATE)
            bigimage.paste(tile, (j * _TILESIZE, k * _TILESIZE))

    west = _x_to_lon(-ntiles / 2 * _TILESIZE, longitude, zoom)
    east = _x_to_lon(ntiles / 2 * _TILESIZE, longitude, zoom)

    north = _y_to_lat(-ntiles / 2 * _TILESIZE, latitude, zoom)
    south = _y_to_lat(ntiles / 2 * _TILESIZE, latitude, zoom)

    # TODO: DEBUG PRINT LINE
    print(f'------------------------------------------------\n'
          f'west: {west:0.4f}, east: {east:0.4f}\n'
          f'north: {north:0.4f}, south: {south:0.4f}\n'
          f'tiles: {ntiles}, zoom: {zoom}')

    return bigimage, ntiles, (north, west), (south, east)
