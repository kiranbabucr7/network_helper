#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
network_helper_exceptions is module which provides all the exceptions 
to be raised to increase the maximum reliabiliy of the network helper module
    exceptions provided:
        1. Error - is a general Exception
        2. LoopBackIpAddrError - Loopback Ip Address is passed by user
        3. CompletePacketLossError - 100% loss on the packets send to ipaddr
        4. OutputParseError - Not able to parse subshell output
        5. UnKnownHostError -  Ip address or hostname is not reachable
"""


class Error(Exception):
    """
    General Exception
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

        return 'Error:Unknown Error' 


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

        return 'LoopBackIpAddrError: Loopback Ip Address is passed by user'


class CompletePacketLossError(Exception):
    """
    CompletePacketLossError Exception is raised whenever there is a 100% packet
    loss on given ip address or domain name
    """

    def __init__(self):
        """
        constructor
        """
    
        pass
        
    def __str__(self):
        """
        Exception message string
        """

        return 'CompletePacketLossError: 100% loss on the packets send to given \
ip'

class OutputParseError(Exception):
    """
    OutputParseError Exception is raised whenever output subshell cannot be 
    parsed
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

        return 'OutputParseError: output returned from sub shell cannot \
be parsed to integer'
        
        
class UnKnownHostError(Exception):
    """
    UnKnownHostError Exception is raised whenever the host is no reachable or
    path to host is unknown
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

        return 'UnKnownHostError: Ip address or hostname is not reachable'
