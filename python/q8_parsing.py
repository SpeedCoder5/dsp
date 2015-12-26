# The football.csv file contains the results from the English Premier League.
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in 'for' and 'against' goals.
# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.
#
# def read_data(data):
#     # COMPLETE THIS FUNCTION
#     raise NotImplementedError
#
# def get_min_score_difference(self, parsed_data):
#     # COMPLETE THIS FUNCTION
#     raise NotImplementedError
#
# def get_team(self, index_value, parsed_data):
#     # COMPLETE THIS FUNCTION
#     raise NotImplementedError

import csv

csvFilename = 'football.csv'
minDeltaGoals = float("inf")
minDeltaTeam = ''

with open(csvFilename) as fin:
    drdr = csv.DictReader(fin)
    for row in drdr:
        deltaGoals = abs(int(row['Goals']) - int(row['Goals Allowed']))
        if deltaGoals < minDeltaGoals:
            minDeltaGoals = deltaGoals
            minDeltaTeam = row['Team']
print "%s had the smallest difference with of %d between 'for' and 'against' goals." % (minDeltaTeam, minDeltaGoals)