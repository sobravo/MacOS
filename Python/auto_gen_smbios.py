
from subprocess import Popen, PIPE, STDOUT
s = '3\nMacPro7,1 10\n\nQ\n'
p = Popen(['/Users/songbin/Hackintosh/APP/GenSMBIOS/GenSMBIOS/GenSMBIOS.command'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
stdout, stderr = p.communicate(s.encode())
print(stdout.decode())

