# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:37:34 2016

@author: Danik
"""

import os
import cgi

from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = r'C:\Users\1\Desktop\WinPython-32bit-3.3.5.0'
PORT = 80
os.chdir(webdir)
srv_addr = ('',PORT)
srvobj = HTTPServer(srv_addr, CGIHTTPRequestHandler)
srvobj.serve_forever() 

