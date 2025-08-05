app_name = "asa_thomas"
app_title = "Asa Thomas"
app_publisher = "thomas"
app_description = "test"
app_email = "thomas@gmail.com"
app_license = "mit"






fixtures = [
    {"dt": "Workflow", "filters": [["document_type", "=", "Annual Service Agreement"]]},
    {"dt": "Role", "filters": [["role_name", "in", [
        "SLA Manager",
        "SLA Reviewer"
    ]]
    ]},
    {"dt": "Workflow State", "filters": [["workflow_state_name", "in", ["Suspended"]]]},
{"dt": "Workflow Action Master", "filters": [["workflow_action_name", "in", ["Suspend"]]]},


]
# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "asa_thomas",
# 		"logo": "/assets/asa_thomas/logo.png",
# 		"title": "Asa Thomas",
# 		"route": "/asa_thomas",
# 		"has_permission": "asa_thomas.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/asa_thomas/css/asa_thomas.css"
# app_include_js = "/assets/asa_thomas/js/asa_thomas.js"

# include js, css files in header of web template
# web_include_css = "/assets/asa_thomas/css/asa_thomas.css"
# web_include_js = "/assets/asa_thomas/js/asa_thomas.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "asa_thomas/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "asa_thomas/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "asa_thomas.utils.jinja_methods",
# 	"filters": "asa_thomas.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "asa_thomas.install.before_install"
# after_install = "asa_thomas.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "asa_thomas.uninstall.before_uninstall"
# after_uninstall = "asa_thomas.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "asa_thomas.utils.before_app_install"
# after_app_install = "asa_thomas.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "asa_thomas.utils.before_app_uninstall"
# after_app_uninstall = "asa_thomas.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "asa_thomas.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"asa_thomas.tasks.all"
# 	],
# 	"daily": [
# 		"asa_thomas.tasks.daily"
# 	],
# 	"hourly": [
# 		"asa_thomas.tasks.hourly"
# 	],
# 	"weekly": [
# 		"asa_thomas.tasks.weekly"
# 	],
# 	"monthly": [
# 		"asa_thomas.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "asa_thomas.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "asa_thomas.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "asa_thomas.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["asa_thomas.utils.before_request"]
# after_request = ["asa_thomas.utils.after_request"]

# Job Events
# ----------
# before_job = ["asa_thomas.utils.before_job"]
# after_job = ["asa_thomas.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"asa_thomas.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

