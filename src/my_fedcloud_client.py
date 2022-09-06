import json

# Import fedcloudclient library
from fedcloudclient.openstack import fedcloud_openstack
#import fedcloudclient.openstack

# Set fixed (for demo) parameters
# Set fixed (for demo) parameters
#token = "YOUR_ACCESS_TOKEN"
#token = input("Provide EGI access token:\n")
#site = "CESGA"
#vo = "vo.access.egi.eu"
# Fix other values for demo
#flavour_selected = "cor2mem4hd20"
#image_selected = "Image for EGI Ubuntu 20.04 [Ubuntu/20.04/VirtualBox]"
#network_selected = "net-vo.access.egi.eu"
#public_network = "public00"

# OpenStack command must be a tuple

def list_fedcloud_flavours(token, site, vo):
    command=('flavor', 'list')
    error_code, result = exec_fedcloud_command(token, site, vo, command, True)
    if (error_code != 0):
        print("Error listing flavours")
        exit()
    print(result)

def list_fedcloud_images(token, site, vo):
    command=('image', 'list')
    error_code, result =  exec_fedcloud_command(token, site, vo, command, True)
    if (error_code != 0):
        print("Error listing images")
        exit()
    print(result)

def list_fedcloud_networks(token, site, vo):
    command=('network', 'list')
    error_code, result =  exec_fedcloud_command(token, site, vo, command, True)
    if (error_code != 0):
        print("Error listing IPs")
        exit()
    print(result)

def list_fedcloud_subnets(token, site, vo):
    command=('subnet', 'list')
    error_code, result =  exec_fedcloud_command(token, site, vo, command, True)
    if (error_code != 0):
        print("Error listing subnets")
        exit()
    print(result)

def list_public_IPs(token, site, vo, public_net):
    command=('floating ip', 'list', '--network', public_net)
    error_code, result =  exec_fedcloud_command(token, site, vo, command, True)
    if (error_code != 0):
        print("Error listing public IPs")
        exit()
    print(result)
    return result

def create_fedcloud_keypair(token, site, vo, ssh_key_path, ssh_key_name):
    command=('keypair', 'create', '--public-key', ssh_key_path, ssh_key_name)
    error_code, result =  exec_fedcloud_command(token, site, vo, command, False)
    if (error_code != 0):
        print("Error creating access key")
        exit()
    print(result)

def show_fedcloud_VM(token, site, vo, vm_name):
    command=('server', 'show', vm_name)
    error_code, result = exec_fedcloud_command(token, site, vo, command, True)
    if (error_code != 0):
        print("Error showing the VM")
        exit()
    print(result)


def delete_fedcloud_VM(token, site, vo, vm_name, json_output=False):
    command=('server', 'delete', vm_name)
    error_code, result = exec_fedcloud_command(token, site, vo, command, False)
    if (error_code != 0):
        print("Error deleting the VM")
        exit()
    print(result)


def create_fedcloud_VM(token, site, vo, flavour_selected, image_selected, network_selected, ssh_key_name, vm_name):
    print("Creating VM ...")
    command = ('server', 'create', '--flavor', flavour_selected, '--image', image_selected, '--network', network_selected, '--key-name', ssh_key_name, vm_name)
    print("before call exec_fedcloud_command")
    error_code, result = exec_fedcloud_command(token, site, vo, command, True)
    if (error_code != 0):
        print("Error creating the VM")
        exit()
    print(result)

def get_a_public_IP(token, site, vo, public_network):
    result = list_public_IPs(token, site, vo, public_network)
    pub_net_list = json.loads(result)
    pub_IPs = [x.get('Floating IP Address') for x in pub_net_list if isinstance(x.get("Fixed IP Address"), type(None))]
    #print(pub_IPs)
    if(len(pub_IPs) == 0):
        return 0
    else:
        return pub_IPs[0]

def assign_public_IP_to_VM(token, site, vo, public_IP, vm_name):
    command = ('server', 'add', 'floating', 'ip', vm_name, public_IP)
    error_code, result = exec_fedcloud_command(token, site, vo, command, False)
    if (error_code != 0):
        print("Error assigning IP")
        exit()
    print(result)
    return result

# Execute the OpenStack command on the site/VO with single line of code
# If command finishes correctly, the error_code is 0 and the result is stored
# in JSON object for easy processing
def exec_fedcloud_command(token, site, vo, command, json_output):
    error_code, result = fedcloud_openstack(token, site, vo, command, json_output)

    # Check error code and print the result if OK
    if error_code == 0:
        cmd_output = json.dumps(result, indent=4)
        print(cmd_output)
        return error_code, cmd_output
    else:
        # If error, result is string containing error message
        error_message = "Error message is %s" % result
        print(error_message)
    return error_code, result


#public_network="public00"
#print(get_a_public_IP(token, site, vo, public_network))


