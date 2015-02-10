Batch inventory feature in ERPNext allows you to group multiple units of an item, and assign them a unique value/number/tag called Batch No.

The practise of stocking based on batch is mainly followed in the pharmaceutical industry. Medicines/drugs produced in a particular batched is assigned a unique id. This helps them updating and tracking manufacturing and expiry date for all the units produced under specific batch.

To set item as a batch item, "Has Batch No" field should be updated as Yes in the Item master.

![Batch Item](assets/erpnext_org/images/erpnext/batch-item.png)

On every stock transaction (Purchase Receipt, Delivery Note, POS Invoice) made for batch item, you should provider item's Batch No. To create new Batch No. master for an item, go to:

> Stock >> Setup >> Batch >> New

Batch master is created before creation of Purchase Receipt. Hence eveytime their is Purchase Receipt or Production entry being made for a batch item, you will first create its Batch No, and then select it in Purcase order or Production Entry.

Following are the steps to create Batch ID:

**Step 1: Enter Batch No and Item Code**

Batch No will be defined based on value entered in Batch ID.

![Batch ID](assets/erpnext_org/images/erpnext/batch-id.png)

> Batch can have only one Item in it.

**Step 2: Enter Description and Dates**

![Batch Details](assets/erpnext_org/images/erpnext/batch-details.png)

In stock transactions, Batch IDs will be filtered based on Item Code, Warehouse, Batch Expiry Date (compared with Posting date of a transaction) and Actual Qty in Warehouse. While searching for Batch ID  without value in Warehouse field, then Actual Qty filter won't be applied.

**Batch No. in Purchase Receipt**

![Batch Receipt](assets/erpnext_org/images/erpnext/batch-receipt.png)

**Batch No. in Delivery Note**

![Batch Delivery](assets/erpnext_org/images/erpnext/batch-delivery.png)

Batchwise Stock Balance Report

To check batchwise stock balance report, go to:

Stock >> Standard Reports >> Batch-wise Balance History

![Batch Report](assets/erpnext_org/images/erpnext/batch-report.png)