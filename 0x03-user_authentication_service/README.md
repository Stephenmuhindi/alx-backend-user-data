Flask API Routes:

Import Flask (from flask import Flask).
Create a Flask app (app = Flask(__name__)).
Define functions (def get_users()...) for endpoints.
Decorate with @app.route('/users', methods=['GET', 'POST']) for URL and methods.
Cookies:

Access securely: username = request.cookies.get('username').
Set with purpose: response.set_cookie('session_id', 'abc123', http_only=True, secure=True).
Form Data:

Retrieve: name = request.form.get('name').
Handle missing data gracefully (e.g., use get() with defaults).
HTTP Status Codes:

Return with message: return jsonify({'message': 'Success!'}), 200.
Use common codes (200, 400, 401, 404, 500) for clarity.
