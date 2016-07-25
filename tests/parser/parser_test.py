#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 测试编译功能 """

import os
import unittest
import prometheus.parser.parsehandler as handler

ROOT_DIR = 'benchmark'
NORMAL_C_DIR = ROOT_DIR + '/normal'
ERR_C_DIR = ROOT_DIR + '/err'


class TestParser(unittest.TestCase):

    def test_parser(self):
        for file_path in self.all_c_files(NORMAL_C_DIR):
            try:
                handler.build_ast(file_path)
            except handler.ParseError:
                self.fail('ParseError raised by build_ast')
        for file_path in self.all_c_files(ERR_C_DIR):
            self.assertRaises(handler.ParseError, handler.build_ast, file_path)

    @staticmethod
    def all_c_files(root_dir):
        """获取文件夹下所有c文件"""
        root_dir = os.path.abspath(root_dir)
        files = []
        for lists in os.listdir(root_dir):
            path = os.path.join(root_dir, lists)
            if os.path.isdir(path):
                files.extend(TestParser.all_c_files(path))
            else:
                files.append(path)
        return files


if __name__ == '__main__':
    unittest.main()
