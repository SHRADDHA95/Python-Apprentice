import json

kpop_json = """{"agency": "BigHit Entertainment", "bandName": "BTS", "country": "South Korea", "member": ["Kim Namjoon", "Kim SeokJin", "Min Yoongi", "Jung Hoseok", "Park Jimin", "Kim Tahyung", "Jeon Jungkook"]}"""
print(type(kpop_json))
python_objFromjson = json.loads(kpop_json)
print(python_objFromjson) ## converts from json to pythom dictionary object
print(type(python_objFromjson))



py_dic= {"country" : "India" , "capital" : "New Delhi"}

with open ("../data-file-resource/india.json", 'w') as jsonFileObject:
    jsonFileObject.write(json.dumps(py_dic)) ## json.dumps() converts from python dictionary to json string


