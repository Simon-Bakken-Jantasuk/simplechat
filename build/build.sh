#!/bin/bash

SCRIPT_DIR="$(pwd)"
CHAT_DIR="$SCRIPT_DIR/../chat"
COMMON_DIR="$SCRIPT_DIR/../common" 
TARGET_DIR="$SCRIPT_DIR/django-simplechat" 


if [ ! -d "$CHAT_DIR" ]; then
    echo "CHAT_DIR does not exist: $CHAT_DIR"
    exit 1 
elif [ ! -d "$COMMON_DIR" ]; then 
    echo "COMMON_DIR does not exist: $COMMON_DIR"
    exit 1 
elif [ ! -d "$CHAT_DIR" ] || [ ! -d "$COMMON_DIR" ]; then
    echo "Source directory does not exist: $CHAT_DIR and $COMMON_DIR"
    exit 1
fi 

cp -r "$CHAT_DIR" "$TARGET_DIR/" && cp -r "$COMMON_DIR" "$TARGET_DIR/chat"

sed -i 's/common.utils.simplechat import datetime_message/chat.common.utils.simplechat import datetime_message/' "$TARGET_DIR/chat/consumers.py"

echo "Build complete."
