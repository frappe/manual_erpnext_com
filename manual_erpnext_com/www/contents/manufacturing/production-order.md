Production Order (also called as Work Order) is a document that is given to
the manufacturing shop floor by the Production Planner as a signal to produce
a certain quantity of a certain Item. Production Order also helps to generate
the material requirements (Stock Entry) for the Item to be produced from its
**Bill of Materials**.

The **Production Order** is generated directly from the **Production Planning
Tool** based on Sales Orders. You can also create a direct Production Order
by:

> Manufacturing > Production Order > New Production Order

<img class="screenshot" alt="Production Order" src="/assets/manual_erpnext_com/img/manufacturing/production-order.png">

### Creating Production Orders

  * Select the Item to be produced.
  * The default BOM for that item will be fetched by the system. You can also change BOM.
  * If the selected BOM has operartion mentioned in it, the system shall fetch all operations from BOM.
  * Mention the Planned Start Date (an Estimated Date at which you want the Production to begin.)
  * Select Warehouses. Work-in-Progress Warehouse is where your Items will be transferred when you begin production and Target Warehouse is  where you store finished Items before they are shipped.

> Note : You can save a Production Order without selecting the warehouses, but warehouses are mandatory for submitting a Production Order

###Reassigning Workstation/Duration for Operations

* By default the system fetchs workstation and duration for Production Order Operations from the selected BOM.
* If you wish to reassign the wrokstation for a particular opeeration in the Production Order, you can do so before submitting the Production Order.
* Select the respective operation, and change its workstation.

* You can also change the Operating Time for that operation

### Capacity Planning in Production Order

* When a Production Order is submitted, based on the Planned Start Date and the availability of the workstations, system schedules all operations for the Production Order (if Production Order has operations specified).
* Drafts of Time Logs are also created based on the scheduled operations.
* You can specify parameters for capacity planning in Manufacturing Settings.
 
### Transfering Materials for Manufacturing

* Once you have submitted your Production Order, you need to Transfer the Raw Materials to initiate the Manufacturing Process.

* Click on 'Transfer Materials for Manufacturing'.

<img class="screenshot" alt="Transfer Materials" src="/assets/manual_erpnext_com/img/manufacturing/PO-material-transfer.png">

* Mention the quantity of materials to be transfered.

<img class="screenshot" alt="Material Transfer Qty" src="/assets/manual_erpnext_com/img/manufacturing/PO-material-transfer-qty.png">

* Submit the Stock Entry

<img class="screenshot" alt="Stock Entry for PO" src="/assets/manual_erpnext_com/img/manufacturing/PO-SE-for-material-transfer.png">

### Making Time Logs











#### Figure 2: Submit Production Order

![Production Order](/assets/manual_erpnext_com/old_images/erpnext/production-order-2.png)

  1. On Submitting the Production Order, the system will reserve a slot for each of the Production Order Operations serially after the planned start date based on the workstation availability. The Workstation availability depends on the Workstation timings, holiday list and if some other Production Order Operation was scheduled in that slot. You can mention the number of days for the system to try scheduling the operations in the Manufacturing Settings. This is set to 30 Days by default. If the operation requires time exceeding the available slot, system shall ask you to break the operations. Once the scheduling is done system shall create Time Logs and save them. You can Modify them and submit them later.
  2. You can also create additional time logs against an Operation. For doing so select the respective operation and click on 'Make Time Log'
  3. Transfer Raw Material: This will create a Stock Entry with all the Items required to complete this Production Order to be added to the WIP Warehouse. (this will add sub-Items with BOM as one Item or explode their children based on your setting above).
  4. Update Finished Goods: This will create a Stock Entry that will deduct all the sub-Items from the WIP Warehouse and add them to the Finished Goods Warehouse.
  5. To check all Time Logs made against the Production Order click on 'Show Time Logs'

> Tip: You can also partially complete a Production Order by updating the
Finished Goods stock creating a Stock Entry.

When you Update Finished Goods to the Finished Goods Warehouse, the “Produced
Quantity” will be updated in the Production Order.

> Note : In order to make a Production Order against an Item you must specify 'Yes' to "Allow Production Order" on the Item form.

{next}
