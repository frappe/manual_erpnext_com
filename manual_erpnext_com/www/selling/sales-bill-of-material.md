Sales BOM stands for Sales Bill-of-Material. It's a master where you can list item which are bundled together and sold as one item. For instance, when laptop is delivered, you need to ensure that charger, mouse and laptop bag are delivered and stock level of these items gets affected. To address this scenario, you can set create Sales BOM for the main item, i.e. laptop, and list deliverable items i.e. laptop + charger + other accessories as child items.
  
Following are the steps on how to setup Sales BOM master, and how is it used in the sales transactions.

####Create new Sales BOM

To create new Sales BOM, Go to:

Selling >> Setup >> Sales BOM >> New

####Select Parent Item

In Sales BOM master, there are two sections. Sales BOM Item and Package Item.

In Sales BOM item, you will select a Parent Item. The parent item must be a <b>non-stock item</b>. This is non-stock item because there is no stock maintained for it but only the Package Items. If you want to maintain stock for the Parent Item, then you must create a regular Bill of Material (BOM) and package them using a Stock Entry Transactions.

In our case, the parent item is PC.

![Sales BOM Item](assets/erpnext_org/images/erpnext/sales_bom_item.png)

####Select Child Items

In Package Item section, you will list all the child items for which we maintain stock and is delivered to customer.The actual laptop item, mouse, charger and laptop bag will be listed in the table of Package Item.

![Sales BOM Packed Items](assets/erpnext_org/images/erpnext/sales_bom_packed_items.png)

####Save Sales BOM

Save Sales BOM after enter Sales BOM and Packing Items, with Qty. Once Sales BOM is saved, it will not be editable again.

####Sales BOM in the Sales Transactions

When making Sales transactions like Sales Invoice, Sales Order and Delivery Note, Parent Item will be selected in the main item table.

![Sales BOM Main in Transaction](assets/erpnext_org/images/erpnext/sales_bom_main_in_transaction.png)

On selection on Parent Item in the main item table, its child items will be fetched in Packing List table of the transaction. If child item is the serialized item, you will be able to specify its Serial Mo. in packing List table itself. On submission of transaction, system will reduce the stock level of child items from warehouse specified in Packing List table.

![Sales BOM Child in Transaction](assets/erpnext_org/images/erpnext/sales_bom_child_in_transaction.png)

<div class="well"><b>Use Sales BOM to Manage Schemes:</b>
<br>
This work-around in Sales BOM was discovered when a customer dealing into nutrition product asked for feature to manage schemes like "Buy One Get One Free". To manage the same, he created a non-stock item which was used as Parent Item. In description of item, he entered scheme details with items image indicating the offer. The saleable product was selected in Package Item where qty was two. Hence every time they sold one qty of Parent item under scheme, system deducted two quantities of product from Warehouse.</div>