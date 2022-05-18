# -*- coding: utf-8 -*-
# from odoo import http


# class VelPurchaseOrderUserApproval(http.Controller):
#     @http.route('/vel_purchase_order_user_approval/vel_purchase_order_user_approval/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vel_purchase_order_user_approval/vel_purchase_order_user_approval/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vel_purchase_order_user_approval.listing', {
#             'root': '/vel_purchase_order_user_approval/vel_purchase_order_user_approval',
#             'objects': http.request.env['vel_purchase_order_user_approval.vel_purchase_order_user_approval'].search([]),
#         })

#     @http.route('/vel_purchase_order_user_approval/vel_purchase_order_user_approval/objects/<model("vel_purchase_order_user_approval.vel_purchase_order_user_approval"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vel_purchase_order_user_approval.object', {
#             'object': obj
#         })
