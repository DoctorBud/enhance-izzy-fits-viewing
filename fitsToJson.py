#!/usr/bin/env python

import codecs, json, sys
from astropy.io import fits
import numpy as np


if (not len(sys.argv) == 4):
    print('Usage: python3 fitsToJson <HDU index> <fits file> <output file>')
    quit()

hduindex = int(sys.argv[1])
fitsfile = sys.argv[2]
jsonfile = sys.argv[3]

with fits.open(fitsfile) as hdu:
    nparray = hdu[hduindex].data
    header = hdu[hduindex].header

pyarray = nparray.tolist() # nested lists with same data, indices
json.dump(pyarray, codecs.open(jsonfile, 'w', encoding='utf-8'), 
          separators=(',', ':'), 
          sort_keys=True) 
