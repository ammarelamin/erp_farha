# -*- coding: utf-8 -*-

from odoo import models, fields, api



class stockPicking(models.Model):
    _inherit = 'stock.picking'

    employee_id = fields.Many2one(comodel_name='hr.employee', string='Engineer')
    