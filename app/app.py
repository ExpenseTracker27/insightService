from flask import Flask, request, jsonify
from app.services.messageService import MessageService


app = Flask(__name__)
messageService = MessageService()

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World! from insight service'

@app.route('/insight/v1/message', methods=['POST'])
def insight_message():
    message = request.json.get('message')
    result = messageService.process_message(message)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
