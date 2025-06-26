# Data modeling

When it comes to data model for relational database, the core idea is to utilize normalization. i.e.

1NF - Each column/field in the table is atomic containing single value.
2NF - 
3NF - 

Let's say we want to capture information of a company, person and their address.

We can create following table 
company
    company_id
    company_name

company_address
    company_id
    address
    country
    state
    ...

person 
    person_id
    person_name
    ...

person_address
    person_id
    address
    country
    state
    ...


The information (columens) that is captured for address is the same for both company and person except their foreig key.
While this works but it's not ideal as there is code duplication that needs to work with both address table.

The same is also applicable for other related data i.e. email address, phone number etc.

company_[email/phone_number]
person_[email/phone_number]

The core idea is to think all of 
