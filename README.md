# enhance-izzy-fits-viewing

This project is intended to enhance Izzy's [Phantom Galaxy](https://izzymones.github.io/blog-kit/posts/phantomgalaxy/) blog post by utilizing some of [Smartdown](https://smartdown.io)'s features to provide better interactivity, and also to implement a means of reading FITS files directly from a static file service, rather than requiring preprocessing of FITS into JSON, which is what Izzy's original blog article relied upon.

Changes include:
- Show an entire image in a zoomed-out mode, justified to the upper left corner of the canvas.
- Remove the `Redraw` button in favor of reactive cells.
- Adds ability to read FITS files rather than JSON files.

## Known issues

- Izzy's FITS-to-JSON tool in `fitsToJson.py` requires a preprocessing step, and results in a larger payload than a binary file. However, because `fitsToJson.py` extracts only the first image **HDU** in the fits file, it is more size-efficient for multi-HDU FITS files.
- Ideally, we'd find a tool that lets a FITS file be split into separate, per-HDU files. That would enable many possibilities in the browser in terms of loading different subsets of the HDUs.
- I re

## Set Up

This project displays two different sets of infrared image data from the JWST. Each set contains 4 files corresponding to the following *filters* which isolate a particular infrared wavelength:

- **f770w** - 7.7 micron wavelength
- **f1000w** - 10.0 micron wavelength
- **f1130w** - 11.3 micron wavelength
- **f2100w** - 21.0 micron wavelength

You will need to obtain the correct FITS files