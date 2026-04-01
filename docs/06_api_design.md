# API Design

## 1. Authentication APIs

### 1.1 Register User

**POST /auth/register**

Request:

```json
{
  "name": "Anushka",
  "email": "anushka@example.com",
  "password": "securepassword"
}
```

Response:

```json
{
  "message": "User registered successfully"
}
```

---

### 1.2 Login User

**POST /auth/login**

Request:

```json
{
  "email": "anushka@example.com",
  "password": "securepassword"
}
```

Response:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

## 2. Document APIs

### 2.1 Upload Document

**POST /documents/upload**

Request:

* Form-data:

  * file
  * document_type

Response:

```json
{
  "document_id": 1,
  "message": "Document uploaded successfully"
}
```

---

### 2.2 Get Document

**GET /documents/{id}**

Response:

```json
{
  "id": 1,
  "document_type": "income_certificate",
  "extracted_data": {
    "income": 180000
  }
}
```

---

## 3. Eligibility APIs

### 3.1 Check Eligibility

**POST /eligibility/check**

Request:

```json
{
  "user_id": 1
}
```

Response:

```json
{
  "eligible_schemes": [
    {
      "scheme_name": "Scholarship A",
      "status": "eligible"
    }
  ],
  "ineligible_schemes": [
    {
      "scheme_name": "Loan B",
      "reason": "Income too high"
    }
  ]
}
```

---

### 3.2 Get Results

**GET /eligibility/results/{user_id}**

Response:

```json
{
  "results": [
    {
      "scheme": "Scholarship A",
      "status": "eligible"
    }
  ]
}
```

---

## 4. Scheme APIs

### 4.1 Get All Schemes

**GET /schemes**

Response:

```json
[
  {
    "id": 1,
    "name": "Scholarship A",
    "category": "Education"
  }
]
```

---

### 4.2 Get Scheme Details

**GET /schemes/{id}**

Response:

```json
{
  "name": "Scholarship A",
  "description": "Details about scheme",
  "rules": [
    {
      "field": "income",
      "operator": "<",
      "value": 200000
    }
  ]
}
```

---

## 5. Design Decisions

* RESTful API design
* JSON-based communication
* JWT authentication for security
* Clear separation of endpoints

---

## 6. Future Enhancements

* Add pagination for large datasets
* Add filtering for schemes
* Add chatbot endpoint (/chat/query)
