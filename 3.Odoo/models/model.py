# -*- coding: utf-8 -*-
from odoo import api, fields, models

class TestModel(models.Model):
    _name = 'myshop.patient'

    name=fields.Char(required=True)
    start_date=fields.Datetime(string='Start Date')
    end_date=fields.Datetime(string='End Date')
    duration=fields.Integer(_compute='_apply_duration')
    tester=fields.Many2one('res.partner',string='Tester')

    @api.depends('end_date','start_date')
    def _apply_duration(self):
        for dur in self:
            durat=dur.end_date - dur.start_date
            dur.duration=durat


