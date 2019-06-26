#!/bin/bash
FOLDER_PATH="$PWD/data/$(date +%Y%m%d_%H%M%S)"
mkdir $FOLDER_PATH
sleep 1
roslaunch gestures_dataset_collection interface.launch --dump-param path:=$FOLDER_PATH > "$FOLDER_PATH/param.yaml"
sleep 1
roslaunch gestures_dataset_collection interface.launch path:=$FOLDER_PATH 
python script/data_analysis.py $FOLDER_PATH