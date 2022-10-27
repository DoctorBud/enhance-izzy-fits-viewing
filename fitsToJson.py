#!/usr/bin/env python

# pip install codecs
# pip install json
# pip install sys
# pip install astropy.io

import codecs, json, sys
from astropy.io import fits
import numpy as np


if (not len(sys.argv) == 3):
    print('Usage: python3 fitsToJson <fits file> <output file>')
    quit()

fitsfile = sys.argv[1]
jsonfile = sys.argv[2]

with fits.open(fitsfile) as hdu:
    nparray = hdu[1].data
    header = hdu[1].header


pyarray = nparray.tolist() # nested lists with same data, indices
json.dump(pyarray, codecs.open(jsonfile, 'w', encoding='utf-8'), 
          separators=(',', ':'), 
          sort_keys=True) 
