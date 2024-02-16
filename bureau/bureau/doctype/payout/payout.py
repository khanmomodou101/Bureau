# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class Payout(Document):
    def validate(self):
        #check if there is enough cash in the cash account:
        branch = frappe.get_doc("Branch", self.branch)
        if branch.account_balance < self.amount:
            frappe.throw("There is Not Enough Cash in This Branch ")
        
    def on_submit(self):
        #update account balance in cash account
        cash_account = frappe.get_doc('Account Type', 'GMD')
        updated_cash_account = cash_account.account_balance - self.amount
        cash_account.db_set('account_balance', updated_cash_account)

        self.create_transaction()
        #append branches to to
        #update cash acocunt to specific branch
        branch = frappe.get_doc("Branch", self.branch)
        updated_amount = branch.account_balance - self.amount
        branch.db_set('account_balance', updated_amount)
    
    #create a transaction after submit
    def create_transaction(self):
        branch = frappe.get_doc("Branch", self.branch)

        frappe.get_doc({
            "doctype": "Transactions",
            "transaction_type": "Payout",
            "amount": self.amount,
            "branch": branch,
            "bureau": branch.bureau,
            "mto": self.mto,
            "date": self.date
        }).insert()
        frappe.msgprint(("Transaction Created"))
        