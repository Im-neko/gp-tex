#!/bin/bash

git pull origin master

cd paper

make clean

cd ..

git add .

git commit -m 'wip'

git push origin master
