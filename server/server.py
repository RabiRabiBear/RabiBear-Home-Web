'''
Author: Alchemist
Date: 2023-04-12
LastEditTime: 2023-07-06
FilePath: /RabiBear-Home-Web/server/server.py
Description: 

Copyright (c) 2023, All Rights Reserved. 
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os


app = Flask(__name__)
CORS(app)

data_path = "./resources/"
user_info_file = "user_info.json"
# saving_pot_file = "saving_pot.json"
# daily_todo_file = "daily_todo.json"
# today_todo_file = "today_todo.json"
file_type_path = {
    'saving_pot': "saving_pot.json",
    'daily_todo': "daily_todo.json",
    'today_todo': "today_todo.json",
    'exercise_calendar': "exercise_calendar.json",
}


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data['name']
    psw = data['password']

    with open(os.path.join(data_path, user_info_file),"r") as f:
        users = json.load(f)
    if name in users.keys():
        if users[name]['psw'] == psw:
            slogan = users[name]['slogan'] if 'slogan' in users[name].keys() else None
            # avatar = users[name]['avatar'] if 'avatar' in users[name].keys() else None
            # response = {'userName': name, 'slogan': slogan, 'avatar': avatar}
            response = {'userName': name, 'slogan': slogan}
            return jsonify(response)
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'Invalid user name'}), 401

@app.route('/modify_saving_pot', methods=['POST'])
def modify_saving_pot():
    data = request.get_json()

    with open(os.path.join(data_path, data['user_name'], file_type_path['saving_pot']),"r") as f:
        data_dict = json.load(f)
    if data['key'] == 'savedAmount':

        data_dict[data['key']] = data['val']
        data_dict['shownAmount'] = data['val'] % data_dict['targetAmount']
    else:
        raise ValueError("this is not allowed")

    with open(os.path.join(data_path, data['user_name'], file_type_path['saving_pot']),"w") as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)
    return jsonify(success=True)

@app.route('/get_data', methods=['GET'])
def get_data():
    user_name = request.args.get('user_name')
    opt_type = request.args.get('opt_type')
    # You can retrieve data from a database or any other source here
    with open(os.path.join(data_path, user_name, file_type_path[opt_type]),"r") as f:
        data_dict = json.load(f)
    return jsonify(data_dict)

@app.route('/init_new_day', methods=['POST'])
def init_new_day():
    data = request.get_json()

    # print('init_new_day', data)
    with open(os.path.join(data_path, data['user_name'], file_type_path['daily_todo']),"r") as f:
        data_dict = json.load(f)
    data_dict[data['date']] = data_dict['daily']
    with open(os.path.join(data_path, data['user_name'], file_type_path['daily_todo']),"w") as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)

    with open(os.path.join(data_path, data['user_name'], file_type_path['today_todo']),"r") as f:
        data_dict = json.load(f)
    data_dict[data['date']] = data['today_todo']
    with open(os.path.join(data_path, data['user_name'], file_type_path['today_todo']),"w") as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)
        
    return jsonify(success=True)

@app.route('/submit', methods=['POST'])
def submit_form():
    
    data = request.get_json()
    if 'Today' in data['title']:
        file_name = os.path.join(data_path, data['user_name'], file_type_path['today_todo'])
    else:
        file_name = os.path.join(data_path, data['user_name'], file_type_path['daily_todo'])

    
    with open(file_name,"r") as f:
        data_dict = json.load(f)
    
    # modify today's todo
    if data['opt'] == 'add':
        print(data['date'], data_dict.keys())
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
    

    with open(file_name,"w") as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)
        return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
