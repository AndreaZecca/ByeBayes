import random
import decimal
import csv


#IS RECoMMENDED TO KEEP THE VALUE OF ORDER BETWEEN 6 AND 1
order = 6
fixedProbabilities = False

def decs(number):
    d = decimal.Decimal(str(number))
    return abs(d.as_tuple().exponent)

alpha = 1
if(fixedProbabilities == True):
    alpha = 2

genderProb = {}
genderProb [ "female"] = 0.4959
genderProb ["male"] = 0.5041

ageProb = {}
ageProb ["young"] = 0.3188
ageProb ["adult"] = 0.5995
ageProb ["old"] = 0.0817

fallsProb = {}
fallsProb ["youngfemalefalse"] = 0.14037 * alpha
fallsProb ["adultfemalefalse"] = 0.06380 * alpha
fallsProb ["oldfemalefalse"] = 0.12761 * alpha
fallsProb ["youngmalefalse"] = 0.18288 * alpha
fallsProb ["adultmalefalse"] = 0.08313 * alpha
fallsProb ["oldmalefalse"] = 0.16626 * alpha
fallsProb ["youngfemaletrue"] = 0.14037 * alpha
fallsProb ["adultfemaletrue"] = 0.08520 * alpha
fallsProb ["oldfemaletrue"] = 0.15 * alpha
fallsProb ["youngmaletrue"] = 0.08313 * alpha
fallsProb ["adultmaletrue"] = 0.10411 * alpha
fallsProb ["oldmaletrue"] = 0.18336 * alpha

poisoningProb = {}
poisoningProb ["youngfemale"] = 0.008901 * alpha
poisoningProb ["adultfemale"] = 0.0079 * alpha
poisoningProb ["oldfemale"] = 0.002967 * alpha
poisoningProb ["youngmale"] = 0.01 * alpha
poisoningProb ["adultmale"] = 0.00928 * alpha
poisoningProb ["oldmale"] = 0.003483 * alpha

natureForceProb = 0.0141

othInjuriesProb = {}
othInjuriesProb ["youngfemale"] = 0.00111 * alpha
othInjuriesProb ["adultfemale"] = 0.0000668 * alpha
othInjuriesProb ["oldfemale"] = 0.000280 * alpha
othInjuriesProb ["youngmale"] = 0.000151 * alpha
othInjuriesProb ["adultmale"] = 0.000160 * alpha
othInjuriesProb ["oldmale"] = 0.000328 * alpha

transportIncidentProb = {}
transportIncidentProb ["youngfemalefalse"] = 0.01 * alpha
transportIncidentProb ["adultfemalefalse"] = 0.057 * alpha
transportIncidentProb ["oldfemalefalse"] = 0.027 * alpha
transportIncidentProb ["youngmalefalse"] = 0.018 * alpha
transportIncidentProb ["adultmalefalse"] = 0.09 * alpha
transportIncidentProb ["oldmalefalse"] = 0.038 * alpha
transportIncidentProb ["youngfemaletrue"] = 0.0152 * alpha
transportIncidentProb ["adultfemaletrue"] = 0.08664 * alpha
transportIncidentProb ["oldfemaletrue"] = 0.04104 * alpha
transportIncidentProb ["youngmaletrue"] = 0.02736 * alpha
transportIncidentProb ["adultmaletrue"] = 0.1368 * alpha
transportIncidentProb ["oldmaletrue"] = 0.05776 * alpha

selfHarmAndViolenceProb = {}
selfHarmAndViolenceProb ["youngfemale"] = 0.00021 * alpha
selfHarmAndViolenceProb ["adultfemale"] = 0.01195 * alpha
selfHarmAndViolenceProb ["oldfemale"] = 0.008 * alpha
selfHarmAndViolenceProb ["youngmale"] = 0.00042 * alpha
selfHarmAndViolenceProb ["adultmale"] = 0.0239 * alpha
selfHarmAndViolenceProb ["oldmale"] = 0.016 * alpha

respiratoryInfectionProb = {}
respiratoryInfectionProb ["youngfemale"] = 0.41500 * alpha
respiratoryInfectionProb ["adultfemale"] = 0.180000 * alpha
respiratoryInfectionProb ["oldfemale"] = 0.247800 * alpha
respiratoryInfectionProb ["youngmale"] = 0.332000 * alpha
respiratoryInfectionProb ["adultmale"] = 0.144000 * alpha
respiratoryInfectionProb ["oldmale"] = 0.198240 * alpha

