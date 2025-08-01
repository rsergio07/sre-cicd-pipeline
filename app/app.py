from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": int(time.time()),
        "version": os.getenv("APP_VERSION", "unknown")
    })

@app.route('/api/data')
def get_data():
    return jsonify({
        "message": "Hello from TechCorp API",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

if __name__ == "__main__":
    print("Flask app initialized.")
    print("To test the app, run the following commands in a separate terminal:")
    print("  curl http://localhost:8080/health")
    print("  curl http://localhost:8080/api/data")
    print("Then press Ctrl+C to exit.")
    app.run(host='0.0.0.0', port=8080)
