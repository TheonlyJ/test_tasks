#!/bin/bash
cat file.txt | grep -oE '\b[[:digit:]]?[13579]\b'