cardiovascularDiseaseProb = {}
cardiovascularDiseaseProb ["youngfemale"] = 0.0036 * alpha
cardiovascularDiseaseProb ["adultfemale"] = 0.0084 * alpha
cardiovascularDiseaseProb ["oldfemale"] = 0.036 * alpha
cardiovascularDiseaseProb ["youngmale"] = 0.084 * alpha
cardiovascularDiseaseProb ["adultmale"] = 0.0476 * alpha
cardiovascularDiseaseProb ["oldmale"] = 0.0204 * alpha

malignacyProb = {}
malignacyProb ["youngfemale"] = 0.002000 * alpha
malignacyProb ["adultfemale"] = 0.065700 * alpha
malignacyProb ["oldfemale"] = 0.168300 * alpha
malignacyProb ["youngmale"] = 0.002400 * alpha
malignacyProb ["adultmale"] = 0.078840 * alpha
malignacyProb ["oldmale"] = 0.201960 * alpha

othSicknessProb = {}
othSicknessProb ["youngfemale"] = 0.00226 * alpha
othSicknessProb ["adultfemale"] = 0.00111 * alpha
othSicknessProb ["oldfemale"] = 0.0145 * alpha
othSicknessProb ["youngmale"] = 0.00280 * alpha
othSicknessProb ["adultmale"] = 0.00287 * alpha
othSicknessProb ["oldmale"] = 0.0171 * alpha

unintentionalInjuriesProb = {}
unintentionalInjuriesProb ["truetruetrue" ] = 0.001460018 * alpha
unintentionalInjuriesProb ["truetruefalse" ] = 0.00145122 * alpha
unintentionalInjuriesProb ["truefalsetrue" ] = 0.001362798 * alpha
unintentionalInjuriesProb ["truefalsefalse" ] = 0.001354 * alpha
unintentionalInjuriesProb ["falsetruetrue" ] = 0.000106018 * alpha
unintentionalInjuriesProb ["falsetruefalse" ] = 0.00009722 * alpha
unintentionalInjuriesProb ["falsefalsetrue" ] = 0.000008798 * alpha
unintentionalInjuriesProb ["falsefalsefalse" ] = 0.00000001 * alpha

sicknessProb = {}
sicknessProb ["truetruetrue" ] = 0.05344 * alpha
sicknessProb ["truetruefalse" ] = 0.044026 * alpha
sicknessProb ["truefalsetrue" ] = 0.022126 * alpha
sicknessProb ["truefalsefalse" ] = 0.006356 * alpha
sicknessProb ["falsetruetrue" ] = 0.05344 * alpha
sicknessProb ["falsetruefalse" ] = 0.03767 * alpha
sicknessProb ["falsefalsetrue" ] = 0.01577 * alpha
sicknessProb ["falsefalsefalse" ] = 0.0001 * alpha

