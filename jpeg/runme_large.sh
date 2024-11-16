#!/bin/sh
./jpeg-6a/cjpeg -dct int -progressive -opt -outfile catburrito_encode.jpeg catburrito.ppm
./jpeg-6a/djpeg -dct int -ppm -outfile catburrito_decode.ppm catburrito_in.jpg
