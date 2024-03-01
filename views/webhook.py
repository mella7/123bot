from flask import Blueprint, request

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON payload from the request
    data = request.json
    
    # Process the data from TradingView webhook
    # Example: Extract relevant information from the payload
    symbol = data['symbol']
    strategy = data['strategy']
    condition = data['condition']
    value = data['value']
    
    # Example: Perform some action based on the received data
    print(f"Received webhook for symbol '{symbol}' with strategy '{strategy}':")
    print(f"Condition: {condition}, Value: {value}")
    
    # Optionally, you can perform additional processing here, such as placing orders
    
    # Respond with a success message
    return {'message': 'Webhook received successfully'}, 200