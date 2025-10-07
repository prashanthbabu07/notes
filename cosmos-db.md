# emulator for cosmos db
1. Run a new container using the container image and the following configuration:
docker run \
    --publish 8081:8081 \
    --publish 10250-10255:10250-10255 \
    --name azure-cosmos-emulator \
    --detach \
    mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest

2. Navigate to https://localhost:8081/_explorer/index.html to access the data explorer.

I went with using azure for creating cosmos as there is a learning verion and free usage with limits.

1 RU is 1 KB. This is how RU are calculated and used for billing.

The cosmos db for NoSql support SQL queries.

when designing the model for nosql think in terms of embedding patters for relationships.

example 
    order and order details. (bounded embeddings)

full embedding
partial embedding
two way embedding - many to many

RDBMS to Consmos NoSql

Database - Cosmos DB 
Schema - not applicable  
Table - Container 
Columns - Doc props


# Cosmos DB Relational Patterns - Embedded Modeling Guide

This guide demonstrates how to model traditional relational database patterns in Cosmos DB using embedded patterns.

## 1. One-to-Many Relationships

### Pattern 1: Embed Child Collection (Recommended when children are small and bounded)

**Relational Model:**
```sql
-- Customer Table
Customer: CustomerId, Name, Email
-- Orders Table  
Order: OrderId, CustomerId, OrderDate, Total
```

**Cosmos DB Embedded Model:**
```json
{
  "id": "customer-12345",
  "customerId": "12345",
  "name": "John Doe",
  "email": "john@example.com",
  "orders": [
    {
      "orderId": "order-001",
      "orderDate": "2025-06-30T10:00:00Z",
      "total": 150.00,
      "status": "shipped"
    },
    {
      "orderId": "order-002", 
      "orderDate": "2025-06-28T14:30:00Z",
      "total": 89.99,
      "status": "pending"
    }
  ],
  "cosmosDocType": "customer",
  "_partitionKey": "12345"
}
```

### Pattern 2: Reference Pattern (When children are large or unbounded)

**Customer Document:**
```json
{
  "id": "customer-12345",
  "customerId": "12345", 
  "name": "John Doe",
  "email": "john@example.com",
  "cosmosDocType": "customer",
  "_partitionKey": "12345"
}
```

**Order Documents (separate):**
```json
{
  "id": "order-001",
  "orderId": "order-001",
  "customerId": "12345",
  "orderDate": "2025-06-30T10:00:00Z",
  "total": 150.00,
  "cosmosDocType": "order",
  "_partitionKey": "12345"
}
```

## 2. Many-to-Many Relationships

### Pattern 1: Embed Arrays of References

**Relational Model:**
```sql
-- Student Table
Student: StudentId, Name
-- Course Table
Course: CourseId, Title  
-- StudentCourse Junction Table
StudentCourse: StudentId, CourseId, EnrollmentDate, Grade
```

**Cosmos DB Embedded Model:**
```json
{
  "id": "student-12345",
  "studentId": "12345",
  "name": "Jane Smith",
  "enrollments": [
    {
      "courseId": "math-101",
      "courseTitle": "Calculus I",
      "enrollmentDate": "2025-01-15T00:00:00Z",
      "grade": "A",
      "credits": 3
    },
    {
      "courseId": "phys-201", 
      "courseTitle": "Physics II",
      "enrollmentDate": "2025-01-15T00:00:00Z",
      "grade": "B+",
      "credits": 4
    }
  ],
  "cosmosDocType": "student",
  "_partitionKey": "12345"
}
```

**Course Document (with enrolled students):**
```json
{
  "id": "course-math-101",
  "courseId": "math-101", 
  "title": "Calculus I",
  "credits": 3,
  "enrolledStudents": [
    {
      "studentId": "12345",
      "studentName": "Jane Smith",
      "enrollmentDate": "2025-01-15T00:00:00Z",
      "grade": "A"
    },
    {
      "studentId": "67890",
      "studentName": "Bob Johnson", 
      "enrollmentDate": "2025-01-15T00:00:00Z",
      "grade": "B"
    }
  ],
  "cosmosDocType": "course",
  "_partitionKey": "math-101"
}
```

### Pattern 2: Junction Document Pattern (For complex many-to-many)

**Enrollment Document:**
```json
{
  "id": "enrollment-12345-math101",
  "studentId": "12345",
  "courseId": "math-101",
  "enrollmentDate": "2025-01-15T00:00:00Z",
  "grade": "A",
  "assignments": [
    {
      "name": "Homework 1",
      "score": 95,
      "submittedDate": "2025-02-01T23:59:00Z"
    }
  ],
  "cosmosDocType": "enrollment",
  "_partitionKey": "12345"
}
```

## 3. One-to-One Relationships

### Pattern 1: Embed Related Data

**Relational Model:**
```sql
-- User Table
User: UserId, Username, Email
-- UserProfile Table
UserProfile: UserId, FirstName, LastName, Bio, Avatar
```

**Cosmos DB Embedded Model:**
```json
{
  "id": "user-12345",
  "userId": "12345",
  "username": "johndoe",
  "email": "john@example.com",
  "profile": {
    "firstName": "John",
    "lastName": "Doe", 
    "bio": "Software developer passionate about cloud technologies",
    "avatar": "https://example.com/avatars/john.jpg",
    "dateOfBirth": "1990-05-15T00:00:00Z",
    "address": {
      "street": "123 Main St",
      "city": "Seattle",
      "state": "WA",
      "zipCode": "98101"
    }
  },
  "cosmosDocType": "user",
  "_partitionKey": "12345"
}
```

