# How to access a VM created in EGI using keypairs

First you need to create a keypair by providing your public key

`fedcloud openstack --oidc-access-token $OIDC_ACCESS_TOKEN keypair create --public-key <PATH_TO_PUBLIC_KEY> <NAME_FOR_THE_KEYPAIR> --VO <VO> --site <SITE>
`  

Then you can create a VM with this keypair assigned or add it to your existing VM.
This is the command to create a VM with a keypair.

`fedcloud openstack --oidc-access-token $OIDC_ACCESS_TOKEN server create --flavor <FLAVOR> --image <IMAGE> --key-name <NAME_FOR_THE_KEYPAIR> --network <NETWORK> --VO <VO> --site <SITE>`

The public key will be associated with the default user of the VM. You need to find out what is the default user. In EGI it seems that VMs based on Ubuntu image the defaul user is 'ubuntu'

