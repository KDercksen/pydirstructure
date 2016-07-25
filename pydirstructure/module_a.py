#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SomeClass:

    def __init__(self):
        self.msg = 'Hello, {}'

    def do_something(self, arg):
        return self.msg.format(arg)


def main():
    print(SomeClass().do_something('this is module_a.main()'))


if __name__ == '__main__':
    main()
