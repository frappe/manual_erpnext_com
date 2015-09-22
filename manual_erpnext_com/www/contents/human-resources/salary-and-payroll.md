Salary is a fixed amount of money or compensation paid to an employee by an employer in return for the work performed . 

Payroll is the administration of financial records of employees' salaries, wages, bonuses, net pay, and deductions.

To process Payroll in ERPNext,

  1. Create Salary Structures for all Employees.
  2. Generate Salary Slips via Process Payroll.
  3. Book the Salary in your Accounts.

### Salary Structure

The Salary Structure represents how Salaries are calculated based on Earnings
and Deductions. 

Salary structures are used to help organizations:
  1. Maintain pay levels that are competitive with the external labor market,
  2. Maintain internal pay relationships among jobs,
  3. Recognize and reward differences in level of responsibility, skill, and performance, and manage pay expenditures.

The usual components of the salary structure (in india) include:

__Basic Salary:__ It is the taxable base income and generally not more than 40% of CTC.

__House Rent Allowance:__ The HRA constitutes 40 to 50% of the basic salary.

__Special Allowances:__ Makes up for the remainder part of the salary, mostly smaller than the basic salary which is completely taxable.

__Leave Travel Allowance:__ The non-taxable amount paid by the employer to the employee for vacation/trips with family within India.

__Gratuity:__ It is basically a lump sum amount paid by the employer when the employee resigns from the organization or retires.

__PF:__ Fund collected during emergency or old age. 12% of the basic salary is automatically deducted and goes to the employee provident fund.

__Medical Allowance:__ The employer pays the employee for the medical expenditures incurred. It is tax free up to Rs.15,000.

__Bonus:__ Taxable part of the CTC, usually a once a year lump sum amount, given to the employee based on the individual’s as well as the organizational performance for the year.

__Employee Stock Options:__ ESOPS are Free/discounted shares given by the company to the employees. This is done to primarily increase employee retention.

To create a new Salary Structure go to:

> Human Resources > Setup > Salary Structure > New Salary Structure

#### Figure 1:Salary Structure

<img class="screenshot" alt="Salary Structure" src="/assets/manual_erpnext_com/img/human-resources/salary-structure.png">

### In the Salary Structure,

  * Select the Employee
  * Set the starting date from which this is valid (Note: There can only be one Salary Structure that can be “Active” for an Employee during any period)
  * In the “Earnings” and “Deductions” table all your defined Earning Type and Deductions Type will be auto-populated. Set the values of the Earnings and Deductions and save the Salary Structure.

### Leave Without Pay (LWP)

Leave Without Pay (LWP) happens when an Employee runs out of allocated leaves
or takes a leave without an approval (via Leave Application). If you want
ERPNext to automatically deduct salary in case of LWP, then you must check on
the “Apply LWP” column in the Earning Type and Deduction Type masters. The
amount of pay cut is the proportion of LWP days divided by the total working
days for the month (based on the Holiday List).

If you don’t want ERPNext to manage LWP, just don’t click on LWP in any of the
Earning Types and Deduction Types.

* * *

### Creating Salary Slips

Once the Salary Structure is created, you can make a salary slip from the same
form or you can process your payroll for the month using Process Payroll.

To create a salary slip from Salary Structure, click on the button Make Salary
Slip.

#### Figure 2: Salary Slip

<img class="screenshot" alt="Salary Slip" src="/assets/manual_erpnext_com/img/human-resources/salary-slip.png">

You can also create salary slip for multiple employees using Process Payroll:

> Human Resources > Process Payroll

#### Figure 3: Process Payroll

<img class="screenshot" alt="Process Payroll" src="/assets/manual_erpnext_com/img/human-resources/process-payroll.png">

In Process Payroll,

  1. Select the Company for which you want to create the Salary Slips.
  2. Select the Month and the Year for which you want to create the Salary Slips.
  3. Click on “Create Salary Slips”. This will create Salary Slip records for each active Employee for the month selected. If the Salary Slips are created, the system will not create any more Salary Slips. All updates will be shown in the “Activity Log” section.
  4. Once all Salary Slips are created, you can check if they are created correctly or edit it if you want to deduct Leave Without Pay (LWP).
  5. After checking, you can “Submit” them all together by clicking on “Submit Salary Slips”. 1. If you want them to be automatically emailed to the Employee, make sure to check the “Send Email” box.

### Booking Salaries in Accounts

The final step is to book the Salaries in your Accounts.

Salaries in businesses are usually dealt with extreme privacy. In most cases,
the companies issues a single payment to the bank combining all salaries and
the bank distributes the salaries to each employee’s salary account. This way
there is only one payment entry in the company’s books of accounts and anyone
with access to the company’s accounts will not have access to the individual
salaries.

The salary payment entry is a Journal Entry entry that debits the total
salary of all Employees to the Salary Account and credits the company’s bank
Account.

To generate your salary payment voucher from Process Payroll, click on
“Make Bank Voucher” and a new Journal Entry with the total salaries will be
created.

{next}