deathProb = {}
deathProb [ "truetruetruetruetruetrue" ] = 0.9999
deathProb [ "truetruetruetruetruefalse" ] = 0.81 
deathProb [ "truetruetruetruefalsetrue" ] = 0.75 
deathProb [ "truetruetruetruefalsefalse" ] = 0.56 
deathProb [ "truetruetruefalsetruetrue" ] = 0.85 
deathProb [ "truetruetruefalsetruefalse" ] = 0.66 
deathProb [ "truetruetruefalsefalsetrue" ] = 0.6 
deathProb [ "truetruetruefalsefalsefalse" ] = 0.41 
deathProb [ "truetruefalsetruetruetrue" ] = 0.9 
deathProb [ "truetruefalsetruetruefalse" ] = 0.71
deathProb [ "truetruefalsetruefalsetrue" ] = 0.65 
deathProb [ "truetruefalsetruefalsefalse" ] = 0.46 
deathProb [ "truetruefalsefalsetruetrue" ] = 0.75
deathProb [ "truetruefalsefalsetruefalse" ] = 0.56 
deathProb [ "truetruefalsefalsefalsetrue" ] = 0.5 
deathProb [ "truetruefalsefalsefalsefalse" ] = 0.3
deathProb [ "truefalsetruetruetruetrue" ] = 0.85 
deathProb [ "truefalsetruetruetruefalse" ] = 0.66
deathProb [ "truefalsetruetruefalsetrue" ] = 0.6 
deathProb [ "truefalsetruetruefalsefalse" ] = 0.41
deathProb [ "truefalsetruefalsetruetrue" ] = 0.7
deathProb [ "truefalsetruefalsetruefalse" ] = 0.5
deathProb [ "truefalsetruefalsefalsetrue" ] = 0.44
deathProb [ "truefalsetruefalsefalsefalse" ] = 0.25
deathProb [ "truefalsefalsetruetruetrue" ] = 0.75
deathProb [ "truefalsefalsetruetruefalse" ] = 0.56
deathProb [ "truefalsefalsetruefalsetrue" ] = 0.5
deathProb [ "truefalsefalsetruefalsefalse" ] = 0.3
deathProb [ "truefalsefalsefalsetruetrue" ] = 0.59
deathProb [ "truefalsefalsefalsetruefalse" ] = 0.4
deathProb [ "truefalsefalsefalsefalsetrue" ] = 0.34
deathProb [ "truefalsefalsefalsefalsefalse" ] = 0.15
deathProb [ "falsetruetruetruetruetrue" ] = 0.85
deathProb [ "falsetruetruetruetruefalse" ] = 0.66
deathProb [ "falsetruetruetruefalsetrue" ] = 0.6
deathProb [ "falsetruetruetruefalsefalse" ] = 0.41
deathProb [ "falsetruetruefalsetruetrue" ] = 0.7
deathProb [ "falsetruetruefalsetruefalse" ] = 0.5
deathProb [ "falsetruetruefalsefalsetrue" ] = 0.44
deathProb [ "falsetruetruefalsefalsefalse" ] = 0.25
deathProb [ "falsetruefalsetruetruetrue" ] = 0.75 
deathProb [ "falsetruefalsetruetruefalse" ] = 0.56 
deathProb [ "falsetruefalsetruefalsetrue" ] = 0.5
deathProb [ "falsetruefalsetruefalsefalse" ] = 0.3
deathProb [ "falsetruefalsefalsetruetrue" ] = 0.59
deathProb [ "falsetruefalsefalsetruefalse" ] = 0.4
deathProb [ "falsetruefalsefalsefalsetrue" ] = 0.34 
deathProb [ "falsetruefalsefalsefalsefalse" ] = 0.15
deathProb [ "falsefalsetruetruetruetrue" ] = 0.7 
deathProb [ "falsefalsetruetruetruefalse" ] = 0.5 
deathProb [ "falsefalsetruetruefalsetrue" ] = 0.44
deathProb [ "falsefalsetruetruefalsefalse" ] = 0.25
deathProb [ "falsefalsetruefalsetruetrue" ] = 0.54
deathProb [ "falsefalsetruefalsetruefalse" ] = 0.35
deathProb [ "falsefalsetruefalsefalsetrue" ] = 0.29
deathProb [ "falsefalsetruefalsefalsefalse" ] = 0.1
deathProb [ "falsefalsefalsetruetruetrue" ] = 0.59 
deathProb [ "falsefalsefalsetruetruefalse" ] = 0.4
deathProb [ "falsefalsefalsetruefalsetrue" ] = 0.34
deathProb [ "falsefalsefalsetruefalsefalse" ] = 0.15
deathProb [ "falsefalsefalsefalsetruetrue" ] = 0.44
deathProb [ "falsefalsefalsefalsetruefalse" ] = 0.25
deathProb [ "falsefalsefalsefalsefalsetrue" ] = 0.19
deathProb [ "falsefalsefalsefalsefalsefalse" ] = 0.0001

