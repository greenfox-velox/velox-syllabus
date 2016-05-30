#!/bin/bash
for work_file in works/*.py; do
    cp $work_file 'tests/work.py'
    python3 main.py $(basename $work_file)'.result'
    # echo $(head -n 1 $(basename $work_file)'.result')
    echo $(tail -n 2 $(basename $work_file)'.result')' < '$(basename $work_file)
    rm 'tests/work.py'
done
