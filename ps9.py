import re

string = '''Interface		IP-Address	OK? 	Method Status	Protocol
 
FastEthernet0/0	192.168.1.242	YES 	manual up	up 
FastEthernet1/0        unassigned	YES 	unset		down 
Serial2/0              	192.168.1.250	YES 	manual up	up 
Serial3/0              	192.168.1.233	YES 	manual up	up 
FastEthernet4/0        unassigned	YES 	unset  		down	
FastEthernet5/0        unassigned	YES        unset 		down
'''

print(re.findall("([a-zA-Z0-9/]+)\s+[0-9a-z.]+\s+[A-Z]+\s+([a-z]+)\s+([a-z]+)\s+.+", string))
