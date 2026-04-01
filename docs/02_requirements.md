# Requirements Document

## 1. Functional Requirements

### 1.1 User Management

* Users should be able to register and log in securely
* Users should be able to view and manage their profile

### 1.2 Document Upload & Processing

* Users should be able to upload documents (Aadhar, income certificate, etc.)
* The system should store uploaded documents securely
* The system should extract relevant information using OCR

### 1.3 Data Extraction & Parsing

* The system should parse extracted text into structured data
* The system should handle noisy or incomplete OCR outputs

### 1.4 Eligibility Detection

* The system should evaluate user data against scheme eligibility rules
* The system should return a list of eligible schemes
* The system should provide reasons for ineligibility

### 1.5 Missing Document Detection

* The system should identify missing required documents
* The system should guide users on required documents

### 1.6 Scheme Management

* The system should store and manage government scheme data
* Admins should be able to add/update scheme rules (optional future feature)

---

## 2. Non-Functional Requirements

### 2.1 Performance

* Eligibility results should be generated within 2–3 seconds
* OCR processing should be handled efficiently

### 2.2 Scalability

* The system should support multiple concurrent users
* Services should be designed for horizontal scaling

### 2.3 Security

* User data and documents must be securely stored
* Authentication should use JWT-based mechanisms
* File uploads must be validated

### 2.4 Reliability

* The system should handle failures in OCR or parsing gracefully
* Data consistency must be maintained

### 2.5 Usability

* The UI should be simple and user-friendly
* The system should support users with minimal technical knowledge

---

## 3. User Stories

### 👤 User

* As a user, I want to upload my documents so that I don’t have to manually enter data
* As a user, I want to know which schemes I am eligible for
* As a user, I want to understand why I am not eligible for certain schemes
* As a user, I want to know which documents are missing

### 🛠️ Admin (Future Scope)

* As an admin, I want to add or update scheme rules
* As an admin, I want to manage scheme data efficiently
