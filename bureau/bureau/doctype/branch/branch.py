# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Branch(Document):
	# def after_insert(self):
	# 	#add branch to bureau
	# 	self.add_branch_to_bureau()

	# #add brnahc ot bureau
	# def add_branch_to_bureau(self):
	# 	#check if the branch is already added to the bureau
	# 	bureau = frappe.get_doc("Bureau", self.bureau)
	# 	bureau.append('branches', {
	# 		'branch': self.branch_name,
	# 		'branch_location': self.location
	# 	})
	# 	bureau.save()
	
	#create an account for the branch
	
