# -*- coding: utf-8 -*-
from odoo import http


class SqlAssistant(http.Controller):
    @http.route('/sql_assistant/sql_assistant', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/sql_assistant/sql_assistant/objects', auth='public')
    def list(self, **kw):
        return http.request.render('sql_assistant.listing', {
            'root': '/sql_assistant/sql_assistant',
            'objects': http.request.env['sql_assistant.sql_assistant'].search([]),
        })

    @http.route('/sql_assistant/sql_assistant/objects/<model("sql_assistant.sql_assistant"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('sql_assistant.object', {
            'object': obj
        })
