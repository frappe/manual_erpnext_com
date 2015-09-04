# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "manual_erpnext_com"
app_title = "manual_erpnext_com"
app_publisher = "Frappe"
app_description = "manual.erpnext.com"
app_icon = "icon-globe"
app_color = "blue"
app_email = "info@frappe.io"
app_version = "0.0.1"

website_route_rules = [
	{"from_route": "/search", "to_route": "Web Page"}
]

website_context = {
	"brand_html": "<img class='navbar-icon' src='/assets/frappe_theme/img/erp-icon.svg' />The ERPNext Manual",
	"top_bar_items": [
		{"label": "Videos", "url": "/videos", "right": 1},
		{"label": "Knowledge Base", "url": "https://kb.erpnext.com", "right": 1, "target": 'target="_blank"'},
	],
	"hide_login": 1,
	"include_search": 1,
	"page_titles": {
		"kb": "ERPNext Manual"
	},
	"js_globals": {
		"search_path": "/search"
	},
	"custom_footer": """<div class="text-extra-muted manual-feedback" style="padding-bottom: 70px;">
		<a class="underline" href="https://discuss.frappe.io" target="_blank">
			Have questions? Ask at the forum.</a></div>""",
	"favicon": "/assets/frappe_theme/img/favicon.ico",
}

website_clear_cache = "manual_erpnext_com.utils.clear_contents"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/manual_erpnext_com/css/manual_erpnext_com.css"
# app_include_js = "/assets/manual_erpnext_com/js/manual_erpnext_com.js"

# include js, css files in header of web template
web_include_css = "/assets/frappe_theme/css/lightbox.css"
web_include_js = ["/assets/frappe_theme/js/lightbox.min.js",
	"/assets/manual_erpnext_com/js/setup_lightbox.js"]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "manual_erpnext_com.install.before_install"
# after_install = "manual_erpnext_com.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "manual_erpnext_com.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"manual_erpnext_com.tasks.all"
# 	],
# 	"daily": [
# 		"manual_erpnext_com.tasks.daily"
# 	],
# 	"hourly": [
# 		"manual_erpnext_com.tasks.hourly"
# 	],
# 	"weekly": [
# 		"manual_erpnext_com.tasks.weekly"
# 	]
# 	"monthly": [
# 		"manual_erpnext_com.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "manual_erpnext_com.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "manual_erpnext_com.event.get_events"
# }

fixtures = ["Contact Us Settings"]
