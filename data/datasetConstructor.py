import random
import decimal

order = 1
alpha = 1


def decs(number):
    d = decimal.Decimal(str(number))
    return abs(d.as_tuple().exponent)
    #n = len(str(number).split(".")[1])
    #return n

X = 0

genderProb = {}
genderProb [ "female"] = 0.4959
genderProb ["male"] = 0.5041

ageProb = {}
ageProb ["young"] = 0.3188
ageProb ["adult"] = 0.5995
ageProb ["old"] = 0.0817

fallsProb = {}
fallsProb ["youngfemalefalse"] = 0.14037
fallsProb ["adultfemalefalse"] = 0.06380
fallsProb ["oldfemalefalse"] = 0.12761
fallsProb ["youngmalefalse"] = 0.18288
fallsProb ["adultmalefalse"] = 0.08313
fallsProb ["oldmalefalse"] = 0.16626
fallsProb ["youngfemaletrue"] = 0.14037
fallsProb ["adultfemaletrue"] = 0.08520
fallsProb ["oldfemaletrue"] = 0.15
fallsProb ["youngmaletrue"] = 0.08313
fallsProb ["adultmaletrue"] = 0.10411
fallsProb ["oldmaletrue"] = 0.18336

poisoningProb = {}
poisoningProb ["youngfemale"] = 0.008901
poisoningProb ["adultfemale"] = 0.0079
poisoningProb ["oldfemale"] = 0.002967
poisoningProb ["youngmale"] = 0.01
poisoningProb ["adultmale"] = 0.00928
poisoningProb ["oldmale"] = 0.003483

natureForceProb = 0.141

othInjuriesProb = {}
othInjuriesProb ["youngfemale"] = 0.00111
othInjuriesProb ["adultfemale"] = 0.0000668
othInjuriesProb ["oldfemale"] = 0.000280
othInjuriesProb ["youngmale"] = 0.000151
othInjuriesProb ["adultmale"] = 0.000160
othInjuriesProb ["oldmale"] = 0.000328

transportIncidentProb = {}
transportIncidentProb ["youngfemalefalse"] = 0.01
transportIncidentProb ["adultfemalefalse"] = 0.057
transportIncidentProb ["oldfemalefalse"] = 0.027
transportIncidentProb ["youngmalefalse"] = 0.018
transportIncidentProb ["adultmalefalse"] = 0.09
transportIncidentProb ["oldmalefalse"] = 0.038
transportIncidentProb ["youngfemaletrue"] = 0.0152
transportIncidentProb ["adultfemaletrue"] = 0.08664
transportIncidentProb ["oldfemaletrue"] = 0.04104
transportIncidentProb ["youngmaletrue"] = 0.02736
transportIncidentProb ["adultmaletrue"] = 0.1368
transportIncidentProb ["oldmaletrue"] = 0.05776

selfHarmAndViolenceProb = {}
selfHarmAndViolenceProb ["youngfemale"] = 0.00021
selfHarmAndViolenceProb ["adultfemale"] = 0.01195
selfHarmAndViolenceProb ["oldfemale"] = 0.008
selfHarmAndViolenceProb ["youngmale"] = 0.00042
selfHarmAndViolenceProb ["adultmale"] = 0.0239
selfHarmAndViolenceProb ["oldmale"] = 0.016

respiratoryInfectionProb = {}
respiratoryInfectionProb ["youngfemale"] = 0.41500
respiratoryInfectionProb ["adultfemale"] = 0.180000
respiratoryInfectionProb ["oldfemale"] = 0.247800
respiratoryInfectionProb ["youngmale"] = 0.332000
respiratoryInfectionProb ["adultmale"] = 0.144000
respiratoryInfectionProb ["oldmale"] = 0.198240

cardiovascularDiseaseProb = {}
cardiovascularDiseaseProb ["youngfemale"] = 0.0036
cardiovascularDiseaseProb ["adultfemale"] = 0.0084
cardiovascularDiseaseProb ["oldfemale"] = 0.036
cardiovascularDiseaseProb ["youngmale"] = 0.084
cardiovascularDiseaseProb ["adultmale"] = 0.0476
cardiovascularDiseaseProb ["oldmale"] = 0.0204

malignacyProb = {}
malignacyProb ["youngfemale"] = 0.002000
malignacyProb ["adultfemale"] = 0.065700
malignacyProb ["oldfemale"] = 0.168300
malignacyProb ["youngmale"] = 0.002400
malignacyProb ["adultmale"] = 0.078840
malignacyProb ["oldmale"] = 0.201960

othSicknessProb = {}
othSicknessProb ["youngfemale"] = 0.00226
othSicknessProb ["adultfemale"] = 0.00111
othSicknessProb ["oldfemale"] = 0.0145
othSicknessProb ["youngmale"] = 0.00280
othSicknessProb ["adultmale"] = 0.00287
othSicknessProb ["oldmale"] = 0.0171

# al posto delle x vanno le somme di quelli negli appunti calcolati il primo giorno (no distinzione age-gender)

unintentionalInjuriesProb = {}
unintentionalInjuriesProb ["truetruetrue" ] = 0.001460018
unintentionalInjuriesProb ["truetruefalse" ] = 0.00145122
unintentionalInjuriesProb ["truefalsetrue" ] = 0.001362798
unintentionalInjuriesProb ["truefalsefalse" ] = 0.001354
unintentionalInjuriesProb ["falsetruetrue" ] = 0.000106018
unintentionalInjuriesProb ["falsetruefalse" ] = 0.00009722
unintentionalInjuriesProb ["falsefalsetrue" ] = 0.000008798
unintentionalInjuriesProb ["falsefalsefalse" ] = 0.00000001

sicknessProb = {}
sicknessProb ["truetruetrue" ] = 0.05344
sicknessProb ["truetruefalse" ] = 0.044026
sicknessProb ["truefalsetrue" ] = 0.022126
sicknessProb ["truefalsefalse" ] = 0.006356
sicknessProb ["falsetruetrue" ] = 0.05344
sicknessProb ["falsetruefalse" ] = 0.03767
sicknessProb ["falsefalsetrue" ] = 0.01577
sicknessProb ["falsefalsefalse" ] = 0.0001

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

if __name__ == "__main__":
    
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

    with open('dataset.txt', 'w') as f:
        headerLine = "ID        Age-range   Gender   #####    Falls     Poisonings     Naure-force     Cardiovascular-disease    Malignancy  Respiratory-infection     #####     Transport-incident      Sickness     Other-injuries     Unintentional-injuries      Other-sickness      SHV     #####      Death"
        f.write(headerLine)
        f.write('\n\n')
        for i in range(1,(10**order)+1):
            line = ""
            line = line + str(i) + "\t\t   "

            if ( i in ageTresholds ):
                ageGroupIndex = ageGroupIndex + 1
            if ( i in genderTresholds ):
                genderIndex = 1 - genderIndex

            gender = genderGroups[genderIndex]
            age = ageGroups[ageGroupIndex]

            line = line + str(age) + "\t  "

            if(ageGroupIndex == 2):
                line = line + "\t  "

            line = line + str(gender) + "\t"

            
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

            line = str(line) + str(falls) + str(poisonings) + str(natureForce) + str(cardiovascularDisease) + str(malignacy) + str(respiratoryInfection) + str(transportIncident) + str(sickness) + str(othInjuries) + str(unintentional) + str(othSickness) + str(shv) + str(death)

            f.write(line)
            f.write('\n')

        f.close()
