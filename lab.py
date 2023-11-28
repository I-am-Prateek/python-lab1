
#taking input from the user

name=input("Patient's name:")
visited=input("Has the patient been here before (y/n)?:")
height=int(input("What is the patient’s height (in cm)?:"))
current_weight=float(input("What is the patient’s weight (in kg)?:"))
last_weighted_date=input("When was the patient last weighed in(DD/MM/YYYY):")
last_weight=float(input("Whan was the patient last weighed:"))
overall_assessment=int(input("Practitioner’s overall assessment of the patient’s health:"))

if last_weight==-1:
    weight_changed=0
else:
    weight_changed= last_weight-current_weight

#bmi calculation
bmi=((current_weight/ (height**2)) * 10000)
bmi=round(1)

#conditions applying for bmi
if bmi>30:
    result="Obese"
elif 25<= bmi<=29.9:
      result="overweight"
elif 18.5<= bmi <=24.9:
      result="Healthy"
elif 17<= bmi <=18.4:
      result="underweight"
else:
      result="too-thin"

#intermediate health score

if result==["obese","too-thin"]:
    intermediate_health_score=0
elif result==["overweight","underweight"]:
    intermediate_health_score=3
else:
   intermediate_health_score=5

#intermediate health score

#overall final health score calculator 
if weight_changed==0:
    intermediate_health_score= intermediate_health_score+1
elif weight_changed<1:
    intermediate_health_score=-intermediate_health_score-1
elif weight_changed>1:
    intermediate_health_score=intermediate_health_score+2

#calculating the change in weightpgg 

intermediate_health_score= intermediate_health_score+overall_assessment
final_health_score= intermediate_health_score
#printing the total output
 #simple receipt from Melanie Dental Clinic
print("Melanie Dental Clinic")
print("****************************")
print("Name:",name)
print("Patient height:",height,"cm")
print("Patient weight:",current_weight,"Kg")
print("Patient weight loss:",weight_changed)
print("-------------------------------------")
#For calculating BMI
  
print("BMI=",bmi)
print("Health Assessment:",intermediate_health_score)
print("-------------------------------------")
print("Overall:",final_health_score)

if final_health_score > 5:
    print("Great condition!")
elif 3 <= final_health_score <= 5:
    print("Need a little work")
elif 1 <= final_health_score < 3:
    print("Need a lot of work")
else:
    print("Patient is 'At risk!'")
   
