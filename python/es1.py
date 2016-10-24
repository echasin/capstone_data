from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(['http://ec2-52-54-140-219.compute-1.amazonaws.com:9200'])

#res = es.get(index="cyber", doc_type='tweet', id=1)
#print(res['_source'])

#es.indices.refresh(index="test-index")

res = es.search(index="cyber", doc_type='dns', body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    #print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
    print("%(host)s %(time)s" % hit["_source"])  
