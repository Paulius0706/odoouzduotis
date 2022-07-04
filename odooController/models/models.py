# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Documet(models.Model):
    _name = "my.document"
    _description = "Company document"
    
    name = fields.Char(string='Name', max_length=255, required=False)
    description = fields.Char(string='Description', required=False)
    company_id = fields.Many2one(comodel_name="res.company", string='Company', max_length=255, required=False)
    
    
class Company(models.Model):
    _inherit='res.company'
    documents_id = fields.One2many(comodel_name='my.document',inverse_name='company_id',string='Documents')

    # @api.model
    # def create(self,vals):
    #     record = self.env['your.model'].create({
    #         'name': vals['name'],
    #         'description': vals['description']
    #     })
    #     return record

# class odoo_controller(models.Model):
#     _name = 'odoo_controller.odoo_controller'
#     _description = 'odoo_controller.odoo_controller'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
