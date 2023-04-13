'''
Author: Alchemist
Date: 2023-04-12
LastEditTime: 2023-04-13
FilePath: /RabiBear-Home-Web/server/server.py
Description: 

Copyright (c) 2023, All Rights Reserved. 
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/init_new_day', methods=['POST'])
def init_new_day():
    data = request.get_json()
    # print(data)
    with open("./resources/daily_todo.json","r") as f:
        data_dict = json.load(f)
    data_dict[data['date']] = data_dict['daily']
    with open("./resources/daily_todo.json","w") as f:
        json.dump(data_dict, f, indent=4)

    with open("./resources/today_todo.json","r") as f:
        data_dict = json.load(f)
    data_dict[data['date']] = data['today_todo']
    with open("./resources/today_todo.json","w") as f:
        json.dump(data_dict, f, indent=4)
        
    return jsonify(success=True)

@app.route('/submit', methods=['POST'])
def submit_form():
    # print(request)
    # print(request.get_json())
    
    
    data = request.get_json()
    if 'Today' in data['title']:
        file_name = "resources/today_todo.json"
    else:
        file_name = "./resources/daily_todo.json"

    
    with open(file_name,"r") as f:
        data_dict = json.load(f)
    
    # modify today's todo
    if data['opt'] == 'add':
        assert data['date'] in data_dict.keys()
        data_dict[data['date']].append(data['todo'])
        
    elif data['date'] in data_dict.keys():
        for i, todo in enumerate(data_dict[data['date']]):
            if todo['id'] == data['todo']['id']:
                if data['opt'] == 'toggle':
                    data_dict[data['date']][i] = data['todo']
                elif data['opt'] == 'remove':
                    data_dict[data['date']].pop(i)
                else:
                    ValueError("No such opt in the data_dict")
                break
    else:
        ValueError("No such date in the data_dict")
    

    # import pdb; pdb.set_trace()
    with open(file_name,"w") as f:
        json.dump(data_dict, f, indent=4)
        # f.write(str(data))
        # f.write("\n")
        return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
