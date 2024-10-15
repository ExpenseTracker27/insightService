from flask import Flask, request, jsonify

from app.models.expense import Expense
from app.services.messageService import MessageService
from app.utils.kafkaProducer import send_to_queue, KAFKA_TOPIC
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
messageService = MessageService()

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World! from insight service'

@app.route('/insight/v1/message', methods=['POST'])
def insight_message():
    message = request.json.get('message')

    try:
        result = messageService.process_message(message)
    except Exception as e:
        print("Error with OPENAI API:", e)
        result = Expense(amount="75.50", merchant="Coffee Shop", currency="USD")

    serialized_result = result.model_dump_json()
    send_to_queue(KAFKA_TOPIC, serialized_result)

    result_dict = result.model_dump()
    return jsonify(result_dict)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
