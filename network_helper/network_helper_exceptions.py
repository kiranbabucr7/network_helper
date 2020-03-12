#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "kiranbabu"
__status__ = "Dev"
"""
network_helper_exceptions is module which provides all the exceptions 
to be raised to increase the maximum reliabiliy of the network helper package
    exceptions provided by the module network_helper_exceptions:
        1. LoopBackIpAddrError - Loopback Ip Address is passed by the user
        2. CompletePacketLossError - 100% loss on the packets send to ipaddr
        3. UnKnownHostError -  unknown hostname or ip address
        4. HostNotReachableError - route to host is unknown
"""


class LoopBackIpAddrError(Exception):
    """
    LoopBackIpAddrError Exception is raised whenever a user passes loopback ip
    """

    def __init__(self):
        """
        contructor
        """
        pass
      
    def __str__(self):
        """
        Exception message string
        """

        return 'LoopBackIpAddrError: Loopback Ip Address {} is passed by user'\
                .format("127.0.0.0") 


class CompletePacketLossError(Exception):
    """
    CompletePacketLossError Exception is raised whenever there is a 100% packet
    loss on given ip address or domain name
    """

    def __init__(self, ip_or_dname):
        """
        constructor
        """
        
        self._ip_or_dname = ip_or_dname
        
    def __str__(self):
        """
        Exception message string
        """

        return "CompletePacketLossError: 100% loss on host {}"\
                .format(self._ip_or_dname)
        
        
class UnKnownHostError(Exception):
    """
    UnKnownHostError Exception is raised whenever the host cannot be reached
    """
    
    def __init__(self, ip_or_dname):
        """
        contructor
        """
        
        self._ip_or_dname = ip_or_dname
        
    def __str__(self):
        """
        Exception message string
        """

        return "UnKnownHostError: Host {} unknown".format(self._ip_or_dname) 
class HostNotReachableError(Exception):
    """
    HostNotReachableError Exception is raised whenever the host is not known or
    path to host is unknown
    """
    
    def __init__(self, ip_or_dname):
        """
        contructor
        """
        
        self._ip_or_dname = ip_or_dname
        
    def __str__(self):
        """
        Exception message string
        """

        return "UnKnownHostError: Host {} unknown".format(self._ip_or_dname)       
