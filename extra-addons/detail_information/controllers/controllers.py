# -*- coding: utf-8 -*-
# from odoo import http


# class DetailInformation(http.Controller):
#     @http.route('/detail_information/detail_information', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/detail_information/detail_information/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('detail_information.listing', {
#             'root': '/detail_information/detail_information',
#             'objects': http.request.env['detail_information.detail_information'].search([]),
#         })

#     @http.route('/detail_information/detail_information/objects/<model("detail_information.detail_information"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('detail_information.object', {
#             'object': obj
#         })
