#!/bin/bash
 
JAVA_HOME={{ java_path }}
PATH=$PATH:$JAVA_HOME/jre/bin
export PATH
java -jar /var/jenkins/bin/agent.jar


