#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "kiran babu"
__status__ = "Dev"

"""
Network Helper
=============
provides
    NetworkHelper module provides class NetworkHelperCommands
    with helper functions which provies.
        1. ping details of an ip address or domain name.
        2. hop count of an ip address or domain name.
        3. default gateway details.
        4. interface details.
"""


import os
import socket
from .network_helper_exceptions import LoopBackIpAddrError\
                                       , CompletePacketLossError\
                                       , UnKnownHostError\
                                       , HostNotReachableError 

class NetworkHelperCommands:
    """
    class: NetworkHelperCommands
    ============================
        NetworkHelperCommands class provides helper functions 
        to perform network commands such as
            1. network_ping_statistics 
            2. network_hop_count
            3. default_gateway_details
            4. network_interface_details
    """

    @staticmethod
    def _ping_loss(ip_or_dname):
        """
        _ping_loss is protected function returns the amount of loss 
        percentage of packets send to the parameter which is passsed by the
        user. If the function returns there is an ouput else
        an exception is raised.
            
            Exceptions raised:
                1.UnKnownHostError    
        """
    
        try:
            _command = "ping -c 4 {} | tail -n3 | awk '{}'".format(ip_or_dname\
                       , "{print substr($6,1,length($6)-1)}")
            return int(os.popen(_command).read().strip())
        
        except:
        
            raise  UnKnownHostError(ip_or_dname)           
                        
    @staticmethod
    def network_ping_statistics(ip_or_dname):
    
        """
         network_ping_statistics returns a string contaning
         the ping statistics of the given argument if there is an output, 
         else raises the required exceptions such as
         
            exceptions:
                1.LoopBackIpAddrError
                2.CompletePacketLossError
                3.UnKnownHostError
            Parameters:
                1.domain_name(it can either be domain name or an ip address)
        """
      
        if ip_or_dname == "127.0.0.0":
        
            raise LoopBackIpAddrError

        elif(NetworkHelperCommands._ping_loss(ip_or_dname) == 100):
        
            raise CompletePacketLossError(ip_or_dname)
            
        else:
             
            return os.popen("ping -c 4 " + ip_or_dname + " | tail -n 3")\
                             .read().strip()
        

    @staticmethod
    def network_hop_count(ip_or_dname):
        """
        network_hop_count returns a string contaning the ping statistics of the 
        given argument if there is an output, else raises
        the required exceptions such as
        
            exceptions:
                1.LoopBackIpAddrError
                2.CompletePacketLossError
                3.UnKnownHostError
                4.HostNotReachableError
                
            Parameter
                1.ip_or_dname(it can either be domain name or an ip address)
        """
        
        if(ip_or_dname == "127.0.0.0"):
        
            raise LoopBackIpAddrError()
            
        elif(NetworkHelperCommands._ping_loss(ip_or_dname) == 100):
           
            raise CompletePacketLossError(ip_or_dname)
            
        try:
            _command="traceroute {} | tail -n 1 | awk \
                     {}".format(ip_or_dname,"'{print $1}'")
            _hop_value = int(os.popen(_command).read().strip())
                            
        except:
            
            raise UnKnownHostError
                            
        if _hop_value >= 30:
        
            raise HostNotReachableError(ip_or_dname)
            
        else:   
        
            return _hop_value


    @staticmethod
    def default_gateway_details():
        """
        network_interface_details returns a list and the total number of
        interfaces and number of interfaces with no ip address
        """
        
        return os.popen("ip route show | head -n 1 | awk '{print $5}'")\
                        .read().strip()\
                        , os.popen("ip route show | head -n1 \
                        | awk '{print $3}'")\
                        .read().strip()

    @staticmethod
    def _get_interfaces():
        """
        _get_interfaces is a protected method which returns a list 
        contaning the names of the network interfaces available
        """
        
        _ifce_list = os.popen("ifconfig -a | grep -Eo '^[^ ]+'").read().strip()
        return _ifce_list.strip().split()


    @staticmethod
    def network_interface_details():
        """
        network_interface_details returns a list and the total number of
        interfaces and number of interfaces with no ip address
        """
        _dict_ifip = {}
        _ifce_cnt = 0
        _ifce_cnt_noip = 0
        
        for i in NetworkHelperCommands._get_interfaces():
            
            _ip_addr = os.popen("ifconfig {} | grep 'inet addr:'\
                                 | cut -d: -f2 | awk {}"\
                                 .format(i,"'{ print $1}'")).read().strip()
                     
            if len(_ip_addr) == 0:
            
                _ifce_cnt_noip = _ifce_cnt_noip + 1
                _ifce_cnt = _ifce_cnt + 1
                _dict_ifip[i] = "No ip address for this device"
                
            else:
            
                _dict_ifip[i] = _ip_addr
                _ifce_cnt = _ifce_cnt + 1
                
        return list(dict.items(_dict_ifip)), _ifce_cnt, _ifce_cnt_noip
