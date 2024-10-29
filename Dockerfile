FROM dustynv/ros:noetic-ros-base-l4t-r35.4.1 
RUN apt update && apt install -y git vim tmux

# RUN apt-get update && apt-get install -y sudo
# RUN apt purge 'python3'
RUN apt-get update && apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip &&\
    pip3 install --user --no-cache-dir openai
