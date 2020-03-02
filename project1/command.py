"""
Network Helper
=============
provides
	Simple network helper functions such as
		1) for the ping details to an ip address
		2)-pn 
"""
import sys
import os
import socket
import network_helper 

#function which returns the ping details to a domain_name
def my_ping_dm(domain_name):
	if domain_name == "127.0.0.0" :
		return "ConnectError: [Not able to ping broadcast]"
	return os.popen("ping -c 4 " + domain_name + " | tail -n 3").read().strip()
	
#function which returns the ping details to an ip_addr	
def my_ping(ip_addr):
	if ip_addr == "127.0.0.0" :
		return "ConnectError: [Not able to ping broadcast]"
	if __ipaddr_validate(ip_addr):
		return os.popen("ping -c 4 "+ip_addr+" | tail -n 3").read().strip()
	return "ArgumentError: [Invalid ip address]"
	
	
#function which returns the Default gateway details of the kernal ip routing 
#table
def my_gateway():
	return os.popen("ip route show | head -n 1 | awk '{print $5}'")\
					.read().strip(), os.popen("ip route show | head -n\
					1 | awk '{print $3}'").read().strip()
	
#function which returns the hop_count to an ip_addr or url
def my_hops(ip_addr):
	if(ip_addr=="127.0.0.0"):
		return "ConnectError: [Permission denied to 127.0.0.0]"		
	hop_value=os.popen("traceroute " + ip_addr + " | tail -n 1 | awk \
					   '{print $1}'").read().strip()
	if hop_value == "30" or hop_value=="":
		return "ConnectError: [Ip address or hostname not reachable]"
	return hop_value + " Hop to " + ip_addr
	
	
#function which returns the dictionary of all available insterfaces as the key 
#and the ip_addr as the value,the total no: interface(with ip_addr,without 
#ip_aadr and both)
def ifip():
	dict_ifip = {}
	ifce_cnt = 0
	ifce_cnt_noip = 0
	for i in get_interfaces():
		ip_addr = os.popen("ifconfig " + i + " | grep 'inet addr:'\
						 | cut -d: -f2 | awk '{ print $1}'").read().strip()
		if len(ip_addr) == 0:
			ifce_cnt_noip = ifce_cnt_noip+1
			ifce_cnt = ifce_cnt+1
			dict_ifip[i] = "No ip address for this device"
		else:
				dict_ifip[i] = ip_addr
				ifce_cnt = ifce_cnt+1
	return list(dict.items(dict_ifip)), ifce_cnt, ifce_cnt_noip
	
	
#function which returns the list of all available insterfaces
def get_interfaces():
	ifce_list = os.popen("ifconfig -a | grep -Eo '^[^ ]+'").read().strip()
	return ifce_list.strip().split()
	
		
def __ipaddr_validate(ip_addr):
	try:
		socket.inet_aton(ip_addr)
		if ip_addr.count(".")==3:
			return True
		return False
	except socket.error:
		return False	
		
#__main__:main function takes command line arguments from user to performs corresponding operations to prints the required details
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
		print(my_ping(sys.argv[2]))
	elif sys.argv[1] == "-pd":
		if len(sys.argv) > 3:
			print("UsageError: [Unwanted arguments passed]\n\
Usage:  [-pd takes one argument ip address]")
			exit()
		if len(sys.argv) < 3:
			print("UsageError: [No arguments passed]\n\
Usage:  [-pd takes one argument domain name]")
			exit()
		print(my_ping_dm(sys.argv[2]))
	elif sys.argv[1] == "-ifip":
		if len(sys.argv) > 2:
			print("UsageError:  [-ifip takes no arguments]")
			exit()
		list_ifip, ifce_cnt, ifce_cnt_noip = ifip()
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
		gateway_dev, gateway_ip=my_gateway()
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
		print(my_hops(sys.argv[2]))
	else :
		print("IllegalOperation:  [valid operations]\n\
Usage:  [-h : to find hop count to an ip address(add ip after -h)]\n\
\t[-p: to get an ip addr(add ip after -p)]\n\t[-g: to print default gateway]\
\n\t[-ifip: to print interface details]")
n=network_helper.NetworkHelper()
print(n.network_hop_count("google.com"))
exit()	


