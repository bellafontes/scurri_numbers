#!/usr/bin/env python3

"""
    @author isabella.fontes <aisabellafontes@gmail.com>
    @cia Scurri

    Write a program that prints the numbers from 1 to 100.
    But for multiples of three print “Three” instead of the number
    and for the multiples of five print “Five”.
    For numbers which are multiples of both three and five print “ThreeFive”.

"""


class Numbers(object):

    def __init__(self):
        self.range = range(1, 101)

    '''
            @:description Verify if number is multiple to value.
            @:param value = int.
            @:param number = int.
    '''
    @staticmethod
    def multiple(value=int, number=int):
        if not (isinstance(value, int) and isinstance(number, int)):
            return False

        if number % value == 0:
            return True

        return False

    '''
            @:description Validate rules
            @:param number = int.
    '''
    def validate(self, number):
        if not (self.multiple(3, number) or self.multiple(5, number)):
            return number
        result = ''
        if self.multiple(3, number):
            result += 'Three'
        if self.multiple(5, number):
            result += 'Five'
        return result

    def print_numbers(self):
        for number in self.range:
            print(self.validate(number))


if __name__ == '__main__':
    numbers = Numbers()
    numbers.print_numbers()
