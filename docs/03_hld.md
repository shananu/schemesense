# High-Level Design (HLD)

## 1. System Overview

SchemeSense is a web-based platform that enables users to determine their eligibility for government schemes by analyzing uploaded documents and personal data.

The system follows a modular architecture with separate components for document processing, eligibility evaluation, and data storage.

---

## 2. Architecture Overview

### Components:

* Frontend (React)
* Backend API (FastAPI)
* Document Processing Service (OCR + NLP)
* Eligibility Engine (Rule-based system)
* Database (PostgreSQL)
* Cache Layer (Redis)

---

## 3. System Architecture Diagram

```text
User (Browser)
     ↓
Frontend (React)
     ↓
Backend API (FastAPI)
     ↓
--------------------------------
| Document Processing Service  |
| Eligibility Engine           |
--------------------------------
     ↓
PostgreSQL Database ←→ Redis Cache
```

---

## 4. Component Description

### 4.1 Frontend

* Handles user interaction
* Allows document upload
* Displays eligibility results

### 4.2 Backend API

* Handles incoming requests
* Coordinates between services
* Ensures authentication and validation

### 4.3 Document Processing Service

* Performs OCR on uploaded documents
* Extracts raw text data

### 4.4 NLP Parser

* Converts raw text into structured data
* Handles noisy OCR outputs

### 4.5 Eligibility Engine

* Evaluates structured data against predefined rules
* Determines eligibility status

### 4.6 Database (PostgreSQL)

* Stores user data, documents, and scheme rules

### 4.7 Cache (Redis)

* Stores frequently accessed results
* Reduces database load

---

## 5. Data Flow

1. User uploads a document via frontend
2. Backend receives and stores the document
3. Document Processing Service performs OCR
4. NLP parser extracts structured data
5. Data is stored in PostgreSQL
6. Eligibility engine evaluates rules
7. Results are cached in Redis
8. Response is sent back to the user

---

## 6. Tech Stack Justification

* React: Fast and scalable frontend
* FastAPI: High performance for AI-based workloads
* PostgreSQL: Reliable relational database for structured data
* Redis: Efficient caching and performance optimization
* OCR + NLP: Enables automation of document analysis
