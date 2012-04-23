#!/usr/bin/python2

#!/usr/bin/python2
# Shebang is for Arch. You may need to
# change this to !/usr/bin/env python

import urllib, os, sys
import os.path
from xml.dom import minidom


# Edit these variables.
gpxFile = "carneddau_photos.gpx" # gpx file containing POI data.
icon = "icon_blue.png" # Icon used to denote POI.
iconSize = "24,24"
iconOffset = "0,-24" # Offset icon from POI so it doesn't obscure the POI.

# Placeholder. You will need to edit the titles manually
# in the text file.
title = "My Title."

dom = minidom.parse(gpxFile)

# Get a list containing the trackpoint nodes.
trkpt = dom.getElementsByTagName('trkpt')

def make_href(link):
    """
    Construct a url from the image file name. The url will display the
    thumbnail and a link to full size photo.
    """

    # Break up filename into path and filename components.
    dir, fname = os.path.split(link)

    # Construct the link.
    href = ('<a  href=javascript:popUp("%s")> <img src="%s/thumb.%s" alt="photo" />  </a><br>') % (link, dir, fname)

    return href


# Print out the position data, Title,icon data and a url
# containing the photo information in tab separated format.
print "lat\tlon\ttitle\tdescription\ticon\ticonSize\ticonOffset"
for trk in trkpt:
    lat =  trk.getAttribute('lat')
    lon =  trk.getAttribute('lon')
    link = trk.getElementsByTagName('link')

    # Turn the image filename into a url.
    for linkname in link:
        mylink = make_href(linkname.getAttribute('href'))

    # print the result to stdout. You can redirect
    # this to a filename.
    print ("%s\t%s\t%s\t%s\t%s\t%s\t%s" ) % (lat, lon, title, mylink, icon, iconSize, iconOffset)

# We need a final blank line at the end of the file
print "\n"
