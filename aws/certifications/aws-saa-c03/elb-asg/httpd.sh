#!/bin/bash

yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
EC2_AZ=$(curl curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
echo "<h1>Hello World from $(hostname -f)</h1> in AZ $EC2_AZ" > /var/www/html/index.html