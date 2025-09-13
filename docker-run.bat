


@echo off
REM Usage: docker-run problems/001
set problem=%1
set winpath=%cd%

echo Running problem: %problem%
echo Host path: %winpath%

docker run --rm -it -v "/c/Users/PC/Desktop/agent-workforce-test:/workspace" -w /workspace --env-file "%winpath%\.env" python:3.10-slim sh -c "cd %1 && python agent.py"
