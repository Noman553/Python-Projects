# -Json stand for - JavaScript object notation  this is the lightweight formate use to store data btween programs , websites , and apis
# think it as a box that is Use to send data from one application to another application

# now let's see that how python use the - Json there is a build in module in python that allow you to convert python object into the json and - json data back into the python object

import json
#let's try to convert the - some data form json to python object
# if you have a json string you can parse it by using json.load()
x = '{"name" : "noman" , "age" : 30 , "city" : "new York" }'
# now lets parse them
y = json.loads(x)
# the result will be in dictionary
print(y["age"])