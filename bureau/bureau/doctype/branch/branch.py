# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Branch(Document):
	def after_insert(self):
		#add branch to bureau
		self.add_branch_to_bureau()
		self.create_account()

	#add brnahc ot bureau
	def add_branch_to_bureau(self):
		#check if the branch is already added to the bureau
		bureau = frappe.get_doc("Bureau", self.bureau)
		bureau.append('branches', {
			'branch': self.branch_name,
			'branch_location': self.location
		})
		bureau.save()
	
	#create an account for the branch
	def create_account(self):
		#check if the account is already created
		if not frappe.db.exists("Account", f'Cash - {self.branch_name}'):
			frappe.get_doc({
				"doctype": "Account",
				"account_name": 'Cash',
				"branch": self.name,
				"currency": "GMD",
				"account_balance": 0
			}).insert()
		else:
			frappe.msgprint(("Account Already Created"))
