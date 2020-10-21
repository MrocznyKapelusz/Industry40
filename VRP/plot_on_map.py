import gmplot   # to plot on map
import os       # for opening browser from python script

mapFileName = "generatedMaps/map.html"

lati = [19.0790, 19.0810, 19.0850]  # szerokość geograficzna
longi = [72.890, 72.910, 72.930]    # długość geograficzna

gmap = gmplot.GoogleMapPlotter(19.0760,72.8777,15)
# gmap = gmplot.GoogleMapPlotter(51.2587475,15.5522313,15)
gmap.scatter(lati, longi, '#ff0000', size=50, marker = False)
gmap.plot(lati, longi, 'blue', edge_width=2.5)
gmap.draw(mapFileName)

# open generated map
os.system("start " + mapFileName)