# Manufacturing

<p class="lead"> To manufacture a product, a Production Order is made. Raw materials are transferred from the stores to the work-in-progress Warehouse before completion. After completion, the raw materials are consumed from the work-in-progress Warehouse and updated in the finished goods Warehouse.</p>

### Production Order

Production Order (also called as Work Order) is a document that is given to the manufacturing shop floor by the production planner as a signal to produce a certain quantity of  certain Item. Production Order also helps to generate the material requirements (Stock Entry) for the Item to be produced from its Bill of Materials.

> Manufacturing > Production Order > New Production Order

__Figure 1: Production Order__

![Production Order](/assets/manual_erpnext_com/old_images/erpnext/m-t-s-po-butterflyprint.png)

Save and submit the Production Order. An Action button will appear at the extreme right of the form. It will have a drop-down button. Click on Transfer Raw Materials to proceed further. 

#### Step 1: Stores to Work-in-Progress (WIP)

Materials which are in stores need to be transferred to the work-in-progress Warehouse. Work-in-progress Warehouses, are basically your Workstations, where you manufacture your products. Even if you do not have a seperate workspace for manufacturing, in the system, mention a place called 'Work-in-Progress' and transfer your material to this place on Stock Entry.

__Figure 2: Stock Entry with Warehouse Details.__

![Transfer Material 2](/assets/manual_erpnext_com/old_images/erpnext/m-t-s-transfer-material.png)

Note that transferring the raw material is a Stock Entry. To be able to manufacture, you are required to transfer your raw-material from the stores to the work-in-progress Warehouse. The Stock Entry specifies the transfer of goods from one Warehouse to other. After the final product is manufactured in the work-in-progress it is necessary to transfer it to a Finished Goods Warehouse. This transaction, has to be shown in another Stock Entry.

To make this Stock Entry directly, click on the Action button of the Production Order and select Update Finished Goods.

<i class="icon-lightbulb text-warning" style="font-size: 200%"></i> Tip: To go to your Production Order you may use a shortcut route. Go to the head bar at the top ( the black bar) and click on History. Then, select the respective Production Order.

#### Step 2: Back Flush: From Work-in-Progress (WIP) to Finished Goods

Back flush means to consume raw materials gone into the making of the product. 
After clicking on Update Finished Goods, a Stock Entry form will appear.  Fill that form. Update source Warehouse and target Warehouse. The source Warehouse is a place from where you issue or transfer materials. A target Warehouse is a place where Stock/Item is received. In this case it will be Finished Goods-SOG

Note that this Stock Entry will have its purpose as Manufacture/Repack. In this form mention the source Warehouse as work-in-progress Warehouse and target Warehouse as Finished Goods Warehouse. Then click on ‘Get Stock and Rate’. Save and submit the document.

__Figure 3: Update Finished Goods__

![Update](/assets/manual_erpnext_com/old_images/erpnext/m-t-s-update-fg.png)

Since this is a make-to-stock product, the billing will not happen immediately. Money will be recovered only when these products are sold at an exhibition or when a retailer buys them.



Next: [Selling and Customer Billing](/guide-books/make-to-stock/selling)
