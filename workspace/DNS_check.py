#Title: 	DNS_check.py
#Auhtor: 	Luke Smith, lws3955@rit.edu
#Description:	Gets IP addresses for supplied domains from
#		several public DNS servers.
#Requirements:	Make sure the 'domains.list' and 'dns.list'
#		files are in the same directory as this script.

from subprocess import *
import re

#open files storing data
domain_file = open('domains.list')
dns_file = open('dns.list')
domains_list = domain_file.readlines()[1:]
dns_list = dns_file.readlines()[1:]



def TEST_DNS( name, ip ):

	#fix DNS server IP address for dig command
	ip = "@" + ip

	#store output from dig command	
	output = check_output(["dig", ip, name, "+noall", "+answer", "-t","a"])

	#remove useless lines
	zone_info = output.split('\n')[4:]		

	#get IP address from A records, print to terminal	
	for line in zone_info:
		response = re.findall('(?<!\d)\d{1,3}\.(?<!\d)\d{1,3}\.(?<!\d)\d{1,3}\.\d{1,3}(?!\d)', line)		
		if len(response) == 1:
			print( ip[1:] +" \t "), response[0]
	return


for domain_name in domains_list:
	#remove trailing newline
	domain_name = domain_name[:-1]

	#print heading for output columns
	print("\t"+domain_name)
	print("DNS IP Address \t  Response") 

	#get all the IP addresses from the A records on the DNS servers 
	for dns_ip in dns_list:
		dns_ip = dns_ip[:-1]
		TEST_DNS( domain_name, dns_ip )
	print("\n")


