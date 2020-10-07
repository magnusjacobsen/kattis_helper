#!/usr/bin/env bash
PROBLEM=${1?Error: no url given}
python3 ~/git/kattis_helper/src/kattis_helper.py https://open.kattis.com/problems/$PROBLEM
