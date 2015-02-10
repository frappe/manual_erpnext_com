# Email Alerts

You can configure various email alerts in your system to remind you of important activities such as:

1. Completion date of a Task.
1. Expected Delivery Date of a Sales Order.
1. Expected Payment Date.
1. If an Order greater than a particular value is received or sent.
1. Expiry notification for a Contract
1. Completion / Status change of a Task

For this, you need to setup an Email Alert.

> Setup > Email > Email Alert

### Setting Up An Alert

To setup an Email Alert:

1. Select which Document Type you want watch changes on
1. Define what events you want to watch. Events are:
	1. New: When a new document of the selected type is made.
	2. Save / Submit / Cancel: When a document of the selected type is saved, submitted, cancelled.
	3. Value Change: When a particular value in the selected type changes.
	4. Date Change: When the date matches a particular field in the document (this will be called at midnight when the date changes). You can also set "Days in Advance" incase you want to be reminded of the event in advance.
1. Set additional conditions if you want.
1. Set the recipients of this alert. The recipient could either be a field of the document or a list of fixed email ids.
1. Compose the message

#### Defining the Criteria

![Defining Criteria](/assets/erpnext_org/images/erpnext/setup/email-alert-1.png)

#### Setting the Recipients and Message

![Set Message](/assets/erpnext_org/images/erpnext/setup/email-alert-2.png)

