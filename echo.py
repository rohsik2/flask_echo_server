from flask import Flask, request, jsonify, make_response

flask_app = Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@flask_app.route('/', defaults={'path': ''}, methods=HTTP_METHODS)
@flask_app.route('/<path:path>', methods=HTTP_METHODS)
def api_create_order(path):
    default_body = {
        "method" : request.method,
        "body" : request.data.decode("UTF-8"),
        "path" : path
    }

    print(default_body)

    if request.method == "OPTIONS": # CORS preflight
        print("Get pre-flight option call")
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight  # Whatever.
        if(not request.is_json):
            return _cors_response(jsonify(default_body))
        default_body["request"] = request.get_json()
        return _cors_response(jsonify(default_body))
    else:
        return _cors_response(jsonify(default_body))

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _cors_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

flask_app.run()

