from frappe.website.utils import delete_page_cache

def clear_contents(path):
	delete_page_cache("contents")

def list_old_images():
	import os, frappe

	for basepath, folders, files in os.walk(frappe.get_app_path("manual_erpnext_com", "www")):
		for fname in files:
			with open(os.path.join(basepath, fname), "r") as f:
				content = f.read()
				if "old_images" in content:
					print os.path.relpath(os.path.join(basepath, fname), frappe.get_app_path("manual_erpnext_com"))
