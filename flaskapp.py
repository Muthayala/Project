# app.py (Flask)
from flaskapp import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Serve static images (like .png files) or HTML files (interactive charts)
@app.route('/graph-image')
def graph_image():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sine_wave.png')

@app.route('/interactive-graph')
def interactive_graph():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'interactive_graph.html')

if __name__ == '__main__':
    app.run(debug=True)
