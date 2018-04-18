#!/usr/bin/env bash

exec 1>/var/bootstrap.log
exec 2>/var/bootstrap_error.log

yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum -y update

yum -y install ansible
yum -y install git

exec &>/dev/tty


ansible --version | tee -a /var/bootstrap.log


