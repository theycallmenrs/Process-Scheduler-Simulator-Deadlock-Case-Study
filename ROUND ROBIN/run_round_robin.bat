@echo off
REM Run the self-contained ROUND ROBIN CLI from this folder
pushd %~dp0
py -3 round_robin.py %*
popd
