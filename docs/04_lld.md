# Low-Level Design (LLD)

## 1. Backend Structure

```text
backend/
 ├── app/
 │   ├── main.py
 │   ├── api/
 │   │     ├── routes/
 │   │     │     ├── auth.py
 │   │     │     ├── documents.py
 │   │     │     ├── schemes.py
 │   │     │     ├── eligibility.py
 │   │
 │   ├── services/
 │   │     ├── ocr_service.py
 │   │     ├── nlp_parser.py
 │   │     ├── eligibility_engine.py
 │   │     ├── cache_service.py
 │   │
 │   ├── models/
 │   │     ├── user.py
 │   │     ├── document.py
 │   │     ├── scheme.py
 │   │     ├── eligibility_rule.py
 │   │
 │   ├── db/
 │   │     ├── session.py
 │   │     ├── base.py
```

---

## 2. Module Breakdown

### 2.1 API Layer

* Handles HTTP requests
* Validates input
* Calls appropriate services

### 2.2 Service Layer

* Contains business logic
* Independent and reusable

### 2.3 Data Layer

* Handles database operations
* Uses ORM (SQLAlchemy)

---

## 3. Core Services

### 3.1 OCR Service

* Accepts document input
* Extracts raw text using OCR

### 3.2 NLP Parser

* Cleans extracted text
* Converts into structured key-value pairs

### 3.3 Eligibility Engine

* Takes structured user data
* Applies rules from database
* Returns eligibility result

### 3.4 Cache Service (Redis)

* Stores eligibility results
* Improves performance

---

## 4. Detailed Data Flow

1. User uploads document
2. API receives file
3. File stored temporarily
4. OCR service extracts text
5. NLP parser processes text
6. Structured data saved in DB
7. Eligibility engine runs rules
8. Results cached in Redis
9. Response returned

---

## 5. Eligibility Engine Logic (Example)

```python
def check_eligibility(user_data, rules):
    for rule in rules:
        field = rule["field"]
        operator = rule["operator"]
        value = rule["value"]

        if operator == "<" and not user_data[field] < value:
            return False
        if operator == ">" and not user_data[field] > value:
            return False
        if operator == "==" and not user_data[field] == value:
            return False

    return True
```

---

## 6. Design Decisions

* Modular services for scalability
* Separation of concerns (API, services, DB)
* Redis caching for performance optimization
* Rule-based engine for flexibility in scheme updates
