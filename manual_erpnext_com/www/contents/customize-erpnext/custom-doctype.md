DocType or Document Type is a tool to insert form in ERPNext. The forms like Sales Order,
Sales Invoices, Production Order are added as Doctype in the backend. Let's assume we are
creating a Custom Doctype for a Book.

Custom Doctype allows you to insert custom forms in ERPNext as per your requirement.

To create a new **DocType**, go to:

`Setup > Customize > Doctype > New`

#### Doctype Detail

1. Module: Select module in which this Doctype should be placed.
1. Document Type: Specify if this Doctype will be to carry master data, or to track transactions. Doctype
for book will be added as Master.
1. Is Child table: If this Doctype is to be inserted as table into another Doctype, like Item table
in the Sales Order Doctype, then you should check Is Child Table. Else no.
1. Is Single: If checked, this Doctype will become a single form, like Selling Setting, which user will
not be able to re-produce.
1. Custom?: This field will be checked by default when adding Custom Doctype.

![Docytype Basic](/assets/manual_erpnext_com/img/setup/customize/doctype-basics.png)

#### Fields

In the Fields Table, you can add the fields (properties) of the DocType (Article).

Fields are much more than database columns, they can be:

1. Columns in the database
1. For Layout (section / column breaks)
1. Child tables (Table type field)
1. HTML
1. Actions (button)
1. Attachments or Images

![Docytype fields](/assets/manual_erpnext_com/img/setup/customize/Doctype-all-fields.png)

When you add fields, you need to enter the **Type**. **Label** is optional for Section Break and Column Break. **Name** (`fieldname`) is the name of the database table column.

You can also set other properties of the field like whether it is mandatory, read only etc.

#### Naming

Define criteria based on which records will be named for this Doctype. You can have naming for this
Doctype's records done based on various criteria, as mentioned below.

![Docytype Naming](/assets/manual_erpnext_com/img/setup/customize/Doctype-naming.png)

#### Permission

In this table, you should select roles and define permission roles for them for this Doctype.

![Docytype Permissions](/assets/manual_erpnext_com/img/setup/customize/Doctype-permissions.png)

#### Save Doctype

On saving doctype, you will get pop-up to provide name for this Doctype.

![Docytype Save](/assets/manual_erpnext_com/img/setup/customize/Doctype-save.png)

#### Doctype in System

To check this Doctype, open Module defined for this doctype. Since we have added Books doctype in the
Human Resource module, to access this doctype, go to:

`Human Resource > Document > Book`

![Docytype List](/assets/manual_erpnext_com/img/setup/customize/Doctype-list-view.png)

#### Book master

Using the fields entered, following is the master one book.

![Docytype List](/assets/manual_erpnext_com/img/setup/customize/Doctype-book-added.png)
