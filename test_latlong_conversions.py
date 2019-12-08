'''lat, long conversions tests to/ from pixels
   tests for 4 quandrants in the world
'''
import pytest
from goompy import GooMPy

WIDTH = 800
HEIGHT = 500
MAPTYPE = 'roadmap'
TEST_TOLERANCE = 1
zoom = 15


class TestNL:
    ''' ----------------------- AMSTERDAM TEST (+LON, +LAT) -------------- '''
    test_set_nl = {
        'LONGITUDE': 4.8994,
        'LATITUDE': 52.3755,
        'longitude_result': 4.8882,
        'latitude_result': 52.3774,
        'x_pixels': 60,
        'y_pixels': 246,
    }

    LONGITUDE = test_set_nl.get('LONGITUDE')
    LATITUDE = test_set_nl.get('LATITUDE')

    goompy = GooMPy(
        WIDTH, HEIGHT, LATITUDE, LONGITUDE, zoom, MAPTYPE, radius_meters=None)
    goompy.use_map_type(MAPTYPE)

    goompy.leftx = 1280
    goompy.uppery = 1280

    def test_get_lon_from_x_nl(self):
        x_pixels = self.test_set_nl.get('x_pixels')
        longitude_result = self.test_set_nl.get('longitude_result')

        lon = self.goompy.get_lon_from_x(x_pixels)
        assert f'{lon:0.4f}' == f'{longitude_result:0.4f}'


    def test_get_lat_from_y_nl(self):
        latitude_result = self.test_set_nl.get('latitude_result')
        y_pixels = self.test_set_nl.get('y_pixels')

        lat = self.goompy.get_lat_from_y(y_pixels)
        assert f'{lat:0.4f}' == f'{latitude_result:0.4f}'


    def test_get_x_from_lon_nl(self):
        longitude_result = self.test_set_nl.get('longitude_result')
        x_pixels_result = self.test_set_nl.get('x_pixels') + self.goompy.leftx

        x = self.goompy.get_x_from_lon(longitude_result)
        assert abs(x - x_pixels_result) <= 1


    def test_get_y_from_lat_nl(self):
        latitude_result = self.test_set_nl.get('latitude_result')
        y_pixels_result = self.test_set_nl.get('y_pixels') + self.goompy.uppery

        y = self.goompy.get_y_from_lat(latitude_result)
        assert abs(y - y_pixels_result) <= TEST_TOLERANCE


class TestUS:
    ''' ----------------------- NEW YORK TEST (-LON, +LAT) ------------- '''
    test_set_us = {
        'LONGITUDE': -74.012,
        'LATITUDE': 40.7044,
        'longitude_result': -74.0045,
        'latitude_result': 40.7097,
        'x_pixels': 495,
        'y_pixels': 156,
    }

    LONGITUDE = test_set_us.get('LONGITUDE')
    LATITUDE = test_set_us.get('LATITUDE')

    goompy = GooMPy(
        WIDTH, HEIGHT, LATITUDE, LONGITUDE, zoom, MAPTYPE, radius_meters=None)
    goompy.use_map_type(MAPTYPE)

    goompy.leftx = 1280
    goompy.uppery = 1280

    def test_get_lon_from_x_us(self):
        x_pixels = self.test_set_us.get('x_pixels')
        longitude_result = self.test_set_us.get('longitude_result')

        lon = self.goompy.get_lon_from_x(x_pixels)
        assert f'{lon:0.4f}' == f'{longitude_result:0.4f}'


    def test_get_lat_from_y_us(self):
        latitude_result = self.test_set_us.get('latitude_result')
        y_pixels = self.test_set_us.get('y_pixels')

        lat = self.goompy.get_lat_from_y(y_pixels)
        assert f'{lat:0.4f}' == f'{latitude_result:0.4f}'


    def test_get_x_from_lon_us(self):
        longitude_result = self.test_set_us.get('longitude_result')
        x_pixels_result = self.test_set_us.get('x_pixels') + self.goompy.leftx

        x = self.goompy.get_x_from_lon(longitude_result)
        assert abs(x - x_pixels_result) <= 1


    def test_get_y_from_lat_us(self):
        latitude_result = self.test_set_us.get('latitude_result')
        y_pixels_result = self.test_set_us.get('y_pixels') + self.goompy.uppery

        y = self.goompy.get_y_from_lat(latitude_result)
        assert abs(y - y_pixels_result) <= TEST_TOLERANCE


