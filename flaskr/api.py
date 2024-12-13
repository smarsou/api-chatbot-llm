from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from .gpt import AssistantAPI

bp = Blueprint('api', __name__, url_prefix='/api')

ass = AssistantAPI()

@bp.route('/gen',methods=['POST'])
def gen():
    if request.method == 'POST':
        chat_request = request.json
        if chat_request:
            try:
                return ass.process_user_request(chat_request), 200
            except:
                return 'Internal Server Error', 500
        else:
            return 'The request of the user is empty', 400