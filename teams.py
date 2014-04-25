#!/usr/bin/env python

import json
import os
import sys
from subprocess import check_call, check_output
import yaml

if len(sys.argv) != 3:
    exit("Usage ./teams.py TEAMS_YAML TEAMS_JSON")

teams_yaml_path = sys.argv[1]
teams_data = sys.argv[2]

with open(teams_yaml_path) as tyd:
    teams1 = yaml.load(tyd)['teams']

with open(teams_data) as tjd:
    teams2 = json.load(tjd)

assert teams1
assert teams2

for tla, _ in teams1.items():
    info = teams2[tla]
    name = info.get('team_name', _['name'])
    print "Generating: '{0}: {1}'.".format(tla, name)
#    open("images/"+name, 'w').close()
    output = check_output(['./signgen', '-s', 'a4-team', '-m', tla, '-i', name, '-o', 'teams-out/' + tla + '.pdf'])
    if output:
        print output
#    break
