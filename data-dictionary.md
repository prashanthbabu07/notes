--
# data dictionary
--

we have a entity that needs to capture client inform -

entity name: client

    client name -
    type: string
    required: true (mandatory field)

        semantic rules -
            min length: 1
            max length: 100
            example: "john doe"

        business rules -
            the client name must be unique within the system.

    client type -
    type: string
    required: true (mandatory field)

        semantic validation -
            min length: 1
            max length: 50
            example: "self-serve"

        business rules -
            the client type must be one of the predefined values: "self-serve", "theorem managed"

    client logo -
    type: image
    required: false (optional field)

        semantic validation -
            file type: jpg, png
            max file size: 5mb

        business rules -
            if provided, the client logo must be unique within the system.
            if not provided, a default logo will be used.


    client contacts -
    type: contact
    required: true (mandatory field)

        semantic validation -
            email: must be a valid email format
            phone: must be a valid phone number format

        business rules -
            the client contact must have at least one valid email or phone number.
            if both are provided, the email will be the primary contact method.
            should support multiple contacts.

if we need to capture more info then the client will become it's own independent entity.  i.e.
entity name: contact

    contact name -
    type: string
    required: true (mandatory field)

        semantic validation -
            min length: 1
            max length: 100
            example: "jane smith"

        business rules -
            the contact name must be unique within the client.

    contact email -
    type: string
    required: true (mandatory field)

        semantic validation -
            must be a valid email format

        business rules -
            the contact email must be unique within the client.

    contact phone -
    type: string
    required: false (optional field)

        semantic validation -
            must be a valid phone number format

        business rules -
            if provided, the contact phone must be unique within the client.

