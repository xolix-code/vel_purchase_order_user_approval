# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUser(models.Model):
    _inherit = 'res.users'

    user_approval_amount = fields.Monetary(string="Monto mínimo")

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _approval_allowed(self):
        """Returns whether the order qualifies to be approved by the current user"""
        self.ensure_one()
        user_approval_amount = self.env.user.user_approval_amount
        return (
            self.company_id.po_double_validation == 'one_step'
            or (self.company_id.po_double_validation == 'two_step'
                and self.amount_total < self.env.company.currency_id._convert(
                    user_approval_amount, self.currency_id, self.company_id,
                    self.date_order or fields.Date.today()))
            or self.user_has_groups('purchase.group_purchase_manager'))

# class vel_purchase_order_user_approval(models.Model):
#     _name = 'vel_purchase_order_user_approval.vel_purchase_order_user_approval'
#     _description = 'vel_purchase_order_user_approval.vel_purchase_order_user_approval'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
