# How to add a Public IP to a VMs in EGI

Note: In order to get access to EGI resources, you need to belong to a Virtual Organisation (VO). Some EGI sites support the VO vo.access.egi.eu to facilitate newcomers / begginers to get familiar with EGI. 

Before assigning a public IP you need to find out the public network in the site

`fedcloud openstack --oidc-access-token $OIDC_ACCESS_TOKEN network list --vo <VO> --site <SITE>`


Then you can list the IP available in the public network 

`fedcloud openstack "floating ip" list --network <NETWORK> --oidc-access-token $OIDC_ACCESS_TOKEN --vo <VO> --site <SITE>
`  

The output is a table with the following columns:

<img width="1301" alt="imagen" src="https://user-images.githubusercontent.com/1725775/169075795-bf441b84-839b-4fc6-9397-2bf166613c99.png">

Those Floating IP address with "Fixed IP Address" equal to None are the ones that are available to be assigned to a VM instance.

The command to assigned public IP is:
  
`fedcloud openstack server add floating ip <NAME_VM> <IP> --oidc-access-token $OIDC_ACCESS_TOKEN --vo <VO> --site <SITE>`

