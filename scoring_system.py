# This file will score the data of the school

# psuuedocode : THIS WILL BE SCORED IN MULTIPLE PASSES OF DIFFERENT FUNCTIONS

# MIDDLESCHOOL SCORING ALGORITHM: 

#Let's score the middleschools based on these three things
#Academic Score 50 pts
#Health and Safety Score - 25 pts (BASED ON IN SCHOOL SAFETY AND HEALTH)
#Neighborhood Score - 25 pts (BASED ON OUTSIDE ACCIDENTS IN AREA)

# USING 2021 DOE Middle School Directory :    ---- Using a 7 as a checkmark
# 1. Get the middleschool file from the __path__ 7
# 2. Use that file's data to find certain attributes relevent to scoring including elaprof and mathprof 7   

# 3. Does it offer any accelerated math classes or computer science? 
# 4. Accessibility? - maybe not idk
# 5. Survey safety? 

# Show those top 3 highschools? Maybe Or maybe Top 1 is good enough. Gives a decent estimate based on that. 

# USING THE 2021 - 2022 Average Class Size by School (and Grade): 
# 1. Find the average class size and maximum class size for the span of school grades 
# Eg: Pre-K - First Grade , 2nd - 5th , 6th - 8th  
# 2. Using the average for the school indicated, show the class average as well as score based on :
#     -Less is more. Less students means less distraction from the teacher's lesson.

#     THINK ON THIS ONE
#     We want a class size within 3 students of 15 for the best, within 10 of 15  for second best
#     Anything above 25 can be distracting so that is seen as too many. 
#     Less than 10 students is seen as too little for socialization.  

# USING DOHMH School Cafeteria Inspections (2020-Present): 
# 1. Was there any inspection of the cafeteria on record and was there a violation? 

#----------------------------------------------------------------------------------------------
# # Course pass rate --- I USED THIS TO GET THE MEAN AND MEDIAN PASS RATES
# coursePassRateColumn = schoolDirectory["coursepassrate"]

# coursePassRateText = coursePassRateColumn.astype(str).str.replace("%", "", regex=False)
# coursePassRateNumbers = pd.to_numeric(coursePassRateText, errors="coerce")

# # Count the schools that have a usable number. NaN values are not counted.
# numberOfSchoolsWithRate = coursePassRateNumbers.count()

# # Mean (average): add up every pass rate, then divide by how many there are.
# meanCoursePassRate = coursePassRateNumbers.mean()

# # Median: sort all the pass rates from lowest to highest and take the middle one.
# # If there's an even number of schools, it averages the two middle values.
# medianCoursePassRate = coursePassRateNumbers.median()

# print(f"Schools with a pass rate: {numberOfSchoolsWithRate}")
# print(f"Mean course pass rate: {meanCoursePassRate:.2f}")
# print(f"Median course pass rate: {medianCoursePassRate:.2f}")

#--------------------------------------------------------------------------------------------
#DATA : 
# Schools with a pass rate: 468
# Mean course pass rate: 91.67
# Median course pass rate: 94.00

#-----------------------------------------------------------------------------
#if acceleratedclasses contains algebra I or geometry, that is considered the highest math class. 
#Geometry is greater than algebra I
#-----------------------------------------------------------------------------


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


#traverse through the list looking for the school name selected or maybe this can be an 0(1) operation
#Then show and save the 'elaprof' and 'mathprof' scores from the columns named the same as in the previous quotations
#for that specific name 
#then once saved into seperate variables, that is all. 


# Read the CSV into a DataFrame, a table in memory with rows and named columns.
# Relative path: starts from the folder you run the script in (the project folder)
schoolDirectory = pd.read_csv("data/2021_DOE_Middle_School_Directory_20261107.csv")


# ---------------------------------------------------------------------------
# STEM LETTER FUNCTION
# Takes ONE school's row (a single record) and returns S, T, E, M as True/False.
# ---------------------------------------------------------------------------
def checkStemLetters(selectedSchoolRow):
    # Get the two class lists as text. An empty cell becomes "" so nothing crashes.
    electiveText = "" if pd.isna(selectedSchoolRow["electiveclasses"]) else str(selectedSchoolRow["electiveclasses"])
    acceleratedText = "" if pd.isna(selectedSchoolRow["acceleratedclasses"]) else str(selectedSchoolRow["acceleratedclasses"])

    # Join both lists and make everything lowercase so capital letters don't matter.
    allClassText = (electiveText + ", " + acceleratedText).lower()

    # S = science. Remove "computer science" first so it doesn't count as regular science.
    textWithoutComputerScience = allClassText.replace("computer science", "")
    scienceWords = ["science", "living environment", "chemistry", "physics"]
    hasScience = any(word in textWithoutComputerScience for word in scienceWords)

    # T = technology: computer science, robotics, or technology.
    hasTechnology = ("computer science" in allClassText
                     or "robotics" in allClassText
                     or "technology" in allClassText)

    # E = engineering.
    hasEngineering = "engineering" in allClassText

    # M = math. Algebra and geometry are math classes too.
    mathWords = ["math", "algebra", "geometry"]
    hasMath = any(word in allClassText for word in mathWords)

    # Return the four True/False results with labels.
    return {"S": hasScience, "T": hasTechnology, "E": hasEngineering, "M": hasMath}


# The school we want to look up. It must match the file's spelling exactly.
#**************************
####THIS IS WHERE WE INSERT THE INFO FROM THE ZIPCODE DATA.  THIS NEEDS TO BE CONNECTED TO THAT AND ALSO RUN THIS FUNCTION 
#AS A FOR LOOP SO THAT ALL THE SCHOOLS THAT ARE IN THE ZIPCODE WE SEARCHED CAN BE EVALUATED 
#schoolNameToFind = "EXAMPLE MIDDLE SCHOOL"
#*******************************
schoolNameToFind = "P.S. 034 Franklin D. Roosevelt" #sample

# Step 1: Build a True/False "mask," one True or False per row.
# True means that row's school name matches. Think of it as running your finger
# down a class roster and checking off the one name you're looking for.
isMatchingSchool = schoolDirectory["name"] == schoolNameToFind

# Step 2: Keep only the rows where the mask is True.
matchingSchoolRows = schoolDirectory[isMatchingSchool]

# Safety check: if nothing matched, stop with a clear message
# instead of failing later with a confusing error.
if matchingSchoolRows.empty:
    raise ValueError(f"No school named '{schoolNameToFind}' was found.")

# Step 3: Take the first matching row. A row is a Series, a single record
# holding that school's values for every column.
selectedSchoolRow = matchingSchoolRows.iloc[0]

# Step 4: Pull out the scores and save each one in its own variable.
elaProficiencyScore = selectedSchoolRow["elaprof"]
mathProficiencyScore = selectedSchoolRow["mathprof"]
surveyedSafety = selectedSchoolRow["surveysafety"]

# Step 5: Run the STEM check on this same school's row.
# It returns a dictionary, so stemLetters["S"] gives the science result, and so on.
stemLetters = checkStemLetters(selectedSchoolRow)

# Show the results
print(f"{schoolNameToFind} Survey Safety: {surveyedSafety}")
print(f"{schoolNameToFind} ELA proficiency: {elaProficiencyScore}")
print(f"{schoolNameToFind} Math proficiency: {mathProficiencyScore}")
print(f"{schoolNameToFind} STEM letters: {stemLetters}")

#------------------------------------------------------------------------
#for safety we should just have percent of crashes by zipcode 
