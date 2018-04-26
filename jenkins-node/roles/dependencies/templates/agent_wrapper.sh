#!/bin/bash
 
JAVA_HOME={{ java_path }}
PATH=$PATH:$JAVA_HOME/bin
export PATH
java -jar /var/jenkins/bin/agent.jar


