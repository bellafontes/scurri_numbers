# Scurri Numbers Code test

This is a production-ready setup for running a program that prints
the numbers from 1 to 100.

But for multiples of three print “Three” instead of the number
  and for the multiples of five print “Five”.

For numbers which are multiples of both three and five print “ThreeFive”.

## Quick usage

    $ git clone this repository
    $ cd scurri_numbers/
    $ python scurri_numbers.py

## Installation

    $ git clone this repository
    $ python setup.py install

## Import usage
    from scurri_numbers import Numbers
    numbers = Numbers()
    numbers.print_numbers()

## Test
    cd scurri_numbers/
    python3 scurri_numbers_test.py
        or
    python3 -m unittest scurri_numbers_test.py