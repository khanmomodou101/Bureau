# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class Payout(Document):
    def validate(self):
        branch = frappe.get_doc("Branch", self.branch)
        if branch.account_balance < self.amount:
            frappe.throw("There is Not Enough Cash in This Branc ")
        
    def on_submit(self):
        #update account balance in cash account
        cash_account = frappe.get_doc('Account Type', 'GMD')
        updated_cash_account = cash_account.account_balance - self.amount
        cash_account.db_set('account_balance', updated_cash_account)


        #update cash acocunt to specific branch
        branch = frappe.get_doc("Branch", self.branch)
        updated_amount = branch.account_balance - self.amount
        branch.db_set('account_balance', updated_amount)
    # @frappe.whitelist()
    # def get_agent_username():
    #         user = frappe.session.user
    #         agent = frappe.get_doc("Agent", user.username)
    #         return agent