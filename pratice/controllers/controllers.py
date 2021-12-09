# -*- coding: utf-8 -*-
# from odoo import http


# class Pratice(http.Controller):
#     @http.route('/pratice/pratice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pratice/pratice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pratice.listing', {
#             'root': '/pratice/pratice',
#             'objects': http.request.env['pratice.pratice'].search([]),
#         })

#     @http.route('/pratice/pratice/objects/<model("pratice.pratice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pratice.object', {
#             'object': obj
#         })
