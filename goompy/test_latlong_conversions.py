'''lat, long conversions tests to/ from pixels
   tests for 4 quandrants in the world
'''
from ._goompy_functions import (
    _x_to_lon, _y_to_lat, _lon_to_x, _lat_to_y
)

TEST_TOLERANCE = 1
ntiles = 4
zoom = 15

# ----------------------- AMSTERDAM TEST (+LON, +LAT) --------------
test_set_nl = {
    'LATITUDE': 52.3755,
    'LONGITUDE': 4.8994,
    'longitude_result': 4.8882,
    'latitude_result': 52.3774,
    'x_pixels': 1340,
    'y_pixels': 1526,
}

def test_x_to_lon_nl():
    LONGITUDE = test_set_nl.get('LONGITUDE')
    x_pixels = test_set_nl.get('x_pixels')
    longitude_result = test_set_nl.get('longitude_result')

    lon = _x_to_lon(x_pixels, LONGITUDE, ntiles, zoom)
    assert f'{lon:0.4f}' == f'{longitude_result:0.4f}'


def test_y_lat_nl():
    LATITUDE = test_set_nl.get('LATITUDE')
    y_pixels = test_set_nl.get('y_pixels')
    latitude_result = test_set_nl.get('latitude_result')

    lat = _y_to_lat(y_pixels, LATITUDE, ntiles, zoom)
    assert f'{lat:0.4f}' == f'{latitude_result:0.4f}'


def test_lon_to_x_nl():
    LONGITUDE = test_set_nl.get('LONGITUDE')
    longitude_result = test_set_nl.get('longitude_result')
    x_pixels = test_set_nl.get('x_pixels')

    x = _lon_to_x(longitude_result, LONGITUDE, ntiles, zoom)
    assert abs(x - x_pixels) <= 1


def test_lat_to_y_nl():
    LATITUDE = test_set_nl.get('LATITUDE')
    latitude_result = test_set_nl.get('latitude_result')
    y_pixels = test_set_nl.get('y_pixels')

    y = _lat_to_y(latitude_result, LATITUDE, ntiles, zoom)
    assert abs(y - y_pixels) <= TEST_TOLERANCE


# ----------------------- NEW YORK TEST (-LON, +LAT) -------------
test_set_us = {
    'LATITUDE': 40.7044,
    'LONGITUDE': -74.012,
    'longitude_result': -74.0045,
    'latitude_result': 40.7097,
    'x_pixels': 1775,
    'y_pixels': 1436,
}

def test_x_to_lon_us():
    LONGITUDE = test_set_us.get('LONGITUDE')
    x_pixels = test_set_us.get('x_pixels')
    longitude_result = test_set_us.get('longitude_result')

    lon = _x_to_lon(x_pixels, LONGITUDE, ntiles, zoom)
    assert f'{lon:0.4f}' == f'{longitude_result:0.4f}'


def test_y_lat_us():
    LATITUDE = test_set_us.get('LATITUDE')
    y_pixels = test_set_us.get('y_pixels')
    latitude_result = test_set_us.get('latitude_result')

    lat = _y_to_lat(y_pixels, LATITUDE, ntiles, zoom)
    assert f'{lat:0.4f}' == f'{latitude_result:0.4f}'


def test_lon_to_x_us():
    LONGITUDE = test_set_us.get('LONGITUDE')
    longitude_result = test_set_us.get('longitude_result')
    x_pixels = test_set_us.get('x_pixels')

    x = _lon_to_x(longitude_result, LONGITUDE, ntiles, zoom)
    assert abs(x - x_pixels) <= 1


def test_lat_to_y_us():
    LATITUDE = test_set_us.get('LATITUDE')
    latitude_result = test_set_us.get('latitude_result')
    y_pixels = test_set_us.get('y_pixels')

    y = _lat_to_y(latitude_result, LATITUDE, ntiles, zoom)
    assert abs(y - y_pixels) <= TEST_TOLERANCE


# ----------------------- BUENOS AIRES TEST (-LON, -LAT) -------------
test_set_ar = {
    'LATITUDE': -34.6246,
    'LONGITUDE': -58.4017,
    'longitude_result': -58.4589,
    'latitude_result': -34.6109,
    'x_pixels': 266,
    'y_pixels': 1212,
}


def test_x_to_lon_ar():
    LONGITUDE = test_set_ar.get('LONGITUDE')
    x_pixels = test_set_ar.get('x_pixels')
    longitude_result = test_set_ar.get('longitude_result')

    lon = _x_to_lon(x_pixels, LONGITUDE, ntiles, zoom)
    assert f'{lon:0.4f}' == f'{longitude_result:0.4f}'


def test_y_lat_ar():
    LATITUDE = test_set_ar.get('LATITUDE')
    y_pixels = test_set_ar.get('y_pixels')
    latitude_result = test_set_ar.get('latitude_result')

    lat = _y_to_lat(y_pixels, LATITUDE, ntiles, zoom)
    assert f'{lat:0.4f}' == f'{latitude_result:0.4f}'


def test_lon_to_x_ar():
    LONGITUDE = test_set_ar.get('LONGITUDE')
    longitude_result = test_set_ar.get('longitude_result')
    x_pixels = test_set_ar.get('x_pixels')

    x = _lon_to_x(longitude_result, LONGITUDE, ntiles, zoom)
    assert abs(x - x_pixels) <= 1


def test_lat_to_y_ar():
    LATITUDE = test_set_ar.get('LATITUDE')
    latitude_result = test_set_ar.get('latitude_result')
    y_pixels = test_set_ar.get('y_pixels')

    y = _lat_to_y(latitude_result, LATITUDE, ntiles, zoom)
    assert abs(y - y_pixels) <= TEST_TOLERANCE


# ----------------------- SYDNEY TEST (+LON, -LAT) -------------
test_set_au = {
    'LATITUDE': -33.8566,
    'LONGITUDE': 151.2153,
    'longitude_result': 151.2540,
    'latitude_result': -33.8839,
    'x_pixels': 2501,
    'y_pixels': 2366,
}


def test_x_to_lon_au():
    LONGITUDE = test_set_au.get('LONGITUDE')
    x_pixels = test_set_au.get('x_pixels')
    longitude_result = test_set_au.get('longitude_result')

    lon = _x_to_lon(x_pixels, LONGITUDE, ntiles, zoom)
    assert f'{lon:0.4f}' == f'{longitude_result:0.4f}'


def test_y_lat_au():
    LATITUDE = test_set_au.get('LATITUDE')
    y_pixels = test_set_au.get('y_pixels')
    latitude_result = test_set_au.get('latitude_result')

    lat = _y_to_lat(y_pixels, LATITUDE, ntiles, zoom)
    assert f'{lat:0.4f}' == f'{latitude_result:0.4f}'


def test_lon_to_x_au():
    LONGITUDE = test_set_au.get('LONGITUDE')
    longitude_result = test_set_au.get('longitude_result')
    x_pixels = test_set_au.get('x_pixels')

    x = _lon_to_x(longitude_result, LONGITUDE, ntiles, zoom)
    assert abs(x - x_pixels) <= 1


def test_lat_to_y_au():
    LATITUDE = test_set_au.get('LATITUDE')
    latitude_result = test_set_au.get('latitude_result')
    y_pixels = test_set_au.get('y_pixels')

    y = _lat_to_y(latitude_result, LATITUDE, ntiles, zoom)
    assert abs(y - y_pixels) <= TEST_TOLERANCE
