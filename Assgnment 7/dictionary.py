#Que1: use the dictionary port1={21:"FTP",22:"SSH",23:"telnet",80:"http"},and make a new dictionary in which keys become values and value become keys, as show port2={"FTP":21,"SSH":22,"telnet":23,"http":80}
port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
print("Old dictionary is:")
print(port1)
port2= dict((v,k) for k,v in port1.items())
print("New dictionary is:")
print(port2)
