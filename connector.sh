#!/bin/bash

if [ -z $1 ]; then
    echo -e "You must supply domain name,---> #./connector.sh domain_name"
    exit 100
fi
domain_name=$1
while [[ $domain_name = "" ]]; do
    echo "please enter non-empty, correct domain-->"
    read domain_name
done
ssh -i "your key with absolute path " ubuntu@$domain_name
exit 0
