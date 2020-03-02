#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Network Helper
=============
provides
    NetworkHelper class with helper functions which provies.
        1. ping details of an ip address or domain name.
        2. hop count of an ip address or domain name.
        3. default gateway details.
        4. interface details.
"""
import os
import sys
import socket
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
            5. __get_interfaces 
    """

    @staticmethod
    def __ping_loss(ip_addr):
    
       return int(os.popen("ping -c 4 " + ip_addr + " | tail -n2 | \
                             awk '{print substr($6,1,length($6)-1)}'")\
                             .read().strip())
                        
                        
    @staticmethod
    def network_ping_statistics(ip_or_dname):
    
        """
         network_ping_statistics returns a string contaning
         the ping statistics of the given argument
            Parameters:
                1.domain_name(it can either be domain name or an ip address)
        """
        if(NetworkHelperCommands.__ping_loss(ip_or_dname) == 100):
           return "ConnectError: [Ip address or hostname is not reachable 100% loss]"
        
        if ip_or_dname == "127.0.0.0":
            return "ConnectError: [Not able to ping broadcast]"
            
        return os.popen("ping -c 4 " + ip_or_dname + " | tail -n 3").read().strip()


    @staticmethod
    def network_hop_count(ip_addr):
    
        """
        network_hop_count returns a string 
        contaning the ping statistics of the given argument
            Parameters
                1.domain_name(it can either be domain name or an ip address)
        """
        
        if(NetworkHelperCommands.__ping_loss(ip_addr) == 100):
           return "ConnectError: [Ip address or hostname is not reachable 100% loss]"

        if(ip_addr == "127.0.0.0"):
            return "ConnectError: [Permission denied to 127.0.0.0]"

        hop_value=os.popen("traceroute " + ip_addr + " | tail -n 1 | awk \
                            '{print $1}'").read().strip()
        if hop_value == "30" or hop_value == "":
            return "ConnectError: [Ip address or hostname is not reachable]"
            
        return hop_value + " Hop to " + ip_addr


    @staticmethod
    def default_gateway_details():
        """
        network_interface_details returns a list and the total number of
        interfaces and number of interfaces with no ip address
        """
        return os.popen("ip route show | head -n 1 | awk '{print $5}'")\
                        .read().strip(), os.popen("ip route show | head -n\
                        1 | awk '{print $3}'").read().strip()

    @staticmethod
    def __get_interfaces():
        """
        __get_interfaces is a private method which returns a list 
        contaning the names of the network interfaces available
        """
        ifce_list = os.popen("ifconfig -a | grep -Eo '^[^ ]+'").read().strip()
        return ifce_list.strip().split()


    @staticmethod
    def network_interface_details():
        """
        network_interface_details returns a list and the total number of
        interfaces and number of interfaces with no ip address
        """
        
        dict_ifip = {}
        ifce_cnt = 0
        ifce_cnt_noip = 0
        for i in NetworkHelperCommands.__get_interfaces():
            ip_addr = os.popen("ifconfig " + i + " | grep 'inet addr:'\
                     | cut -d: -f2 | awk '{ print $1}'").read().strip()
            if len(ip_addr) == 0:
                ifce_cnt_noip = ifce_cnt_noip + 1
                ifce_cnt = ifce_cnt + 1
                dict_ifip[i] = "No ip address for this device"
            else:
                dict_ifip[i] = ip_addr
                ifce_cnt = ifce_cnt + 1
        return list(dict.items(dict_ifip)), ifce_cnt, ifce_cnt_noip

