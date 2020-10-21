from typing import List # to use type aliasing
import gmplot   # to plot on map
import os       # for opening browser from python script
from other_algorithms import DataStructure, City

# type alias
Vector = List[int]


def draw(data:DataStructure, permutation: Vector, filename: str):
    """This function plots given permutation using GoogleMaps

    It uses gmaps testing map to print routes of trucks

    Args:
        permutation (Vector): given permutation as a List[int]
        filename (string)   : name of the file
    Returns:
        None
    Example:
        For given permutation [0, 3, 4, 1, 0] it will draw line between these cities
        and save it as a file in .html format. It will also display what's plotted.
    """
    lati = []   # szerokość
    longi = []  # długość

    for city in permutation:
        lati.append(data.cities[city].latitude)
        longi.append(data.cities[city].longitude)

    # lati = [19.0790, 19.0810, 19.0850]  # szerokość geograficzna
    # longi = [72.890, 72.910, 72.930]    # długość geograficzna

    # geometric center of Poland
    gmap = gmplot.GoogleMapPlotter(52.065221, 19.252482, 7)
    gmap.scatter(lati, longi, '#ff0000', size=50, marker = False)
    gmap.plot(lati, longi, 'blue', edge_width=2.5)
    gmap.draw(filename)

    # open generated map
    os.system("start " + filename)
