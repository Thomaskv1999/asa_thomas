# Copyright (c) 2025, thomas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate,days_diff




@frappe.whitelist()
def get_customer(customer_name):
	addresses = frappe.get_all("Address", fields=["name", "email_id","phone"], order_by="creation desc")

	for addr in addresses:
		addr_doc = frappe.get_doc("Address", addr.name)

		for link in addr_doc.links:
			if link.link_doctype == "Customer" and link.link_name == customer_name:
				return {
					"email": addr_doc.email_id,
					"phone": addr_doc.phone
				}

	return {
		"email": None,
		"phone": None
	}
@frappe.whitelist()
def update_agreement_status(docname, status):
	doc = frappe.get_doc("Annual Service Agreement", docname)
	doc.db_set("status", status)

@frappe.whitelist()
def update_values(docname, status):
	doc = frappe.get_doc("Annual Service Agreement", docname)
	doc.db_set("status", status)

@frappe.whitelist()
def generate_agreement_id(agreement_title=None):


    name = agreement_title.replace(" ", "")
    date_str = frappe.utils.now_datetime().strftime("%m%y")

    series_key = f"{name}-ASA-{date_str}-"
    serial = frappe.model.naming.make_autoname(f"{series_key}.###")

    return serial


class AnnualServiceAgreement(Document):
	def validate(self):

		self.created_byon = frappe.session.user
	
	def before_save(self):
		for row in self.asa_coverage:
			if row.sla_value == 0:
				frappe.throw("SLA value must not be zero")


		if (self.total_sla_value or 0) < (self.total_invoiced or 0):
			frappe.throw("Total SLA Value should not be less than Total Billing Amount")	


		visit_dates = set()
		for row in self.asa_visit:
			if row.visit_date in visit_dates:
				frappe.throw(f"Duplicate visit date found: {row.visit_date}")
			visit_dates.add(row.visit_date)
	

		if self.total_visits < 1:
			frappe.throw("Minimum visit should be 1")

		if self.end_date < self.start_date:
			frappe.throw("Date Issue")

