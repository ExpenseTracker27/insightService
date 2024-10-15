from flask import Flask, request, json
from langchain.chains.question_answering.map_reduce_prompt import messages

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! from insight service'

@app.route('/insight/v1/message', methods=['POST'])
def insight_message():
    message = request.json.get('message')
    result = messageService.process_message(message)


if __name__ == '__main__':
    app.run()
