import requests
import time
import random
import json

SUCCESS_WEBHOOK = "https://discord.com/api/webhooks/825453289859579935/onOSWH1OJli0z4lBNLDGau9h8OSjaCgDtrA7H34ixF9Qp8J-bfvzpW1oxMku7wnYPQQ7"

while True:
	
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	print("%s Checking... " % current_time)

	try:
		r = requests.get("http://app.buff.game/api/marketplace/items?limit=99&page=1")
		result = r.json()

		products = result["data"]
		
		for product in products:
			if "1380 Riot Points Gift Card" in product["name"]:
				print(product["name"], end="\t")
				if product["isOutOfStock"] == False:
					print("In stock: %s" % product["name"])
					data = {}
					data["username"] = "Buff"
					data["content"] = "@here rp en stock sur buff"
					
					requests.post(SUCCESS_WEBHOOK, data=json.dumps(data), headers={"Content-Type": "application/json"})
				else:
					print("Not available")
	except Exception as e:
		
		print(e)

	
	print("")
	time.sleep(10)