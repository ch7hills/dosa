import requests,json,time
print "***********************started**************************",str(time.asctime())
#{msp_code=msp_2802, number=T20180725.0001, id=20634}
resHed = {'content-type': "application/vnd.github.v3+json",'Authorization':"token d8ec1c3273d73fde38d755fdcf24e781dd1066b9"}
body={"message": "my test commit message from postman","committer": {"name": "ch7hills","email": "ch.7hills@gmail.com"},"content": "bXkgdXBkYXRlZCBmaWxlIGNvbnRlbnRz","sha": "329688480d39049927147c162b9d2deaf885005f"}
for i in xrange(1):
	#url = "https://stg.netenrichgo.com/incident/connectwise/callback?msp_code=msp_570823&id=6001&number=6001"
	url ="https://api.github.com/repos/ch7hills/dosa/contents/SamplePostAPI.py"
	#url = "http://localhost:8505/incident/connectwise/callback?msp_code=msp_570823&id=5362"+str(i)+"&number=5362"+str(i)
	result=requests.get(url, headers=resHed, data={}, verify = True)
	print result,"RESULT--->--->",result.content
