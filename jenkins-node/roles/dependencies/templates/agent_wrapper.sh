#!/bin/bash
 
JAVA_HOME=/opt/SUN/jdk1.8.0_
PATH=$PATH:$JAVA_HOME/bin
export PATH
java -jar /var/jenkins/bin/agent.jar


