The person who helps in selling your products or services is called a Sales Person.

Sales Person master is maintained in [tree struture](https://erpnext.com/kb/setup/managing-tree-structure-masters). This allows you defining the heirarchy within the Sales Team.

Following are the steps to setup Sales Person master in the ERPNext.

####Selling Module

To add/edit Sales Person, go to:

`Selling > Setup > Sales Person`
  
####Click on Parent to Add new Sales Person

A Sales Person Group called "Sales Team" will be created by default. You can click in it to find option to insert new parent and child Sales Person records. Sales Person master will be saved with the name of Sales Person.

![Sales Person Add](assets/erpnext_org/images/erpnext/sales-person-add.png)

In Group Node field, selecting "Yes" will set that Sales Person master a parent. You will be able to create further group and child Sales Persons under it.

If Group Node is updated as "No", it will be added as child Sales Person which you will be able to select in the sales transactions.

![Sales Person New](assets/erpnext_org/images/erpnext/sales-person-new.png)

While creating new Sales Person, it will ask for Employee if that Sales Person. Hence you should ensure that Employee ID is created for each Sales Person, or for each employee for that matter. This approach allows you to link Sales Person with Employee, and ensures no duplicate Sales Person records is created for any sales person.

![Sales Person Employee](assets/erpnext_org/images/erpnext/sales-person-employee.png)

####Sales Person in Transactions

You can use this Sales Person in Customer, and sales transactions like Sales Order, Delivery Note and Sales Invoice. Based on Sales Person mentioned in the transaction, you will performance report of Sales Persons. Click [here](https://erpnext.com/kb/selling/managing-sales-persons-in-sales-transactions) to learn more about how Sales Persons are used in the transactions of Sales Cycle.