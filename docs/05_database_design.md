# Database Design (PostgreSQL)

## 1. Overview

The system uses PostgreSQL as the primary database to store structured user data, documents, schemes, and eligibility rules.

PostgreSQL is chosen for its reliability, strong relational integrity, and support for advanced data types like JSONB.

---

## 2. Tables

### 2.1 Users

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 2.2 Documents

```sql
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    document_type TEXT,
    file_url TEXT,
    extracted_data JSONB,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

👉 `JSONB` is used to store flexible extracted data (e.g., income, DOB)

---

### 2.3 Schemes

```sql
CREATE TABLE schemes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT
);
```

---

### 2.4 Eligibility Rules

```sql
CREATE TABLE eligibility_rules (
    id SERIAL PRIMARY KEY,
    scheme_id INT REFERENCES schemes(id),
    field_name TEXT,
    operator TEXT,
    value TEXT
);
```

---

### 2.5 Eligibility Results

```sql
CREATE TABLE eligibility_results (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    scheme_id INT REFERENCES schemes(id),
    status TEXT,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 3. Relationships

* One user → many documents
* One scheme → many rules
* One user → many eligibility results

---

## 4. Design Decisions

### 4.1 Use of JSONB

* Flexible schema for OCR-extracted data
* Avoids frequent schema changes

### 4.2 Normalization

* Separate tables for rules and schemes
* Reduces redundancy

### 4.3 Extensibility

* New schemes can be added without changing logic
* Rules are dynamic and stored in DB

---

## 5. Indexing (Future Optimization)

* Index on `user_id` in documents
* Index on `scheme_id` in eligibility_rules
* Index on `email` in users

---

## 6. Future Improvements

* Add audit logs
* Add versioning for scheme rules
* Use partitioning for large datasets
