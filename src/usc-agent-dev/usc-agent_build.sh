#!/bin/bash
FLAG = $1

echo
echo "cd ./external/source/openssl/"
cd ./external/source/openssl/
echo "Building Openssl library"
touch Makefile
make $1
cd ../../../
echo
sleep 2

echo
echo "cd ./common/source/libnetconf"
cd ./common/source/libnetconf/
echo "Building netconf library"
touch Makefile
make $1
cd ../../../
echo
sleep 2

echo
echo "cd ../pyang"
cd ./common/source/pyang
echo "Building Yang model"
make $1
cd ../../../
echo

echo
echo "cd ../server/nc_server/server/"
cd ./server/nc_server/server/
echo "Building Netconf Server"
make $1
echo
sleep 2

echo
echo "cd ../cli/"
cd ../cli/
echo "Building Netconf client"
make $1
echo

sleep 2
echo "cd ../server-sl/"
cd ../server-sl/
echo "Building Netconf Server-sl"
make $1
echo

sleep 2
echo "cd ../transAPI/cfgsystem"
cd ../transAPI/cfgsystem
echo "Building trans API"
make $1
cd ../../../../
echo
sleep 2

echo
echo "cd ../usc-agent/source/agent/"
cd ./usc-agent/source/agent/
patch -p0 <usc-stunnel.patch
echo "Building USC Agent"
touch Makefile
touch src/Makefile

make $1
echo
sleep 2
