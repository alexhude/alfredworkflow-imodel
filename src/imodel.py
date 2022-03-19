import sys
import json

query = sys.argv[1].lower()

result = {
	"items": []
}

with open('./list.txt') as f:
    devices = f.readlines()

uid = 0
for device in devices:
    if query in device.lower():
        parts = device.rstrip('\n').split(' : ')
        if parts[0].startswith("iPhone"):
            icon = "iphone.png"
        elif parts[0].startswith("iPad"):
            icon = "ipad.png"
        elif parts[0].startswith("iPod"):
            icon = "ipod.png"
        elif parts[0].startswith("Apple Watch"):
            icon = "watch.png"
        result["items"].append(
        {
            "uid": "imodel_" + str(uid),
            "type": "file",
            "title": parts[0],
            "subtitle": parts[1] + ' - ' + parts[2],
            "arg": [parts[0], parts[1], parts[2]],
            "autocomplete": "",
            "icon": {
                "path": icon
            }
        })    
        uid += 1

sys.stdout.write(json.dumps(result))

