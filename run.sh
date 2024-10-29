#!/bin/bash

PWD=`pwd`
docker run --rm -it -v ${PWD}/code:/code rosgpt:latest /bin/bash
