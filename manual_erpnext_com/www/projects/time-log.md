## Time Sheets

You can create Time Sheets to track billable work to Customers and also for your internal references. These Time
Sheets can be tracked against Project, Tasks or Production Order Operations so that you can get reports on
how much time was spent on each.

![Time Log](assets/manual_erpnext_com/old_images/erpnext/time-log.png)

Time Logs are a way to track time worked. Time Logs can also be grouped together, or "Batched" for billing. This way you can track whether Time Logs are billed or not. You can also check out the Time Logs in Calender view or in Gantt View

__Step 1: Create a new Time Log__

![Time Log](assets/manual_erpnext_com/old_images/erpnext/timelog1.jpg)

To create a new Time Log, you can go to Projects > Time Log and click on "New Time Log" or click on the calendar view, switch to Daily View and drag on the timeslots to create a new Time Log. Time Logs for Manufacturing processes needs to be created from the Production Order. When a Production Order is submitted, the operations are auto-scheduled and time logs are generated against each operation. To create more Time Logs against Operations select the respective operation and click on the 'Make Time Log' button.

![Time Log](assets/manual_erpnext_com/old_images/erpnext/timelog2.jpg)

In the Time Log, define the Activity Type (this is an easy way to identify the type of activity), Empoyee and update the Project or Task it is worked on. If the Time is billable to the Customer, check the "Billable" box. The system will pull the costing rate and the billing rate from Activity Cost once Activity Type is selected against an Employee. Based on the Hours mentioned in the Time Log, the system will calculate the Costing amount & the Billing Amount. If the Time log is not 'billable' the system will fetch the billing rate but compute the billing amount as 0. On Submission the system will update the respective Task and Project with the costing and billing amount

![Time Log](assets/manual_erpnext_com/old_images/erpnext/timelog3.jpg)

__Step 2. Batching Time Logs for Billing__

You can bill Time Logs by batching them together. This gives you the flexiblity to manage your customer billing in the way you want. To create a new Time Log Batch, go to Projects > Time Log Batch > New Time Log Batch

OR

Just open your Time Log list and check the Items to you want to add to the Time Log. Then click on "Make Time Log Batch" button and these Time Logs will be selected.

![Time Log](assets/manual_erpnext_com/old_images/erpnext/timelog4.jpg)

Once you are satisfied with your Time Log Batch, "Submit" it

![Time Log](assets/manual_erpnext_com/old_images/erpnext/timelog5.jpg)

__Step 3. Making a Sales Invoice__

After submitting the Time Log Batch, click on the "Make Invoice" button. When you click on that button, a new Sales Invoice will open with the total number of hours as "Quantity".

![Time Log](assets/manual_erpnext_com/old_images/erpnext/timelog6.jpg)

Notice that the Time Log Batch number is already updated in the Time Log Batch column and this will be the link of this Invoice to the Time Logs.

![Time Log](assets/manual_erpnext_com/old_images/erpnext/timelog7.jpg)

When you "Submit" the Sales Invoice, the Sales Invoice number will get updated in the Time Logs and Time Log Batch and their status will change to "Billed".

