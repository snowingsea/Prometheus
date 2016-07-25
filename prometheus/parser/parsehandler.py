#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 构建抽象语法树 """

import os
import sys
import time
import random
from antlr4 import *
from prometheus.parser.CLexer import CLexer
from prometheus.parser.CParser import CParser

__all__ = ["build_ast", "ParseError"]


class ParseError(Exception):
    def __init__(self, arg):
        self.err_msg = arg


def build_ast(file_path):
    """读取源代码,构建AST"""
    redirect_path = str(int(time.time())) + str(random.randint(0, 9999999)) + '.err'
    f_handler = open(redirect_path, 'w')
    stderr = sys.stderr
    sys.stderr = f_handler
    lexer = CLexer(FileStream(file_path))
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    f_handler.close()
    sys.stderr = stderr

    f_handler = open(redirect_path)
    err_msg = ''
    while 1:
        line = f_handler.readline()
        if not line:
            break
        err_msg += line
    f_handler.close()
    os.remove(redirect_path)
    if len(err_msg.strip()) != 0:
        raise ParseError(err_msg)

    return tree


if __name__ == '__main__':
    ast = build_ast('../../tests/parser/benchmark/add.c')
