import requests,json,time
print "***********************started**************************",str(time.asctime())
#{msp_code=msp_2802, number=T20180725.0001, id=20634}
resHed = {'content-type': "application/json"}
#url = "https://stg.netenrichgo.com/incident/autotask/callback?msp_code=msp_2802&id=20674&number=T20180801.0006"
#url = "http://f1.netenrich.us/incident/connectwise/callback?msp_code=msp_570823&id=5362&number=5362"
for i in xrange(10):
	url = "https://stg.netenrichgo.com/incident/connectwise/callback?msp_code=msp_570823&id=6001&number=6001"
	#url = "http://localhost:8505/incident/connectwise/callback?msp_code=msp_570823&id=5362"+str(i)+"&number=5362"+str(i)
	result=requests.get(url, headers={}, verify = False)
	print result,"RESULT--->--->",result.content
