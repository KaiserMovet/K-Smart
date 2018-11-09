#!/bin/bash


if [ -f engine/conf.py ]; then
    rm engine/conf.py
    echo "Conf recreated"

fi
cp conf.py engine/config.py
echo -e "\npath = \"`pwd`\"" >> engine/config.py
python3 engine/main.py pwd