# -*- coding: utf-8 -*-

from .sql_traslator import SQL_Traslator
from odoo import models, fields, tools, api
import psycopg2
import psycopg2.extras
import json
from datetime import datetime

api_key=""
traslator = SQL_Traslator(api_key=api_key)

class sql_assistant_record(models.Model):
    _name = 'sql_assistant.record'
    _description = 'SQL Assistant Record'
    sql_assistant_id = fields.Many2one('sql_assistant.sql_assistant', ondelete='cascade')
    data = fields.Serialized()
    display_name = fields.Char(compute='_compute_display_name')
    def _generate_field_label(self, field_name):
        return field_name.replace('_', ' ').capitalize()

    @api.depends('data')
    def _compute_display_name(self):
        for record in self:
            if record.data.get('headers', False):
                record.display_name = '\n|\n'.join(f'{self._generate_field_label(k)}' for k, v in record.data.get('headers', {}).items()) if record.data else _('Undefined')
            else:
                record.display_name = '\n|\n'.join(f'{v}' for k, v in record.data.items()) if record.data else _('Undefined')
            
    class sql_assistant(models.Model):
        _name = 'sql_assistant.sql_assistant'
        _description = 'sql_assistant.sql_assistant'

        prompt = fields.Text(string='Consulta')
        record_ids = fields.One2many('sql_assistant.record', 'sql_assistant_id', string='Records')

        def datetime_to_string(self, data):
            for item in data:
                for key, value in item.items():
                    if isinstance(value, datetime):
                        item[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            return data

        def execute_query(self):
            sql_query = traslator.convert_to_sql(text_for_query=self.prompt)
            self.env.cr.execute(sql_query)
            records = self.env.cr.dictfetchall()
            self.record_ids.unlink()
            records = self.datetime_to_string(records)
            first = True
            for record in records:
                if first:
                    self.env['sql_assistant.record'].create({
                        'sql_assistant_id': self.id,
                        'data': {
                            'is_headers': True,
                            'headers': record
                        }
                    })
                    first = False
                self.env['sql_assistant.record'].create({
                    'sql_assistant_id': self.id,
                    'data': record
                })