The goal is this project is two create a simple 1 front-end, 1 back-end server as such:

- Front-end is an EC2 in a public subnet responding to HTTP request. When connecting to HTML user gets a number fetched from the backend.
- Back-end is an EC2 in a private subnet responding to HTTP request, output a random number.

# Architecture

1) Tasks to enable front-end:
    - Create a VPC
    - Create a subnet inside VPC
    - Create an internet gateway and attach to VPC
    - Create and attach a route table that direct traffic to internet gateway
    - Launch EC2 with front-end code in public VPC
    - Check EC2 is accessible from the internet

2) Tasks to enable back-end:
    - Create a subnet inside VPC
    - Create and attach a route table that only route traffic inside VPC
    - Create a NAT gateway to allow EC2 to communicate safely with the internet
    - Launch EC2 with back-end code in private VPC
    - Check front-end EC2 can communicate with back-end EC2
    - Check back-end EC2 is not accessible from the internet

# Security

1) ACLs:
    - In most cases no need to touch ACLs.

1) Security groups
    - Create and attach security group that allows traffic from/to the internet to front-end EC2
    - Create and attach security group that allows traffic from front-end EC2 to back-end EC2

# Authentication

1) Create a role for front-end EC2 to authorize call on back-end EC2

# Best practices recommendation

- Even if VPC default route table enable local traffic by default, attaching a custom local traffic route table to private subnets make intention clear and indirectly document usage.
- Even if route table control traffic, always set-up security groups

# Learnings

- NetworkManager IAM requires both AWS managed 'NetworkManager' policies and 'EC2ReadOnly' policies, otherwise actions like editting subnets settings are blocked
- ACLs are not usually required for security because they are hard to manage at scale. For example outbound http traffic goes to a port initiated by client, thus it will require to open lot of ports on outbound rule of ACL.
- By default security groups block incoming traffic from internet, including ssh port 22 traffic.

