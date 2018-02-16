import requests
import json
class LuisBotSetter(object):
  
  headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'confidential key',
  }
  
  def getTokens (self, queryFromUser):
    mappingValue = ""  
    stri = ""
    intentFromQuery = ""
    intentEntityDict = {}
    entityList = []
    params ={
      # Query parameter
      'q': 'please send an email to abc@gmail.com',
      # Optional request parameters, set to default values
      'timezoneOffset': '0',
      'verbose': 'false',
      'spellCheck': 'false',
      'staging': 'false',
    }
    params['q'] = queryFromUser
    try:
      r = requests.get ('https://southeastasia.api.cognitive.microsoft.com/luis/v2.0/apps/24c19c39-9242-4cea-ab89-4213e1f146cc', headers = self.headers, params = params)
	    #https://westus.api.cognitive.microsoft.com/api/v2.0/apps/24c19c39-9242-4cea-ab89-4213e1f146cc?subscription-key=ee8f4937e8c94ef9b79ce873d9cce89d&verbose=true&timezoneOffset=330&q=	
      entityIntent = r.json()
      '''entityIntent = {"query":"turn on bed room light",
      "topScoringIntent":{"intent":"homeautomation.turnon","score":0.987},
      "entities":[{"entity":"bedroom","type":"homeautomation",}]}
      '''
      intentFromQuery = entityIntent.get('topScoringIntent')['intent']
      intentEntityDict['intent'] = intentFromQuery
      entitiesFromQuery = entityIntent.get('entities')
      for index, entities in enumerate(entitiesFromQuery): 
        if 'resolution' in entities.keys():
          mappingValue = entities.get('resolution')['values'][0].get('value')
        entityList.append(entities['entity']  + "(" + mappingValue + "),")
        #returnString = returnString + str(index)  + ":" + entities['entity'] + "(" + mappingValue + "),"
        intentEntityDict['entity'] = entityList 
      return json.dumps(intentEntityDict)
    except Exception as e:
      print ("[Errno {0}] {1}".format(e.errno, e.strerror))