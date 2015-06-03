#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: flonly
# @Date:   2015-06-02 21:07:34
# @Last Modified by:   flonly
# @Last Modified time: 2015-06-02 21:54:29

from BitRead import BitRead

class FLV

    def __init__():
        self.ofile='output/o.txt'
        self.ifile='res/i.flv'
        self.ofd = open(self.ofile,'w')
        self.ifd = open(self.ifile,'r')
        self.bitReader = new BitRead(self.ifd)

        self.FLV_HEADER_SIZE    = 9

    def getHeader(fd):
        bytes=readBytes(self.FLV_HEADER_SIZE)


    def readBytes(n):
        bytes=self.bitReader.readBytes(n)
        return bytes

    def start():



if __name__ == '__main__':
    main()