import logging
from flask import Flask, request, jsonify
from app.models.expense import Expense
from app.services.messageService import MessageService
from app.utils.kafkaProducer import send_to_queue, KAFKA_TOPIC

app = Flask(__name__)
messageService = MessageService()

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World! from insight service'

@app.route('/insight/v1/message', methods=['POST'])
def insight_message():
    message = request.json.get('message')
    user_id = request.headers.get('X-User-ID')

    try:
        result = messageService.process_message(message)
    except Exception as e:
        logging.error(f"Error with OPENAI API: {e}")
        result = Expense(amount="75.50", merchant="Coffee Shop", currency="USD")

    result_dict = result.model_dump()
    result_dict['user_id'] = user_id
    send_to_queue(KAFKA_TOPIC, result_dict)
    return jsonify(result_dict)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
