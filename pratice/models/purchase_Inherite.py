from odoo import models, fields, api

class PurchaseModule(models.Model):
    _inherit="purchase.order"

    component_name = fields.Char(string= "Commponet_Name", required=True)

    Warehouse = fields.Char(string="Warehouse_Name",required=True)
    Warehouse1 =  fields.Char(string="Warehouse_Address")
    Delivery = fields.Char(String="Delivery_Person_Name")
    Delivery1 = fields.Char(String="Address")
    Delivery2 =fields.Integer(String="Contact no")