# -*- coding: utf-8 -*-
"""
    flaskext.csrf
    ~~~~~~~~~~~~~

    A small Flask extension for adding CSRF protection.

    :copyright: (c) 2010 by Steve Losh.
    :license: MIT, see LICENSE for more details.
"""

from uuid import uuid4
from flask import abort, request, session, g
from werkzeug.routing import NotFound

_exempt_views = []


def csrf_exempt(view):
    _exempt_views.append(view)
    return view


def csrf(app, on_csrf=None):
    @app.before_request
    def _csrf_check_exemptions():
        try:
            dest = app.view_functions.get(request.endpoint)
            g._csrf_exempt = dest in _exempt_views
        except NotFound:
            g._csrf_exempt = False
    
    @app.before_request
    def _csrf_protect():
        # This simplifies unit testing, wherein CSRF seems to break
        if app.config.get('TESTING'):
            return
        if not g._csrf_exempt:
            if request.method == "POST" or request.method == 'PUT' or request.method == 'DELETE':
                if '_ct' not in session:
                    session['_ct'] = str(uuid4())
                csrf_token = session['_ct']
                if request.form.get("_ct") and csrf_token == request.form.get('_ct'):
                    return
                elif request.args.get("_ct") and csrf_token == request.args.get('_ct'):
                    return
                else:
                    if on_csrf:
                        on_csrf(*app.match_request())
                    abort(400)
    
    def generate_csrf_token():
        if '_ct' not in session:
            session['_ct'] = str(uuid4())
        return session['_ct']
    
    app.jinja_env.globals['csrf_token'] = generate_csrf_token