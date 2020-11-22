import requests
import json
import pprint

httpApiUrl = "https://api.rescuegroups.org/http/v2.json"
s = requests.Session()

appThreshold = 8

def login(username,password,accountNumber):
    data = {"username":username,"password":password,"accountNumber":accountNumber,"action":"login"}
    
    
    result = s.post(httpApiUrl,json=data)   
    #print(result.text)
    resultJson = json.loads(result.text)
    
    return(resultJson["data"]["token"],resultJson["data"]["tokenHash"]  )


def availableAnimals(token,tokenHash):
    requestJson = {
        "token":token,
        "tokenHash":tokenHash,
    "objectType":"animals",
    "objectAction":"search",
    "search":
    {
        "resultStart": "0",
        "resultLimit": "10",
        "resultSort": "animalName",
        "resultOrder": "asc",
        "filters":
        [
            {
                "fieldName": "animalStatus",
                "operation": "equals",
                "criteria": "Available"
            }
        ],
        "filterProcessing": "1",
        "fields":
        [
           
            "animalID","animalName", "animalSpecies","animalEyeColor","animalStatus"
        ]
         
    }
     
}
     #"animalID","animalOrgID","animalActivityLevel","animalAdoptedDate","animalAdoptionFee","animalAgeString","animalAltered","animalAvailableDate","animalBirthdate","animalBirthdateExact","animalBreed","animalCoatLength","animalColor","animalColorID","animalColorDetails","animalCourtesy","animalDeclawed","animalDescription","animalDescriptionPlain","animalDistinguishingMarks","animalEarType","animalEnergyLevel","animalExerciseNeeds","animalEyeColor","animalFence","animalFound","animalFoundDate","animalFoundPostalcode","animalGeneralAge","animalGeneralSizePotential","animalGroomingNeeds","animalHousetrained","animalIndoorOutdoor","animalKillDate","animalKillReason","animalLocation","animalLocationCoordinates","animalLocationDistance","animalLocationCitystate","animalMicrochipped","animalMixedBreed","animalName","animalSpecialneeds","animalSpecialneedsDescription","animalNeedsFoster","animalNewPeople","animalNotHousetrainedReason","animalObedienceTraining","animalOKWithAdults","animalOKWithCats","animalOKWithDogs","animalOKWithKids","animalOwnerExperience","animalPattern","animalPatternID","animalAdoptionPending","animalPrimaryBreed","animalPrimaryBreedID","animalRescueID","animalSearchString","animalSecondaryBreed","animalSecondaryBreedID","animalSex","animalShedding","animalSizeCurrent","animalSizePotential","animalSizeUOM","animalSpecies","animalSpeciesID","animalSponsorable","animalSponsors","animalSponsorshipDetails","animalSponsorshipMinimum","animalStatus","animalStatusID","animalSummary","animalTailType","animalThumbnailUrl","animalUptodate","animalUpdatedDate","animalUrl","animalVocal","animalYardRequired","animalAffectionate","animalApartment","animalCratetrained","animalDrools","animalEagerToPlease","animalEscapes","animalEventempered","animalFetches","animalGentle","animalGoodInCar","animalGoofy","animalHasAllergies","animalHearingImpaired","animalHypoallergenic","animalIndependent","animalIntelligent","animalLap","animalLeashtrained","animalNeedsCompanionAnimal","animalNoCold","animalNoFemaleDogs","animalNoHeat","animalNoLargeDogs","animalNoMaleDogs","animalNoSmallDogs","animalObedient","animalOKForSeniors","animalOKWithFarmAnimals","animalOlderKidsOnly","animalOngoingMedical","animalPlayful","animalPlaysToys","animalPredatory","animalProtective","animalSightImpaired","animalSkittish","animalSpecialDiet","animalSwims","animalTimid","fosterEmail","fosterFirstname","fosterLastname","fosterName","fosterPhoneCell","fosterPhoneHome","fosterSalutation","locationAddress","locationCity","locationCountry","locationUrl","locationName","locationPhone","locationState","locationPostalcode","animalPictures","animalVideos","animalVideoUrls"
    pp = pprint.PrettyPrinter(indent=4)
    result = s.post(httpApiUrl,json=requestJson)   
    #print(result.text)
    resultJson = json.loads(result.text)    
    
    return resultJson



def getNumberOfAdoptionApps(token,tokenHash,animalID):
    
    requestJson = {
   "token":token,
   "tokenHash":tokenHash,
   "objectType":"submittedforms",
   "objectAction":"search",
   "search":{
      "resultStart":"0",
      "resultOrder":"asc",
      "filters":[
         {
            "fieldName":"submittedformAnimalID",
            "operation":"equals",
            "criteria":animalID
         }
      ],
      "filterProcessing":"1",
      "fields":["submittedformAnimalID","submittedformID"]
      
      
   }
} 
    pp = pprint.PrettyPrinter(indent=4)
    result = s.post(httpApiUrl,json=requestJson)   
    resultJson = json.loads(result.text)    
    
   
    return int(resultJson["foundRows"])


def setAnimalStatusToNotAvailable(token,tokenHash,animalID):

    requestJson = {
    
        "token":token,
        "tokenHash":tokenHash,
        "objectType":"animals",
        "objectAction":"edit",
        "values":[
        {
            "animalID": animalID,
            "animalStatus": "Not Available"
        }]
    }
    #pp = pprint.PrettyPrinter(indent=4)
    result = s.post(httpApiUrl,json=requestJson)   
    resultJson = json.loads(result.text)    


def setThresholdOfApps(token,tokenHash,animalID,currentAppThreshold):


    requestJson = {
        "token":token,
        "tokenHash":tokenHash,
        "objectType":"animals",
        "objectAction":"edit",
        "values":[
        {
            "animalID": animalID,
            "animalEyeColor": "" + str(currentAppThreshold + appThreshold)
        }]
    }
    pp = pprint.PrettyPrinter(indent=4)
    print("threshold being set to %s" % str(currentAppThreshold + appThreshold))
    #result = s.post(httpApiUrl,json=requestJson)   
    #resultJson = json.loads(result.text)  


def main():
    
    
    token,tokenHash = login("MYUSERNAME","MYPASSWORD!",RESCUE_GROUPS_ACCOUNT_NUMBER)
    

    
    adoptionJson = availableAnimals(token,tokenHash)
  
    
    for animalID in adoptionJson["data"]:
        print("\n\n\n\n")
        print(animalID)
        print(adoptionJson["data"][animalID]["animalName"])
        print(adoptionJson["data"][animalID]["animalStatus"])

 
            
        numberOfApplications = getNumberOfAdoptionApps(token,tokenHash,animalID)
        
        print("\tnumberofapps %s" % numberOfApplications)
        



    
    
if __name__ == "__main__":
    main()