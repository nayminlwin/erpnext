import frappe
import erpnext

def execute():
	if frappe.db.has_column("Journal Entry", "transaction_currency"):
		default_currency = erpnext.get_default_currency()
		frappe.db.sql(
			"""UPDATE `tabJournal Entry Account` jea
			JOIN `tabJournal Entry` je
			ON jea.parent = je.name
			SET jea.debit_in_transaction_currency = jea.debit_in_account_currency,
			jea.credit_in_transaction_currency = jea.credit_in_account_currency,
			je.transaction_currency = %(default_currency)s,
			je.exchange_rate = 1
			WHERE je.transaction_currency is NULL""",
			{'default_currency': default_currency}
		)

