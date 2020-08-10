# -*- coding: utf-8 -*-
from odoo import http

# class CarModel(http.Controller):
#     @http.route('/car_model/car_model/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_model/car_model/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_model.listing', {
#             'root': '/car_model/car_model',
#             'objects': http.request.env['car_model.car_model'].search([]),
#         })

#     @http.route('/car_model/car_model/objects/<model("car_model.car_model"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_model.object', {
#             'object': obj
#         })