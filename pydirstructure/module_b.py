#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SomeOtherClass:

    def __init__(self):
        self.msg = 'Bye, {}'

    def do_something_else(self, arg):
        return self.msg.format(arg)


def main():
    print(SomeOtherClass().do_something_else('this is module_b.main()'))


if __name__ == '__main__':
    main()
