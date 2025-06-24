from flask import Flask,request,jsonify
import json,os

class TodoAPI:
    def __init__(self,db_file="backend/todo_db.json"):
        self.app = Flask(__name__)
        self.db_file = db_file
        self.todos = self.load_data()
        self.setup_routes()

    def load_data(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file,'w') as f:
                json.dump([],f)
        with open(self.db_file,'r') as f:
            return json.load(f)
    
    def save_data(self):
        with open(self.db_file,'w') as f:
            json.dump(self.todos,f,indent=2)

    def setup_routes(self):
        @self.app.route('/todos',methods=['GET'])
        def get_todos():
            return jsonify(self.todos)
        
        @self.app.route('/todos',methods=['POST'])
        def add_todos():
            data = request.get_json()
            self.todos.append({'task':data['task']})
            self.save_data()
            return jsonify({'message':'Task added'}),201
        
        @self.app.route('/todos/<int:index>',methods=['DELETE'])
        def detele_task(index):
            if 0 <= index < len(self.todos):
                self.todos.pop(index)
                self.save_data()
                return jsonify({'message': 'Task deleted'}), 200
            return jsonify({'error':'Invalid Index'}), 400
        
    def run(self):
        self.app.run(debug=True,port=5005)

if __name__ == "__main__":
    TodoAPI().run()