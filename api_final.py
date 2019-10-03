import requests
import json

def foo(id, depth):
    endpoint = "http://www.employee.com/api/employee/" + id
    r = requests.get(endpoint)
    json_data = json.loads(r.json())
    space = ""
    for i in depth:
        space += " "
    print space + json_data['name'] + " - " + json_data['title']

    for employee in json_data['reports']:
        foo(employee, depth + 1)

id = "A123456789"
foo(A123456789, 0)