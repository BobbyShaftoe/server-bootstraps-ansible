#!/usr/bin/env bash

### TO BE PORTED TO ANSIBLE ###

yum update -y
yum groupinstall -y 'Development Tools'
yum install -y libcurl-devel openssl-devel libxml2-devel

rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm


rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/blas-3.4.2-8.el7.x86_64.rpm
rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/blas-devel-3.4.2-8.el7.x86_64.rpm
rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/lapack-3.4.2-8.el7.x86_64.rpm
rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/lapack-devel-3.4.2-8.el7.x86_64.rpm
rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/texlive-base-2012-38.20130427_r30134.el7.noarch.rpm
rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/texlive-kpathsea-lib-2012-38.20130427_r30134.el7.x86_64.rpm
rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/texlive-kpathsea-svn28792.0-38.el7.noarch.rpm
rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/texlive-kpathsea-bin-svn27347.0-38.20130427_r30134.el7.x86_64.rpm
rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/texlive-epsf-svn21461.2.7.4-38.el7.noarch.rpm
rpm -ivh http://mirror.centos.org/centos/7/os/x86_64/Packages/texinfo-tex-5.1-4.el7.x86_64.rpm



yum update -y
yum groupinstall -y 'Development Tools'
yum install -y libcurl-devel openssl-devel libxml2-devel

curl -O https://download2.rstudio.org/rstudio-server-rhel-1.1.423-x86_64.rpm
yum localinstall -y rstudio-server-rhel-1.1.423-x86_64.rpm

sudo groupadd r-user
sudo useradd -m -b /home -g r-user r-user
