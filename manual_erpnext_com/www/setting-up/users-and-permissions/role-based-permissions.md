# Role Based Permissions

<p class="lead">ERPNext has a role-based permission system.</p>

It means that you can assign Roles to Users, and set Permissions on Roles. The permission structure also allows you to define different permission rules for different fields, using a concept called **Permission "Level"** of a field. Once roles are assigned to a user, it gives you the ability to limit access for a user to only specic documents.

To start with, go to:
> Setup > Users and Permissions > Role Permissions Manager

<figure>
	<img src="/assets/erpnext_org/images/erpnext/setting-up-permissions-leave-application.png"
		class="img-responsive" alt="Role Permissions Manager">
	<figcaption>Manage Read, Write, Create, Submit, Amend access using the Role Permissions Manager</figcaption>
</figure>

Permissions are applied on a combination of:

  * **Roles:** As we saw earlier, Users are assigned to Roles and it is on these Roles that permission rules are applied.

  *Examples of Roles include Accounts Manager, Employee, HR User.*

  * **Document Types:** Each type of document, master or transaction, has a separate list of Role based permissions.

  *Examples of Document Types are Sales Invoice, Leave Application, Stock Entry, etc.*

  * **Permission "Levels":** In each document, you can group fields by "levels". Each group of field is denoted by a unique number (0, 1, 2, 3, etc.). A separate set of permission rules can be applied to each field group. By default all fields are of level 0.

    *Permission "Level" connects the group of fields with level X to a permission rule with level X.*

  * **Document Stages:** Permissions are applied on each stage of the document like on Creation, Saving, Submission, Cancellation and Amendment. A role can be permitted to Print, Email, Import or Export data, access Reports, or define User Permissions.

  * **Apply User Permissions:** This switch decides whether User Permissions should be applied for the role on selected Document Stages.

	If enabled, a user with that role will be able to access only specific Documents for that Document Type. Such specific Document access is defined in the list of User Permissions. Additionally, User Permissions defined for other Document Types also get applied if they are related to the current Document Type through Link Fields.

	To set, User Permissions go to:
    > Setup > Users and Permissions > [User Permissions Manager](/setting-up/permissions/user-permissions)

---

**To add a new rule**, click on "Add a New Rule" button and a pop-up box will ask you to select a Role and a Permission Level. Once you select this and click on "Add", this will add a new row to your rules table.

---

Leave Application is a good **example** that encompasses all areas of Permission System.

<figure>
	<img src="/assets/erpnext_org/images/erpnext/setting-up-permissions-leave-application-form.png"
		class="img-responsive" alt="Leave Application Form">
	<figcaption>Leave Application Form should be created by an Employee, and approved by Leave Approver or HR User</figcaption>
</figure>

   1. **It should be created by an Employee.**
     For this, Employee Role should be given Read, Write, Create permissions.

	 <figure>
	 	<img src="/assets/erpnext_org/images/erpnext/setting-up-permissions-employee-role.png"
	 		class="img-responsive" alt="Leave Application Permissions for Employee Role">
	 	<figcaption>Giving Read, Write and Create Permissions to Employee for Leave Application</figcaption>
	 </figure>

   1. **An Employee should only be able to access his/her Leave Application.**
     Hence, Apply User Permissions should be enabled for Employee Role, and a User Permission record should be created for each User Employee combination. (This effort is reduced for Employee Document Type, by programmatically creating User Permission records.)

	 <figure>
	 	<img src="/assets/erpnext_org/images/erpnext/setting-up-permissions-employee-user-permissions.png"
	 		class="img-responsive" alt="Leave Application User Permissions for a User with Employee Role">
	 	<figcaption>Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager</figcaption>
	 </figure>

   1. **HR Manager should be able to see all Leave Applications.**
     Create a Permission Rule for HR Manager at Level 0, with Read permissions. Apply User Permissions should be disabled.

	 <figure>
	 	<img src="/assets/erpnext_org/images/erpnext/setting-up-permissions-hr-manager-role.png"
	 		class="img-responsive" alt="Leave Application Permissions for HR Manager">
	 	<figcaption>Giving Submit and Cancel permissions to HR Manager for Leave Applications.
			'Apply User Permissions' is unchecked to give full access.</figcaption>
	 </figure>

   1. **Leave Approver should be able to see and update Leave Applications applicable to him/her.**
     Leave Approver is given Read and Write access at Level 0, with Apply User Permissions enabled. Relevant Employee Documents should be enlisted in the User Permissions of Leave Approvers. (This effort is reduced for Leave Approvers mentioned in Employee Documents, by programmatically creating User Permission records.)

	 <figure>
	 	<img src="/assets/erpnext_org/images/erpnext/setting-up-permissions-leave-approver-role.png"
	 		class="img-responsive" alt="Leave Application Permissions for Leave Approver">
	 	<figcaption>Giving Read, Write and Submit permissions to Leave Approver for Leave Applications.
			'Apply User Permissions' is checked to limit access based on Employee.</figcaption>
	 </figure>

   1. **It should be Approved / Rejected only by HR User or Leave Approver.**
     The Status field of Leave Application is set at Level 1. HR User and Leave Approver are given Read and Write permissions for Level 1, while everyone else (All) are given Read permission for Level 1.

	 <figure>
	 	 	<img src="/assets/erpnext_org/images/erpnext/setting-up-permissions-level-1.png"
	 	 		class="img-responsive" alt="Leave Application Permissions for Level 1">
	 	 	<figcaption>Limiting read access for a set of fields to certain Roles</figcaption>
	 	 </figure>

   1. **HR User should be able to delegate Leave Applications to his/her subordinates**
     HR User is given the right to Set User Permissions. A User with HR User role would be able to defined User Permissions on Leave Application for other users.

	 <figure>
	 	 	<img src="/assets/erpnext_org/images/erpnext/setting-up-permissions-hr-user-role.png"
	 	 		class="img-responsive" alt="Leave Application Permissions for HR User">
	 	 	<figcaption>Let HR User delegate access to Leave Applications by checking 'Set User Permissions'. This will allow HR User to access User Permissions Manager for 'Leave Application'</figcaption>
	 	 </figure>

{next}
