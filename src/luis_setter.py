import requests
class LuisBotSetter(object):
  
  headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'confidential key',
  }
  
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
    params['q'] = queryFromUser
    try:
      r = requests.get ('https://southeastasia.api.cognitive.microsoft.com/luis/v2.0/apps/24c19c39-9242-4cea-ab89-4213e1f146cc', headers = self.headers, params = params)
      #print (r.json())
	    #https://westus.api.cognitive.microsoft.com/api/v2.0/apps/24c19c39-9242-4cea-ab89-4213e1f146cc?subscription-key=ee8f4937e8c94ef9b79ce873d9cce89d&verbose=true&timezoneOffset=330&q=	
      entityIntent = r.json() 
      intentFromQuery = entityIntent.get('topScoringIntent')['intent']
      entitiesFromQuery = entityIntent.get('entities')
      returnString = "intent:" + intentFromQuery +",entity:("
      for index, entities in enumerate(entitiesFromQuery): 
        if 'resolution' in entities.keys():
          mappingValue = entities.get('resolution')['values'][0].get('value')
        
        returnString = returnString + str(index)  + ":" + entities['entity'] + "(" + mappingValue + "),"
      returnString = returnString + ")"      
      print(returnString)
    except Exception as e:
      print ("[Errno {0}] {1}".format(e.errno, e.strerror))