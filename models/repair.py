# -*- coding: utf-8 -*-

from odoo import models, fields, _


class repirOrder(models.Model):
    _inherit = 'repair.order'
    ac = fields.Float(string='AC')
    earth = fields.Float(string='Earth')
    repair_type = fields.Selection(string='Repair Type', selection=[('pm', 'PM'), ('call', 'Call'), ('install', 'Installation'), ('assistance', 'Assistance')])
    repair_status = fields.Selection(string='Status', selection=[('warranty', 'Warranty'), ('contract', 'Contract'), ('per_call', 'Per Call'), ('inspection', 'Inspection')])
    employee_ids = fields.Many2many(comodel_name='hr.employee', string='Engineers')
    site_condition = fields.Char(string='Site Condition')
    air_condition = fields.Char(string='Air Condition')
    electricity = fields.Char(string='Electricity')
    cash = fields.Char(string='Cash')
    