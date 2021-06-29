import subprocess
import time
import random
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
(options, arguments) = parser.parse_args()

interface_input = options.interface
iface = str(interface_input)

#creates random MAC address
def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )


#changes MAC address of user-entered interface
def change_mac():

    subprocess.call("ifconfig {} down".format(iface), shell=True)
    subprocess.call("ifconfig {} hw ether {}".format(iface, new_mac), shell=True)
    subprocess.call("ifconfig {} up".format(iface), shell=True)

new_mac = rand_mac()
change_mac()
