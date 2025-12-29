from flask import Flask, request, jsonify
from flask_cors import CORS
from prometheus_client import Counter, Histogram, generate_latest
from pythonjsonlogger import jsonlogger
import logging
import time
import uuid

# Configuration du logging structuré
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
logHandler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# Initialisation Flask
app = Flask(__name__)
CORS(app)

# Métriques Prometheus
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status'])
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP Request Duration', ['method', 'endpoint'])

# Base de données en mémoire (simple pour la démo)
items_db = {}
item_counter = 0


# Middleware pour logging et métriques
@app.before_request
def before_request():
    request.start_time = time.time()
    request.request_id = str(uuid.uuid4())
    logger.info('Request started', extra={
        'request_id': request.request_id,
        'method': request.method,
        'path': request.path,
        'remote_addr': request.remote_addr
    })


@app.after_request
def after_request(response):
    duration = time.time() - request.start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path, status=response.status_code).inc()
    REQUEST_DURATION.labels(method=request.method, endpoint=request.path).observe(duration)
    response.headers['X-Request-ID'] = request.request_id
    logger.info('Request completed', extra={
        'request_id': request.request_id,
        'method': request.method,
        'path': request.path,
        'status_code': response.status_code,
        'duration_ms': round(duration * 1000, 2)
    })
    return response


# Routes


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'devops-api'}), 200


@app.route('/metrics', methods=['GET'])
def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest(), 200


@app.route('/api/items', methods=['GET'])
def get_items():
    """Get all items"""
    return jsonify({'items': list(items_db.values()), 'count': len(items_db)}), 200


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Get a specific item"""
    item = items_db.get(item_id)
    if item:
        return jsonify(item), 200
    logger.warning('Item not found', extra={'request_id': request.request_id, 'item_id': item_id})
    return jsonify({'error': 'Item not found'}), 404


@app.route('/api/items', methods=['POST'])
def create_item():
    """Create a new item"""
    global item_counter
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    item_counter += 1
    new_item = {
        'id': item_counter,
        'name': data['name'],
        'description': data.get('description', ''),
        'created_at': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    items_db[item_counter] = new_item
    logger.info('Item created', extra={'request_id': request.request_id, 'item_id': item_counter})
    return jsonify(new_item), 201


@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item"""
    item = items_db.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    logger.info('Item updated', extra={'request_id': request.request_id, 'item_id': item_id})
    return jsonify(item), 200


@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item"""
    if item_id in items_db:
        del items_db[item_id]
        logger.info('Item deleted', extra={'request_id': request.request_id, 'item_id': item_id})
        return jsonify({'message': 'Item deleted successfully'}), 200
    return jsonify({'error': 'Item not found'}), 404


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    logger.error('Internal server error', extra={'request_id': request.request_id, 'error': str(error)})
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    logger.info('Starting DevOps API server')
    app.run(host='0.0.0.0', port=8080, debug=False)
