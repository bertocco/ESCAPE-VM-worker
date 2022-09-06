import json

# Import fedcloudclient library
from fedcloudclient.openstack import fedcloud_openstack

import my_fedcloud_client

# Set fixed (for demo) parameters
site = "CESGA"
vo = "vo.access.egi.eu"
# Fix other values for demo
flavour_selected = "cor2mem4hd20"
image_selected = "Image for EGI Ubuntu 20.04 [Ubuntu/20.04/VirtualBox]"
network_selected = "net-vo.access.egi.eu"
public_network = "public00"

def create_access_key(token, site, vo, ssh_key_name, ssh_key_path):
    my_fedcloud_client.create_fedcloud_keypair(token, site, vo, ssh_key_path, ssh_key_name)

def delete_vm(token, site, vo, vm_name):
    my_fedcloud_client.delete_fedcloud_VM(token, site, vo, vm_name)

def create_vm(token, site, vo, flavour_selected, image_selected, network_selected, ssh_key_name, vm_name):
    my_fedcloud_client.create_fedcloud_VM(token, site, vo, flavour_selected, image_selected, network_selected, ssh_key_name, vm_name)
    pub_IP = my_fedcloud_client.get_a_public_IP(token, site, vo, public_network)
    result = my_fedcloud_client.assign_public_IP_to_VM(token, site, vo, pub_IP, vm_name)
    print("SERVER CREATED:\n")
    print("access user is ubuntu\n \
       machine name is " + vm_name +"\n" + \
       "IP is " + pub_IP)


def main():

    choose_op = input("Select the operation you want execute: \n \
                       1) Create a Virtual Machine\n \
                       2) Create an access key_pair\n \
                       3) Delete an existing Virtual Machine\n")

    print("The operation selected is " + choose_op)
    # Get input parameters
    #token = "YOUR_ACCESS_TOKEN"
    token = input("Provide EGI access token:\n")

    if(choose_op == '1'):
        # Ask for VM name
        # ESCAPE_TEST
        vm_name = input("Provide the virtual machine name:\n")
        ssh_key_name = input("Provide the ssh access key name previously created\n")
        create_vm(token, site, vo, flavour_selected, image_selected, network_selected, ssh_key_name, vm_name)
    elif(choose_op == '2'):
        # Ask for ssh key name
        #ssh_key_name = "sabe_key"
        ssh_key_name = input("Provide a ssh_key_name:\n")
        ssh_key_path = input("Provide the path of the key file\n")
        create_access_key(ssh_key_name, ssh_key_path)
    elif(choose_op == '3'):
        vm_name = input("Provide the virtual machine name:\n")
        delete_vm(token, site, vo, vm_name)
    else:
        print("Wrong selection")
        exit

if __name__ == "__main__":
    main()
