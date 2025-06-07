from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample listings data
listings = [
  {
    "id": "listing_1",
    "name": "Epic Designs",
    "rating": 4,
    "description": "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
    "projects": 57,
    "years": 8,
    "price": "$$",
    "phones": ["+91 - 984532853", "+91 - 984532854"]
  },
  {
    "id": "listing_2",
    "name": "Studio - D3",
    "rating": 4.5,
    "description": "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
    "projects": 43,
    "years": 6,
    "price": "$$$",
    "phones": ["+91 - 984532853", "+91 - 984532854"]
  }
] 

@app.route('/api/listings', methods=['GET'])
def get_listings():
    return jsonify(listings)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Backend service is running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 