    EC2 stands for Elastic Compute Cloud and it is an infrastructure as a service. Some capabilities of EC2 are:
        - Renting virtual machines (EC2)
        - Storing data on virtual drives (EBS)
        - Distributing load across machines (ELB)
        - Scaling services via auto-scaling group (ASG)
    
    Some of the configurations we can choose for EC2 instances:
        - OS: Linux, Windows, MacOS
        - Compute power & cores
        - RAM
        - Storage: network attached(EBS, EFS), hardware(EC2 instance store)
        - Network: network card speed, public ip
        - Firewall rules: security group
        - EC2 User Data which is a bootstrap script

    There are several different EC2 instance types which are optimized for different things:
        - General Purpose
        - Compute Optimized
        - Memory Optimized
        - Accelerated Computing
        - Storage Optimized

    Naming convention for an EC instance is: m5.2xlarge. In this convention:
        - m: instance class
        - 5: generation
        - 2xlarge: size within the instance class

    To compare all different EC2 instances: https://instances.vantage.sh

    Security groups are fundamental means for network security in AWS. They act as a firewall by controlling how
    traffic is allowed into or out of our EC2 instances. Some of their functionality is:
        - Controls inbound traffic(from other to EC2 instance)
        - Controls outbound traffic(from EC2 istance to other)
        - Port access
        - Authorised IP ranges

    A security group can be attached to multiple EC2 instances and one EC2 instance can have multiple security
    groups. They are valid in a region/VPC combination. By default all inbound traffic is blocked and all outbound
    traffic is authorised. 

    By authorizing other security groups in a security group we can provide access to EC2 instance without explicitly
    stating IP addresses. 

    Some useful ports:
        - 21: FTP
        - 22: SSH, SFTP
        - 80: HTTP
        - 443: HTTPS
        - 3389: RDP