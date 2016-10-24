"""
Simple example of querying Elasticsearch creating REST requests
"""
import requests
import json

def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
		"query": {
			"term": {
				"time": term
				}
			}
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results

def format_results(results):
    """Print results nicely:
    doc_id) content
    """
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']['content']))

def create_doc(uri, doc_data={}):
    """Create new document."""
    query = json.dumps(doc_data)
    response = requests.post(uri, data=query)
    print(response)
    

if __name__ == '__main__':
    uri_search = 'http://ec2-52-54-140-219.compute-1.amazonaws.com:9200/cyber/dns/_search?pretty=true'
    uri_create = 'http://ec2-52-54-140-219.compute-1.amazonaws.com:9200/cyber/dns/'

    results = search(uri_search, 4171627)
    #format_results(results)
    print(results)

    #create_doc(uri_create, {"content": "The fox!"})
    #results = search(uri_search, "fox")
    #format_results(results)
    
