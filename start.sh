#!/bin/bash
echo "$OS_PASSWORD"
source openrc-2b547e4137ab40ac871ffbdbc5d9f3e9-jp2 < password
echo "$OS_PASSWORD"
echo Server_Start
python3 app.py