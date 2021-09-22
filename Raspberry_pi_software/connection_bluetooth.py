import pexpect
import time

try:
    child = pexpect.spawn('bluetoothctl')
    child.sendline("default-agent")
    child.sendline("discoverable on")
    child.expect("passkey")

    debut = (child.before).decode('utf-8')
    ind_device = debut.find('Device')

    child.sendline("yes")
    child.expect("Authorize")
    child.sendline("yes")
    time.sleep(2)
    child.sendline("yes")
    time.sleep(2)
    child.sendline("trust " + debut[ind_device + 7:ind_device + 24])
    time.sleep(2)
    child.sendline("discoverable off")
    child.sendline("exit")
    
except:
    pass
