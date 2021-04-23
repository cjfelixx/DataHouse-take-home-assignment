# DataHouse Take Home Project

## Statements I assumed to solve the problem

* Team members were hired based on some of their attributes.
* Each attributes can range from 0 to 10.
* The company is best in hiring candidates with higher than average attributes.
* In evaluating candidates, there are attributes that are more or less relevant to the other ones . So I incorporated weight coefficients. In a software development company, intelligence and endurance are more important than strength and spicy food tolerance.

## Materials

* Python programming language
* Microsoft Excel to experiment scoring methods.

## Steps

* Using the json python package, convert JSON data from *inputData.json* into a dictionary.
* Convert data into matrix. This is to make this easier with computations.
* For each attributes in the team data, calculate its mean.
* For each applicant and for each of its attribute, calculate *(<average_attribute_value> + <applicant_attribute_value> ) / (<average_attribute_value> + 10)*.
* For each applicant, calculate the weighted average by their attributes.
* Store the score values in a dictionary
* Convert dictionary to JSON into *outputData.json*

## Other notes

* I used list comprehension method often to make the codes a but more concise.
* I made the function *compatibility(data)* for the python computations. JSON to dictionary conversions stayed outside of the function.
* I used the average values in the team data to generalize the team member's attributes.
* The reason why I used *(<average_attribute_value> + <applicant_attribute_value> ) / (<average_attribute_value> + 10)* is to use the ratio of the average team member+applicant to the max possible points, as part of the score.
* In a candidate with all of its attributes 0, the compatibility score will be some positive value due to the *<average_attribute_value>* term in the numerator. This is one of the faults in the scoring method.

## Output

```JSON
{
 "scoredApplicants": [
  {
   "name": "John",
   "score": 0.483
  },
  {
   "name": "Jane",
   "score": 0.602
  },
  {
   "name": "Joe",
   "score": 0.365
  }
 ]
}
```
