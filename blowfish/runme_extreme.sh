#!/bin/sh
./bf e input_extreme.asc output_extreme.enc 1234567890abcdeffedcba0987654321
./bf d output_extreme.enc output_extreme.asc 1234567890abcdeffedcba0987654321