## 4. Complex Nested Relationships (Order with Items)

**Relational Model:**
```sql
-- Order Table
Order: OrderId, CustomerId, OrderDate, Total
-- OrderItem Table  
OrderItem: OrderItemId, OrderId, ProductId, Quantity, Price
-- Product Table
Product: ProductId, Name, Description, Price
```

**Cosmos DB Embedded Model:**
```json
{
  "id": "order-98765",
  "orderId": "98765",
  "customerId": "12345",
  "customerName": "John Doe",
  "orderDate": "2025-06-30T10:00:00Z",
  "status": "processing",
  "shippingAddress": {
    "street": "123 Main St",
    "city": "Seattle", 
    "state": "WA",
    "zipCode": "98101"
  },
  "items": [
    {
      "orderItemId": "item-001",
      "productId": "prod-12345",
      "productName": "Wireless Headphones",
      "quantity": 2,
      "unitPrice": 75.00,
      "totalPrice": 150.00,
      "productDetails": {
        "brand": "TechBrand",
        "model": "WH-1000XM4",
        "color": "Black"
      }
    },
    {
      "orderItemId": "item-002", 
      "productId": "prod-67890",
      "productName": "USB-C Cable",
      "quantity": 1,
      "unitPrice": 15.99,
      "totalPrice": 15.99
    }
  ],
  "payment": {
    "method": "credit_card",
    "last4": "1234",
    "transactionId": "txn-abc123"
  },
  "totals": {
    "subtotal": 165.99,
    "tax": 13.28,
    "shipping": 9.99,
    "total": 189.26
  },
  "cosmosDocType": "order",
  "_partitionKey": "12345"
}
```

## 5. Partitioning Strategies

### By Tenant/Customer (Multi-tenant)
```json
{
  "_partitionKey": "tenant-123",
  "tenantId": "tenant-123",
  "cosmosDocType": "user",
  // ... other properties
}
```

### By Entity Type + ID
```json
{
  "_partitionKey": "customer-12345",
  "cosmosDocType": "order",
  "customerId": "12345",
  // ... other properties  
}
```

### By Date (Time-series data)
```json
{
  "_partitionKey": "2025-06",
  "cosmosDocType": "log",
  "timestamp": "2025-06-30T10:00:00Z",
  // ... other properties
}
```

## 6. Indexing Considerations

### Composite Indexes for Multi-property Queries
```json
{
  "indexingPolicy": {
    "compositeIndexes": [
      [
        {"path": "/customerId", "order": "ascending"},
        {"path": "/orderDate", "order": "descending"}
      ],
      [
        {"path": "/cosmosDocType", "order": "ascending"},
        {"path": "/status", "order": "ascending"}
      ]
    ]
  }
}
```

## 7. Query Patterns

### Single Document Queries (Efficient)
```sql
SELECT * FROM c 
WHERE c.id = 'customer-12345' 
  AND c._partitionKey = '12345'
```

### Cross-partition Queries (Less Efficient)
```sql
SELECT * FROM c 
WHERE c.cosmosDocType = 'order' 
  AND c.status = 'pending'
```

### Embedded Array Queries
```sql
SELECT c.id, c.name, i
FROM c 
JOIN i IN c.items
WHERE c._partitionKey = '12345'
  AND i.productId = 'prod-12345'
```

## Best Practices Summary

1. **Embed when:**
   - Related data is always accessed together
   - Child items are bounded (< 100 items typically)
   - Updates are infrequent or atomic

2. **Reference when:**
   - Child items are unbounded or large
   - Independent access patterns
   - Frequent independent updates

3. **Choose partition key wisely:**
   - Even distribution of data and workload
   - Supports your most common query patterns
   - Consider tenant-based partitioning for multi-tenant apps

4. **Denormalize strategically:**
   - Duplicate commonly accessed fields
   - Pre-calculate aggregates when possible
   - Accept some data redundancy for query performance

In Cosmos DB, **efficient point reads require both `id` and partition key**. If you don’t know the partition key (`city`), you have two options, but both have trade-offs:

### 1. Cross-partition query (not efficient)
You can query by `id` only:
```sql
SELECT * FROM c WHERE c.id = "person123"
```
But this scans all partitions, which is **slow and costly**.

---

### 2. Store a mapping from `id` to partition key (recommended workaround)
Maintain a **lookup/mapping container** or table where you store the mapping of `id` to `city`:
```json
{
  "id": "person123",
  "city": "London"
}
```
- First, query this mapping to get the `city` for the `id`.
- Then, use both `id` and `
city` for an efficient point read in your main container.

---

### 3. Use a synthetic partition key (if possible)
If you control document creation, you can create a synthetic partition key, e.g., `city_id: "London_person123"`, and use that as the partition key. This allows efficient lookups by a single value.


## permissions to perform action [Microsoft.DocumentDB/databaseAccounts/readMetadata]

`
az cosmosdb sql role assignment create \
    --account-name "cosmos-learning-db" \
    --resource-group "<YourResourceGroupName>" \
    --scope "/" \
    --principal-id "291805eb-c97d-4c61-87ac-280fec559178" \
    --role-definition-name "Cosmos DB Built-in Data Contributor"
`
