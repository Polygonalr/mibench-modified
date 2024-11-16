#!/bin/sh
./susan input_extreme.pgm output_extreme.smoothing.pgm -s
./susan input_extreme.pgm output_extreme.edges.pgm -e
./susan input_extreme.pgm output_extreme.corners.pgm -c

