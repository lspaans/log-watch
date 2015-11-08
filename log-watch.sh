#!/bin/bash

export ROOT=$(pwd)
export CFG=$ROOT/etc/
export BIN=$ROOT/
export LOG=$ROOT/log/

$BIN/log-watch.py
