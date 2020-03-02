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
class NetworkHelper:
    """
    class: NetworkHelper
    ====================
        NetworkHelper class provides helper functions 
        to perform network commands such as
            1. network_ping_statistics 
            2. network_hop_count
            3. default_gateway_details
            4. network_interface_details
            5. __get_interfaces 
    """
    def __init__(self):
        """
        Default Constructor
        """
        pass

    def network_ping_statistics(self,domain_name):
        """
         network_ping_statistics returns a string contaning
         the ping statistics of the given argument
            Parameters:
                1.domain_name(it can either be domain name or an ip address)
        """
        if domain_name == "127.0.0.0":
            return "ConnectError: [Not able to ping broadcast]"
        return os.popen("ping -c 4 " + domain_name + " | tail -n 3").read().strip()


    def network_hop_count(self,ip_addr):
        """
        network_hop_count returns a string 
        contaning the ping statistics of the given argument
            Parameters
                1.domain_name(it can either be domain name or an ip address)
        """
        if(ip_addr=="127.0.0.0"):
            return "ConnectError: [Permission denied to 127.0.0.0]"
        hop_value=os.popen("traceroute " + ip_addr + " | tail -n 1 | awk \
                            '{print $1}'").read().strip()
        if hop_value == "30" or hop_value=="":
            return "ConnectError: [Ip address or hostname is not reachable]"
        return hop_value + " Hop to " + ip_addr


    def __get_interfaces(self):
        """
        __get_interfaces is a private method which returns a list 
        contaning the names of the network interfaces available
        """
        ifce_list = os.popen("ifconfig -a | grep -Eo '^[^ ]+'").read().strip()
        return ifce_list.strip().split()


    def default_gateway_details(self):
        """
        network_interface_details returns a list and the total number of
        interfaces and number of interfaces with no ip address
        """
        return os.popen("ip route show | head -n 1 | awk '{print $5}'")\
                        .read().strip(), os.popen("ip route show | head -n\
                        1 | awk '{print $3}'").read().strip()


    def network_interface_details(self):
        """
        network_interface_details returns a list and the total number of
        interfaces and number of interfaces with no ip address
        """
        dict_ifip = {}
        ifce_cnt = 0
        ifce_cnt_noip = 0
        for i in self.__get_interfaces():
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
if __name__=='__main__':
    net_hlp=NetworkHelper()
    if len(sys.argv) < 2:
        print("Usage:  [-h: to find hop count to an ip address(add ip after -h)]\n\
\t[-p: to get ping statistics of an ip addr(add ip after -p)]\
\n\t[-g: to get default gateway]\
\n\t[-pd : to get ping statistics of a purticular domain name]\
\n\t[-ifip: to get interface details]")


    else:

        if sys.argv[1] == "-p":

            if len(sys.argv) > 3:
                print("UsageError: [Unwanted arguments passed]\n\
Usage:  [-p takes one argument ip address]")
                exit()
                
            if len(sys.argv) < 3:
                print("UsageError: [No arguments passed]\n\
Usage:  [-p takes one argument ip address]")
                exit()
                
            print(net_hlp.network_ping_statistics(sys.argv[2]))
            
            
        elif sys.argv[1] == "-ifip":
            if len(sys.argv) > 2:
                print("UsageError:  [-ifip takes no arguments]")
                exit()
                
            list_ifip, ifce_cnt, ifce_cnt_noip = net_hlp.network_interface_details()
            for i,j in list_ifip:
                print(i,":",j)
                
            print("\ntotal no : of interfaces : ", ifce_cnt, "\ntotal no : of \
interfaces with ip addr : ", ifce_cnt-ifce_cnt_noip, "\ntotal\
no : of interfaces without ip addr : ", ifce_cnt_noip)


        elif sys.argv[1] == "-g":
            if len(sys.argv) > 2:
                print("UsageError: [Unwanted arguments passed]\n\
Usage:  [-h takes no arguments]")
                exit()

            gateway_dev, gateway_ip = net_hlp.default_gateway_details()
            print("Default gateway is", gateway_dev, "with "\
                  "ip address", gateway_ip)

 
        elif sys.argv[1] == "-h":
            if len(sys.argv) > 3:
                print("UsageError: [Unwanted arguments passed]\n\
Usage:  [-h takes one argument ip address]")
                exit()

            if len(sys.argv) < 3:
                print("UsageError: [No arguments passed]\n\
Usage:  [-h takes one argument ip address]")
                exit()

            print(net_hlp.network_hop_count(sys.argv[2]))


        else :
            print("IllegalOperation:  [valid operations]\n\
Usage:  [-h : to find hop count to an ip address(add ip after -h)]\n\
\t[-p: to get an ip addr(add ip after -p)]\n\t[-g: to print default gateway]\
\n\t[-ifip: to print interface details]")

    exit()
