#!/usr/bin/env python3

from subprocess import call
call(["xelatex", "./cv_10.tex"])
call(["mv", "cv_10.pdf", "./out/curriculum-latest.pdf"])