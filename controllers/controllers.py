# -*- coding: utf-8 -*-
# from odoo import http


# class ErpFarha(http.Controller):
#     @http.route('/erp_farha/erp_farha', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/erp_farha/erp_farha/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('erp_farha.listing', {
#             'root': '/erp_farha/erp_farha',
#             'objects': http.request.env['erp_farha.erp_farha'].search([]),
#         })

#     @http.route('/erp_farha/erp_farha/objects/<model("erp_farha.erp_farha"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('erp_farha.object', {
#             'object': obj
#         })
