# Creation and usage of tokens in EGI 



There are two kinds of tokens:

- Refresh token: It is the main token and it expires in 13 months
- Access token: it is generated from a Refresh token and it expires in 1 hour.

You can get these tokens by accessing this url https://aai.egi.eu/fedcloud/ and provide your institutional credentials.

You can also get these tokens using the command line took oidc-agent (which is availale in the FedCloud CLI toolkit):

Create an Refresh token (valid for 13 month):
`oidc-gen --pub --issuer https://aai.egi.eu/oidc --scope "email eduperson_entitlement eduperson_scoped_affiliation eduperson_unique_id" susana_token` 
The previous command ask you to visit a web page where you will get a code, which is required to complete the token generation

Renew Access token (valid for 1 hour):
`oidc-token susana_token`


