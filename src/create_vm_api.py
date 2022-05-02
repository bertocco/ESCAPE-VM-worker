"""
This is a simple demo code how to use fedcloudclient code as a library
for development of tools and services for EGI Federated Cloud
Only single call is needed for any OpenStack command at any site/VO
Usage: add your access token to line 14, and execute "python demo.py"
"""

import json

# Import fedcloudclient library
from fedcloudclient.openstack import fedcloud_openstack

def list_flavors():

    command = ("flavor", "list")
    return fedcloud_openstack(token, site, vo, command)

def list_images():
    command = ("image", "list")
    return fedcloud_openstack(token, site, vo, command)

def list_networks():
    command = ("network", "list")
    return fedcloud_openstack(token, site, vo, command)

# If you want, uncomment default values
#INFN-CATANIA-STACK
flavor = "m1.tiny"
image = "ACCESS.EGI.EU Image for EGI Docker [Ubuntu/18.04/VirtualBox]"
network = "NON-LHCone"
#INFN-PADOVA-STACK
#flavor = "m1.tiny"
#image="Ubuntu Server 18.04 LTS"
#network="
def create_VM():
    command = ("server", "create", "ESCAPEEUTEST", "--flavor", flavor, "--image", image, "--network", network)
    return fedcloud_openstack(token, site, vo, command)
    

def check_and_print_result(error_code, result):
    if error_code == 0:
        print(json.dumps(result, indent=4))
    else:
        # If error, result is string containing error message
        print("Error message is %s" % result)

# Setting values for input parameters: token, site, VO
site = "INFN-PADOVA-STACK"
vo = "vo.access.egi.eu"
# Read the auth token from input
token = input("Please, provide your authentication token:\n")
"""
error_code, result = list_flavors()
check_and_print_result(error_code, result)

flavor = input("Select a flavor from the list by name\n")

error_code, result = list_images()
check_and_print_result(error_code, result)

image = input("Select an image from the list by name\n")

error_code, result = list_networks()
check_and_print_result(error_code, result)

network = input("Select a network from the list by name\n")
"""
print("Creating the VM .....")
error_code, result = create_VM()
check_and_print_result(error_code, result)



