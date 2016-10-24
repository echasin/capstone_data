def search(uri, term):
   """Simple Elasticsearch Query"""
   query = json.dumps({
 	"query": {
   		"range": {
     		"time": {
       			"lte": 4171627,
       			"gte": 4171627
     				}
   				}
 			}
   })
   response = requests.get(uri, data=query)
   results = json.loads(response.text)
   return results


