#!/usr/bin/env bash
rm -fr .tmp
mkdir .tmp
cp *.g4 .tmp
cd .tmp
antlr4 *.g4 -Dlanguage=Python3
rm *.g4
mv -f * ../../../../prometheus/parser
rm -fr ../.tmp
