Production Order (also called as Work Order) is a document that is given to
the manufacturing shop floor by the Production Planner as a signal to produce
a certain quantity of a certain Item. Production Order also helps to generate
the material requirements (Stock Entry) for the Item to be produced from its
**Bill of Materials**.

The **Production Order** is generated directly from the **Production Planning
Tool** based on Sales Orders. You can also create a direct Production Order
by:

> Manufacturing > Production Order > New Production Order

#### Figure 1: Create Production Order

![Production Order](/assets/manual_erpnext_com/old_images/erpnext/production-order.png)

  * Select the Item to be produced (must have a Bill of Materials).
  * Select the BOM
  * Select Quantities
  * Select Warehouses. WIP (Work-in-Progress) is where your Items will be transferred when you begin production and FG (Finished Goods) where you store finished Items before they are shipped.
  * Mention the Planned Start Date (an Estimated Date at which you want the Production to begin.)
  * Select if you want to consider sub-assemblies (sub-Items that have their own BOM) as stock items or you want to explode the entire BOM when you make Stock Entries for this Item. What it means is that if you also maintain stock of your sub assemblies then you should set this as “No” and in your Stock Entries, it will also list the sub-assembly Item (not is sub-components).

and “Submit” the Production Order.

Once you “Submit”, you will see two more buttons:

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