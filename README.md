\# Agent Workforce Test – Assessment



This repository contains my completed assessment for the Agent Workforce Test.  



\# Tasks Completed

1\. Task 1: Basic Python script execution in Docker.  

2\. Task 2:Processed reservation data and verified January filter.  

3\. Task 3: Generated user/task data and validated output.  

4\. Task 4: Implemented full reservation workflow (create, add services, cancel).  



All tasks were run and validated inside Docker containers.  



```bash

RUN CMD

docker run --rm -it -v "/c/Users/PC/Desktop/agent-workforce-test:/workspace" -w /workspace python:3.10-slim sh -c "cd problems/001 \&\& python agent.py"