def datasetConstructor():
    ageGroups = ["young","adult","old"]
    genderGroups = ["female","male"]
    ageGroupIndex = 0
    genderIndex = 0

    ageTresholds = []
    ageTresholds.append(int((10**order)*ageProb ["young"]))
    ageTresholds.append(int((10**order)*ageProb ["adult"]) + int((10**order)*ageProb ["young"]))

    genderTresholds = []
    genderTresholds.append(int((10**order)*ageProb ["young"]*genderProb ["female"]))
    genderTresholds.append(int((10**order)*ageProb ["young"]))
    genderTresholds.append(int((10**order)*ageProb ["adult"]*genderProb ["female"]) + int((10**order)*ageProb ["young"]))
    genderTresholds.append(int((10**order)*ageProb ["adult"]) + int((10**order)*ageProb ["young"]))
    genderTresholds.append(int((10**order)*ageProb ["old"]*genderProb ["female"]) + int((10**order)*ageProb ["young"]) + int((10**order)*ageProb ["adult"]))

    with open('./data/dataset.csv', 'w') as file:
        writer = csv.writer(file)
        headerLine = ["ID","Age-range","Gender","Falls","Poisonings","Nature-force","Cardiovascular-disease","Malignancy","Respiratory-infection","Transport-incident","Sickness","Other-injuries","Unintentional-injuries","Other-sickness","SHV","Death"]
        writer.writerow(headerLine)
        for i in range(1,(10**order)+1):

            data = []

            if ( i in ageTresholds ):
                ageGroupIndex = ageGroupIndex + 1
            if ( i in genderTresholds ):
                genderIndex = 1 - genderIndex

            gender = genderGroups[genderIndex]
            age = ageGroups[ageGroupIndex]

            data.append(i)
            data.append(str(age))
            data.append(str(gender))
            
            poisonings = ( round(random.uniform(0, 1), decs(poisoningProb[age+gender])) <= poisoningProb[age+gender] )
            natureForce = ( round(random.uniform(0, 1), decs(natureForceProb)) <= natureForceProb )
            cardiovascularDisease = ( round(random.uniform(0, 1), decs(cardiovascularDiseaseProb[age+gender])) <= cardiovascularDiseaseProb[age+gender] )
            malignacy = ( round(random.uniform(0, 1), decs(malignacyProb[age+gender])) <= malignacyProb[age+gender] )
            respiratoryInfection = ( round(random.uniform(0, 1), decs(respiratoryInfectionProb[age+gender])) <= respiratoryInfectionProb[age+gender] )
            othInjuries = ( round(random.uniform(0, 1), decs(othInjuriesProb[age+gender])) <= othInjuriesProb[age+gender] )
            othSickness = ( round(random.uniform(0, 1), decs(othSicknessProb[age+gender])) <= othSicknessProb[age+gender] )
            shv = ( round(random.uniform(0, 1), decs(selfHarmAndViolenceProb[age+gender])) <= selfHarmAndViolenceProb[age+gender] )

            falls = ( round(random.uniform(0, 1), decs(fallsProb[age+gender+str(cardiovascularDisease).lower()])) <= fallsProb[age+gender+str(cardiovascularDisease).lower()] )
            transportIncident = ( round(random.uniform(0, 1), decs(transportIncidentProb[age+gender+str(cardiovascularDisease).lower()])) <= transportIncidentProb[age+gender+str(cardiovascularDisease).lower()] )

            unintentional = ( round(random.uniform(0, 1), decs(unintentionalInjuriesProb[(str(falls)+str(poisonings)+str(natureForce)).lower()])) <= unintentionalInjuriesProb[(str(falls)+str(poisonings)+str(natureForce)).lower()] )
            sickness = ( round(random.uniform(0, 1), decs(sicknessProb[(str(respiratoryInfection)+str(cardiovascularDisease)+str(malignacy)).lower()])) <= sicknessProb[(str(respiratoryInfection)+str(cardiovascularDisease)+str(malignacy)).lower()] )

            death = ( round(random.uniform(0, 1), decs(deathProb[(str(othInjuries)+str(unintentional)+str(transportIncident)+str(shv)+str(sickness)+str(othSickness)).lower()])) <= deathProb[(str(othInjuries)+str(unintentional)+str(transportIncident)+str(shv)+str(sickness)+str(othSickness)).lower()] )

            data.append(int(falls))
            data.append(int(poisonings))
            data.append(int(natureForce))
            data.append(int(cardiovascularDisease))
            data.append(int(malignacy))
            data.append(int(respiratoryInfection))
            data.append(int(transportIncident))
            data.append(int(sickness))
            data.append(int(othInjuries))
            data.append(int(unintentional))
            data.append(int(othSickness))
            data.append(int(shv))
            data.append(int(death))

            writer.writerow(data)
