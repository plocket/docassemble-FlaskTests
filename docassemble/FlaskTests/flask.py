# pre-load
from flask import request, jsonify
from flask_cors import cross_origin
from docassemble.base.util import create_session, set_session_variables, interview_url
from docassemble.webapp.app_object import app, csrf
from docassemble.webapp.server import api_verify, jsonify_with_status
from docassemble.base.util import log

# How do I use whatever is in here? ~YAML?~ js file in the module
@app.route('/al_hello', methods=['GET'])
def hello():
  return "Hello world"

#@app.route('/create_prepopulate', methods=['POST'])
#@csrf.exempt
#@cross_origin(origins='*', methods=['POST', 'HEAD'], automatic_options=True)
#def create_prepopulate():
#    if not api_verify():
#        return jsonify_with_status({"success": "False", "error_message": "Access denied."}, 403)
#    post_data = request.get_json(silent=True)
#    if post_data is None:
#        post_data = request.form.copy()
#    if 'i' not in request.args:
#        return jsonify_with_status({"success": False, "error_message": "No 'i' specified in URL parameters."}, 400)
#    session_id = create_session(request.args['i'])
#    if len(post_data):
#        set_session_variables(request.args['i'], session_id, post_data, overwrite=True, process_objects=False)
#    url = interview_url(i=request.args['i'], session=session_id, style='short_package', temporary=90*24*60*60)
#    return jsonify({"success": True, "url": url})