#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: flonly
# @Date:   2015-06-02 21:39:48
# @Last Modified by:   flonly
# @Last Modified time: 2015-06-02 22:30:01


class BitReader:
    def __init__(self,fd):
        self.src_fd     = fd
        self.byteOffset = 0 
        self.bitOffset  = 0
        self.buffer     = []

    def readBytes(self,n)
        out=[]
        if(n > len(self.buffer)):
            self.loadBuffer(n)
        if(n < len(self.buffer)):
            n = len(self.buffer)

        out = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return out

    def loadBuffer(bytesCount):
        self.buffer.fromfile(self.src_fd,bytesCount)
        return True


