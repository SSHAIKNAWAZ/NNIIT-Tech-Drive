# NNIIT-Tech-Drive

## INSTRUCTIONS
`Once you are done with your code. Push your code to your github account
Make the repository public. Write a Readme for installation/running or any other information
Test if it's accessible publicly.
Share the repository link in the google form provided
PROBLEM
Build a backend API that classifies a student’s question into one of the predefined topics: Math, Science, or English.
Part 1: Backend API (Create a REST endpoint):`


# POST /classify-question


`Input JSON:
 { "question": "What is the Pythagorean theorem?" }`
 


`Output JSON:
 { "topic": "Math", "confidence": 0.93 }
`

Requirements:


- Technical Language: Any language you can work with
- Validate Input 
- Handle Error Cases

# Part 2: Classification Logic 

Use any method that you want for classification logic:
Option 1 Can be Rule-based :
Option 2 Any Pre-trained model or trained model:

If you are training the model, you need to figure out the data

# Bonus:
Save all incoming questions + results in a local questions.json file for logging
Support a GET /questions endpoint to list past classified questions.



