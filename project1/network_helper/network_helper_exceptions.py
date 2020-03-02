#!/usr/bin/python
# -*- coding: utf-8 -*-
class LoopBackIpAddrError(Exception):
            
    def __str__(self):

        return 'loopback error : cant find no:of hops to loopback address'
	 
	    
class SomeError(Exception):
	pass	
	
