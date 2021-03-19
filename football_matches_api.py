#!/bin/python3

import math
import os
import random
import re
import sys


import requests
#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#


def getTotalGoals(team, year):
    URL = 'https://jsonmock.hackerrank.com/api/football_matches'
    params1 = {
        'year' : year,
        'team1' : team}
    params2 = {
        'year' : year,
        'team2' : team}
    response1 = requests.get(URL, params=params1).json()
    response2 = requests.get(URL, params=params2).json()
    
    goles = 0
    for page in range(1,int(response1["total_pages"])+1):
        params1['page'] = page
        res1 = requests.get(URL, params=params1).json()
        for competition in res1['data']:
            goles += int(competition['team1goals'])
    for page in range(1,int(response2["total_pages"])+1):
        params2['page'] = page
        res2 = requests.get(URL, params=params2).json()
        for competition in res2['data']:
            goles += int(competition['team2goals'])
    return goles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)
    
    fptr.write(str(result) + '\n')

    fptr.close()
