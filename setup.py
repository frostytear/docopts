# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name             = "docopts",
      version          = "0.6.1",
      author           = "Lari Rasku",
      author_email     = "raskug@lavabit.com",
      url              = "https://github.com/docopt/docopts",
      description      = "Shell interface for docopt, the command-line "
                         "interface description language.",
      long_description = open('README').read(),
      scripts          = ["docopts"],
      requires         = ["docopt (==0.6.1)"],
      classifiers      = ["Development Status :: 3 - Alpha",
                          "Environment :: Console",
                          "Intended Audience :: Developers",
                          "License :: OSI Approved :: MIT License",
                          "Programming Language :: Python :: 2.6",
                          "Programming Language :: Python :: 2.7",
                          "Programming Language :: Python :: 3.1",
                          "Programming Language :: Python :: 3.2",
                          "Programming Language :: Python :: 3.3",
                          "Operating System :: OS Independent",
                          "Topic :: Utilities"],
      platforms        = ["OS Independent"],
      license          = "MIT License")
