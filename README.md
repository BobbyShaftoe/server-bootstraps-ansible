# server-bootstraps-ansible

### Overview

This repo is a collection of configuration sets for bootstraping new servers that will have a specific role.
These are all generally based around Ansible playbooks for configuration management driven deployments.

The Ansible configuration for each deployment has a logical layout as roles that contain the tasks for:

* setting up the operating system
  * creating/managing users
  * configuring os parameters such as system limits
  * setting hostname, or making entries to the hosts file
* installing
  * any dependencies such as required libs, development languages or tools
  * the necessary applications such as web, proxy or application servers
* application configuration
  * rendering templates and/or copying files into place
  * Creating and configuring service management definitions
  * managing entries in existing configuration file for the newly installed applications
* tests

_These playbooks are designed to be run locally, however the configuration for each server is managed through:_

```group_vars/```

### For example:

**The Ansible hosts file**

```
[local]
localhost ansible_connection=local

[jenkins]
localhost ansible_connection=local

[jenkins-node]
localhost ansible_connection=local

[R]
localhost ansible_connection=local
```

**The corresponding layout**

```
group_vars/jenkins-node
```

```
hostname_prefix: jenkins-node
hostname: hn-development.net
packages:
  - 'java-1.8.0'
  - 'git'
  - 'ntpdate'
artefact_src_path: 'https://s3.amazonaws.com/artefact-bucket-store'
arefact_paths:
  - [ 'jenkins-node/agent.jar', '/agent' ]
  - [ 'jenkins-node/agent_wrapper.sh', '/usr/local/sbin' ]
users_groups:
  - [ 'jenkins', 'jenkins', '/home/jenkins' ] 
```





**In the playbook**

```
- name: Epel-Release, Create Users, Direcories, Hostnames
  hosts: "jenkins-node"
  remote_user: ansible
  become: True
  gather_facts: True
  roles:
    - "os"
    - "users"
    - "filesystem"
```

```
- name: Install Epel-Release, Docker, HAProxy, Python, Certbot, Tools
  hosts: "jenkins-node"
  remote_user: ansible
  become: True
  gather_facts: True
  roles:
    - "dependencies"
    - "applications"
```

```
- name: Post Install, Final Deployment Actions
  hosts: "jenkins-node"
  remote_user: ansible
  become: True
  gather_facts: True
  roles:
    - "services"
    - "tests"
```

_The standard convention for tasks in any role is the_ ```main.yml``` _file includes the respectively named file for each task._

### For example:

**The** ```main.yml``` **file within the task folder for any role**

```
- include: docker-py.yml
- include: boto.yml
- include: passlib.yml
- include: bcrypt.yml
```

### Details on available setups

* R
  * Install all dependencies (group install 'Development Tools', and others), create users, install rstudio 
* jenkins
  * Install Java JDK, Plugins, and dependencies  
* jenkins-node
  * Install Java JRE, agent.jar, agent wrapper script, and build dependencies for jobs