class TestAR:
    ''' ----------------------- BUENOS AIRES TEST (-LON, -LAT) ------------- '''
    test_set_ar = {
        'LATITUDE': -34.6246,
        'LONGITUDE': -58.4017,
        'longitude_result': -58.4589,
        'latitude_result': -34.6109,
        'x_pixels': 266,
        'y_pixels': 572,
    }

    LONGITUDE = test_set_ar.get('LONGITUDE')
    LATITUDE = test_set_ar.get('LATITUDE')

    goompy = GooMPy(
        WIDTH, HEIGHT, LATITUDE, LONGITUDE, zoom, MAPTYPE, radius_meters=None)
    goompy.use_map_type(MAPTYPE)

    goompy.leftx = 0
    goompy.uppery = 640

    def test_get_lon_from_x_ar(self):
        x_pixels = self.test_set_ar.get('x_pixels')
        longitude_result = self.test_set_ar.get('longitude_result')

        lon = self.goompy.get_lon_from_x(x_pixels)
        assert f'{lon:0.4f}' == f'{longitude_result:0.4f}'


    def test_get_lat_from_y_ar(self):
        latitude_result = self.test_set_ar.get('latitude_result')
        y_pixels = self.test_set_ar.get('y_pixels')

        lat = self.goompy.get_lat_from_y(y_pixels)
        assert f'{lat:0.4f}' == f'{latitude_result:0.4f}'


    def test_get_x_from_lon_ar(self):
        longitude_result = self.test_set_ar.get('longitude_result')
        x_pixels_result = self.test_set_ar.get('x_pixels') + self.goompy.leftx

        x = self.goompy.get_x_from_lon(longitude_result)
        assert abs(x - x_pixels_result) <= 1


    def test_get_y_from_lat_ar(self):
        latitude_result = self.test_set_ar.get('latitude_result')
        y_pixels_result = self.test_set_ar.get('y_pixels') + self.goompy.uppery

        y = self.goompy.get_y_from_lat(latitude_result)
        assert abs(y - y_pixels_result) <= TEST_TOLERANCE


class TestAU:
    ''' ----------------------- SYDNEY TEST (+LON, -LAT) ------------- '''
    test_set_au = {
        'LATITUDE': -33.8566,
        'LONGITUDE': 151.2153,
        'longitude_result': 151.2540,
        'latitude_result': -33.8839,
        'x_pixels': 581,
        'y_pixels': 446,
    }

    LONGITUDE = test_set_au.get('LONGITUDE')
    LATITUDE = test_set_au.get('LATITUDE')

    goompy = GooMPy(
        WIDTH, HEIGHT, LATITUDE, LONGITUDE, zoom, MAPTYPE, radius_meters=None)
    goompy.use_map_type(MAPTYPE)

    goompy.leftx = 1920
    goompy.uppery = 1920

    def test_get_lon_from_x_au(self):
        x_pixels = self.test_set_au.get('x_pixels')
        longitude_result = self.test_set_au.get('longitude_result')

        lon = self.goompy.get_lon_from_x(x_pixels)
        assert f'{lon:0.4f}' == f'{longitude_result:0.4f}'


    def test_get_lat_from_y_au(self):
        latitude_result = self.test_set_au.get('latitude_result')
        y_pixels = self.test_set_au.get('y_pixels')

        lat = self.goompy.get_lat_from_y(y_pixels)
        assert f'{lat:0.4f}' == f'{latitude_result:0.4f}'


    def test_get_x_from_lon_au(self):
        longitude_result = self.test_set_au.get('longitude_result')
        x_pixels_result = self.test_set_au.get('x_pixels') + self.goompy.leftx

        x = self.goompy.get_x_from_lon(longitude_result)
        assert abs(x - x_pixels_result) <= 1


    def test_get_y_from_lat_au(self):
        latitude_result = self.test_set_au.get('latitude_result')
        y_pixels_result = self.test_set_au.get('y_pixels') + self.goompy.uppery

        y = self.goompy.get_y_from_lat(latitude_result)
        assert abs(y - y_pixels_result) <= TEST_TOLERANCE


if __name__ == '__main__':
    test_set_ar = {
        'LATITUDE': -34.6246,
        'LONGITUDE': -58.4017,
        'longitude_result': -58.4589,
        'latitude_result': -34.6109,
        'x_pixels': 266,
        'y_pixels': 572,
    }

    print(test_set_ar)

    LONGITUDE = test_set_ar.get('LONGITUDE')
    LATITUDE = test_set_ar.get('LATITUDE')

    goompy = GooMPy(
        WIDTH, HEIGHT, LATITUDE, LONGITUDE, zoom, MAPTYPE, radius_meters=None)
    goompy.use_map_type(MAPTYPE)
    goompy.leftx = 0
    goompy.uppery = 640

    print(goompy.get_lon_from_x(test_set_ar.get('x_pixels')))
    print(goompy.get_lat_from_y(test_set_ar.get('y_pixels')))
    print(goompy.get_x_from_lon(test_set_ar.get('longitude_result')))
    print(goompy.get_y_from_lat(test_set_ar.get('latitude_result')))
