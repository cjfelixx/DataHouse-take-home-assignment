""" This is the main drive for the compatibility score project

"""

__author__ = 'Clyde James Felix'

import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def compatibilityScore(data):
	''' Determines the score of an applicant
	'''
	teamData = data["team"]
	applicantsData = data["applicants"]

	numTeam = len(teamData)
	numApplicants = len(applicantsData)

	# Transforming data into matrix to do things clean
	teamIntelligence = [teamData[i]["attributes"]["intelligence"] for i in range(numTeam)]
	teamStrength =  [teamData[i]["attributes"]["strength"] for i in range(numTeam)]
	teamEndurance = [teamData[i]["attributes"]["endurance"] for i in range(numTeam)]
	teamSpicyFoodTolerance = [teamData[i]["attributes"]["spicyFoodTolerance"] for i in range(numTeam)]

	applicantsIntelligence = [applicantsData[i]["attributes"]["intelligence"] for i in range(numApplicants)]
	applicantsStrength =  [applicantsData[i]["attributes"]["strength"] for i in range(numApplicants)]
	applicantsEndurance = [applicantsData[i]["attributes"]["endurance"] for i in range(numApplicants)]
	applicantsSpicyFoodTolerance = [applicantsData[i]["attributes"]["spicyFoodTolerance"] for i in range(numApplicants)]

	teamDataProcessed = [teamIntelligence,teamStrength,teamEndurance,teamSpicyFoodTolerance]
	applicantsDataProcessed = [applicantsIntelligence,applicantsStrength,applicantsEndurance,applicantsSpicyFoodTolerance]

	# Taking average attributes of the team
	avgTeam = [sum(teamDataProcessed[i])/numTeam for i in range(len(teamDataProcessed))]

	# Calculating scores
	weightCoefficients = [0.5, 0.1, 0.25, 0.05]
	score = []
	for applicants in range(numApplicants):
		
		score.append(sum([weightCoefficients[i]*((applicantsDataProcessed[i][applicants]+avgTeam[i])/(avgTeam[i]+10)) for i in range(len(weightCoefficients))]))
	
	# Rounding score values
	score = [round(s,3) for s in score]
	
	# Storing scores in a dictionary
	outputData = {}
	outputData["scoredApplicants"] = [{"name": applicantsData[i]["name"],"score":score[i]} for i in  range(len(applicantsData))]

	return outputData

if __name__ == "__main__":
	# Converting JSON to dict
	with open('sampleData.json') as file:
		data = json.load(file)

	# Calculate score 
	score = compatibilityScore(data)
	print("score\n",score)

	# Converting score dict to JSON
	with open('outputData.json','w') as outfile:
		json.dump(score,outfile,indent=1)


	