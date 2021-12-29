@echo off

Title BTDB2 Exp Grinder Setup
set python_ver=39

echo Welcome to the BTDB2 Exp Grinder Setup
echo This script relies on python to work, make sure you have python 3.9 installed
pause

pip freeze
pip install PyAutoGUI==0.9.53

echo Installation Complete
pause