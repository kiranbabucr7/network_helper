#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import network_helper
__author__ = "kiran babu"
"""
command.py is a program to implement the network_helper module which
    provides fucntions such as:
        1. ping details of an ip address or domain name.
        2. hop count of an ip address or domain name.
        3. default gateway details.
        4. interface details.
"""

if __name__ == '__main__':

    if len(sys.argv) < 2:
    
        print("Usage:  [-h: to find hop count to an ip address(add ip after -h)]")
        print("\t[-p: to get ping statistics of an ip addr(add ip after -p)]")
        print("\t[-g: to get default gateway]")
        print("\t[-ifip: to get interface details]")

    else:

        if sys.argv[1] == "-p":

            if len(sys.argv) > 3:
            
                print("UsageError: [Unwanted arguments passed]")
                print("Usage:  [-p takes one argument ip address]")
                exit()
                
            if len(sys.argv) < 3:
            
                print("UsageError: [No arguments passed]")
                print("Usage:  [-p takes one argument ip address]")
                exit()
                
            try:
              
                print(network_helper.NetworkHelperCommands.\
                      network_ping_statistics(sys.argv[2]))
                      
            except (network_helper.network_helper_exceptions.LoopBackIpAddrError\
                    , network_helper.network_helper_exceptions.UnKnownHostError\
                    , network_helper.network_helper_exceptions\
                    .CompletePacketLossError) as err:
            
                print(str(err))
            
        elif sys.argv[1] == "-ifip":
        
            if len(sys.argv) > 2:
            
                print("UsageError:  [-ifip takes no arguments]")
                exit()
              
            list_ifip, ifce_cnt, ifce_cnt_noip = network_helper.\
                                                 NetworkHelperCommands.\
                                                 network_interface_details()
                                                  
            for i,j in list_ifip:
            
                print("{} : {}".format(i,j))
                
            print("\ntotal no : of interfaces : {}".format(ifce_cnt))
            print("total no : of interfaces with ip addr : {}"\
                   .format(ifce_cnt))
            print("total no : of interfaces without ip addr : {}"\
                   .format(ifce_cnt_noip))

        elif sys.argv[1] == "-g":
        
            if len(sys.argv) > 2:
            
                print("UsageError: [Unwanted arguments passed]")
                print("Usage:  [-h takes no arguments]")
                exit()

            gateway_dev, gateway_ip = network_helper.NetworkHelperCommands.\
                                       default_gateway_details()
            print("Default gateway is {} with ip address {}"
                   .format(gateway_dev, gateway_ip))

        elif sys.argv[1] == "-h":
        
            if len(sys.argv) > 3:
            
                print("UsageError: [Unwanted arguments passed]")
                print("Usage:  [-h takes one argument ip address]")
                exit()

            if len(sys.argv) < 3:
            
                print("UsageError: [No arguments passed]")
                print("Usage:  [-h takes one argument ip address]")
                exit()
                
            try:   
            
                print("{} to {}"\
                      .format(network_helper.NetworkHelperCommands\
                      .network_hop_count(sys.argv[2]), sys.argv[2]))
            
            except (network_helper.network_helper_exceptions.LoopBackIpAddrError\
                    , network_helper.network_helper_exceptions.UnKnownHostError\
                    , network_helper.network_helper_exceptions\
                    .CompletePacketLossError\
                    , network_helper.network_helper_exceptions\
                    .HostNotReachableError) as err:
               
                print(str(err))

        else :
        
            print("IllegalOperation:  [Invalid options]")
            print("Usage:  [-h : to find hop count to an ip address(add ip after -h)]")
            print("\t[-p: to get an ip addr(add ip after -p)]")
            print("\t[-g: to print default gateway]")
            print("\t[-ifip: to print interface details]")

    exit()	
