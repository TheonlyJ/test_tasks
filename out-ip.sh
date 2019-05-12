#!/bin/bash

ip -o route get 8.8.8.8 | sed 's/.*src \([^ ]\+\) .*/\1/'
