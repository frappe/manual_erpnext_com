# Manufacturing

<p class="lead"> To manufacture a product, a Production Order is made. Raw materials are transferred from the stores to the work-in-progress Warehouse before completion. After completion, the raw materials are consumed from the work-in-progress Warehouse and updated in the finished goods Warehouse.</p>

Production Orders can be made directly from the Manufacturing module or from the Production Planning Tool.

> Manufacturing > Production Order > New Production Order

#### Step 1: Save and submit the Production Order

A submitted Production Order has an Action button on the right hand corner which provides option to 'Transfer Raw materials' and Update Finished Goods'.

__Figure 1: Production Order Generated From PPT__

![Production Order](/assets/manual_erpnext_com/old_images/erpnext/m-t-o-production-order-ppt-jps-1.png)

After completion of the Production Order, transfer the raw materials from stores to the work-in-progress Warehouse.

### Transfer Raw Materials 

To transfer raw materials you can either use the 'Transfer Raw Material' button or raise a Stock Entry manually .

#### Step 2: Click on Action and select ‘Transfer Raw Material’
 
On this form, mention the Source Warehouse and the Target Warehouse. The Source Warehouse is a place from where you issue or transfer materials. A Target Warehouse is a place where Stock/Item is received. In this example, the system will  transfer raw materials from the stores Warehouse to the work-in-progress Warehouse. The raw materials which are transferred are pulled from the Bill of Materials of that product.

__Figure 2: Transfer raw material__

![Transfer raw material](/assets/manual_erpnext_com/old_images/erpnext/m-t-o-stock-entry-1-jps.png)

> Note: If you get an error while transferring raw materials, it may be due to inaccurate 'purpose' selection, while making a manual Stock Entry. To transfer materials, the 'purpose' should be 'Material Transfer' and to transfer materials to finished goods Warehouse, the 'purpose' should be 'Manufacture/Repack'.

<i class="icon-lightbulb text-warning" style="font-size: 200%"></i> Tip: If you get negative error, ensure that you have enough Stock. Your Purchase Receipt should be saved and submitted.

After transferring the material to the work-in-progress Warehouse, the product gets manufactured. After completion, it is essential to shift the finished product to the finished goods Warehouse. Thus, one more Stock Entry has to be done that updates the finished goods in the Warehouse. 

### Update Finished Goods 

Under this section, you will mention your source Warehouse as 'Work-in-progress-SOG' and target Warehouse as 'Finished Goods-SOG'. The purpose will be Manufacture/Repack. This is so because, once the product gets manufactured, it is supposed to go to finished goods Stock to enable delivery.

#### Step 3: Click on Update Finished Goods

This step performs the backflush by raising a Stock Entry for materials that have been consumed while manufacturing the finished goods Item.

__Figure 3: Update finished goods__

![Update finished goods](/assets/manual_erpnext_com/old_images/erpnext/m-t-o-update-finished-goods.png)

> Note: (a) If you wish to get Stock and valuation rates at this stage, press on ‘Get Stock and Rate’. Valuation rate is the average rate divided by the actual price of an item. This is arrived at by the FIFO method - weighted average of the lot.
(b) At this stage if you wish to change the BOM manufacturing quantity, you can do so by clicking on ‘Get Items’.

Save and submit the document. To see if everything has occurred as planned, go back to the Production Order. The Production Order will show that it is 100% complete. The green line will be complete. After manufacturing the product is delivered and billed.

Next: [Shipping and Billing](/guide-books/make-to-order/shipping-and-billing)