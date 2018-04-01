import requests
import json
from constants import *

class LuisBotSetter(object):
  
  def getTokens (self, queryFromUser):
    mappingValue = ""  
    

    params ={
      # Query parameter
      'q': 'please send an email to abc@gmail.com',
      # Optional request parameters, set to default values
      'timezoneOffset': '0',
      'verbose': 'false',
      'spellCheck': 'false',
      'staging': 'false',
    }

    headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': LUIS_API_SUBSCRIPTION,
    }
    
    params['q'] = queryFromUser
    try:

      r = requests.get('https://southeastasia.api.cognitive.microsoft.com/luis/v2.0/apps/'+ LUIS_APP_KEY, headers = headers, params = params)

      print ("[luissetter log] Response - {}".format(r.json()))
      entityIntent = r.json()
      
      intentFromQuery = entityIntent.get('topScoringIntent')['intent']
      intentEntityDict = {}
      intentEntityDict['intent'] = intentFromQuery
      entitiesFromQuery = entityIntent.get('entities')
      entityList = []
      
      for index, entities in enumerate(entitiesFromQuery): 
        entityList.append((entities['entity'], entities['type']))
        #returnString = returnString + str(index)  + ":" + entities['entity'] + "(" + mappingValue + "),"
      
      intentEntityDict['entity'] = entityList

      return json.dumps(intentEntityDict)
    
    except Exception as e:
      print ("[Errno {0}] {1}".format(e.errno, e.strerror))