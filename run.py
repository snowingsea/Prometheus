#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Run Main """

import sys
from antlr4 import *
from prometheus.parser.CLexer import CLexer
from prometheus.parser.CParser import CParser


def main(argv):
    input = FileStream(argv[1])
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.StartRule()


if __name__ == '__main__':
    main(sys.argv)
