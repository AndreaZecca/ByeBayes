import random

order = 1
alpha = 1

X = 0

genderProb = {}
genderProb [ "female"] = 0.4959
genderProb ["male"] = 0.5041

ageProb = {}
ageProb ["young"] = 0.3188
ageProb ["adult"] = 0.5995
ageProb ["old"] = 0.0817

fallsProb = {}
fallsProb ["youngFemalefalse"] = 0.14037
fallsProb ["adultFemalefalse"] = 0.06380
fallsProb ["oldFemalefalse"] = 0.12761
fallsProb ["youngMalefalse"] = 0.18288
fallsProb ["adultMalefalse"] = 0.08313
fallsProb ["oldMalefalse"] = 0.16626
fallsProb ["youngFemaletrue"] = 0.14037
fallsProb ["adultFemaletrue"] = 0.08520
fallsProb ["oldFemaletrue"] = 0.15
fallsProb ["youngMaletrue"] = 0.08313
fallsProb ["adultMaletrue"] = 0.10411
fallsProb ["oldMaletrue"] = 0.18336

poisoningProb = {}
poisoningProb ["youngFemale"] = 0.008901
poisoningProb ["adultFemale"] = 0.0079
poisoningProb ["oldFemale"] = 0.002967
poisoningProb ["youngMale"] = 0.01
poisoningProb ["adultMale"] = 0.00928
poisoningProb ["oldMale"] = 0.003483

natureForceProb = 0.141

othInjuriesProb = {}
othInjuriesProb ["youngFemale"] = 0.00111
othInjuriesProb ["adultFemale"] = 0.0000668
othInjuriesProb ["oldFemale"] = 0.000280
othInjuriesProb ["youngMale"] = 0.000151
othInjuriesProb ["adultMale"] = 0.000160
othInjuriesProb ["oldMale"] = 0.000328

transportIncidentProb = {}
transportIncidentProb ["youngFemalefalse"] = 0.01
transportIncidentProb ["adultFemalefalse"] = 0.057
transportIncidentProb ["oldFemalefalse"] = 0.027
transportIncidentProb ["youngMalefalse"] = 0.018
transportIncidentProb ["adultMalefalse"] = 0.09
transportIncidentProb ["oldMalefalse"] = 0.038
transportIncidentProb ["youngFemaletrue"] = 0.0152
transportIncidentProb ["adultFemaletrue"] = 0.08664
transportIncidentProb ["oldFemaletrue"] = 0.04104
transportIncidentProb ["youngMaletrue"] = 0.02736
transportIncidentProb ["adultMaletrue"] = 0.1368
transportIncidentProb ["oldMaletrue"] = 0.05776

selfHarmAndViolenceProb = {}
selfHarmAndViolenceProb ["youngFemale"] = 0.00021
selfHarmAndViolenceProb ["adultFemale"] = 0.01195
selfHarmAndViolenceProb ["oldFemale"] = 0.008
selfHarmAndViolenceProb ["youngMale"] = 0.00042
selfHarmAndViolenceProb ["adultMale"] = 0.0239
selfHarmAndViolenceProb ["oldMale"] = 0.016

respiratoryInfectionProb = {}
respiratoryInfectionProb ["youngFemale"] = 0.41500
respiratoryInfectionProb ["adultFemale"] = 0.180000
respiratoryInfectionProb ["oldFemale"] = 0.247800
respiratoryInfectionProb ["youngMale"] = 0.332000
respiratoryInfectionProb ["adultMale"] = 0.144000
respiratoryInfectionProb ["oldMale"] = 0.198240

cardiovascularDiseaseProb = {}
cardiovascularDiseaseProb ["youngFemale"] = 0.0036
cardiovascularDiseaseProb ["adultFemale"] = 0.0084
cardiovascularDiseaseProb ["oldFemale"] = 0.036
cardiovascularDiseaseProb ["youngMale"] = 0.084
cardiovascularDiseaseProb ["adultMale"] = 0.0476
cardiovascularDiseaseProb ["oldMale"] = 0.0204

malignacyProb = {}
malignacyProb ["youngFemale"] = 0.002000
malignacyProb ["adultFemale"] = 0.065700
malignacyProb ["oldFemale"] = 0.168300
malignacyProb ["youngMale"] = 0.002400
malignacyProb ["adultMale"] = 0.078840
malignacyProb ["oldMale"] = 0.201960

othSicknessProb = {}
othSicknessProb ["youngFemale"] = 0.00226
othSicknessProb ["adultFemale"] = 0.00111
othSicknessProb ["oldFemale"] = 0.0145
othSicknessProb ["youngMale"] = 0.00280
othSicknessProb ["adultMale"] = 0.00287
othSicknessProb ["oldMale"] = 0.0171

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

            print(random.uniform(0.00000001, 1))
            

            
            
            
            
            f.write(line)
            f.write('\n')

        f.close()
