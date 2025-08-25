# 🚀 SupplySphere Backend

## 📌 Overview

The **SupplySphere Backend** powers the blockchain-enabled supply chain traceability platform.
It handles authentication, role-based access, product/inventory management, shipment tracking, AI-assisted queries, and integrates with blockchain for verifiable logs.

This backend is designed to be:

* **Scalable** — supports multi-tenant supply chains.
* **Secure** — JWT authentication, RBAC, optional 2FA.
* **Interoperable** — REST APIs ready for frontend & third-party integration.
* **Extensible** — modular Flask services, pluggable blockchain layer.

---

## 🛠️ Tech Stack

* **Framework**: [Flask](https://flask.palletsprojects.com/) (Python lightweight backend)
* **Database**: PostgreSQL (production-ready, relational consistency)
* **Blockchain Layer**: ICP Canister / Smart contract (traceability logs)
* **Authentication**: JWT, Role-Based Access Control (RBAC), optional 2FA
* **AI Assistant**: OpenAI API / Gemini (for natural language queries)
* **Deployment**: Docker + Render / Railway / ICP
* **Testing**: Pytest

---

## 🔑 Core Features (Backend Services)

* ✅ **Authentication & Authorization** (JWT, RBAC, refresh tokens)
* ✅ **User Management** (Suppliers, Vendors, Analysts, Admins)
* ✅ **Products & Inventory** (CRUD, batch tracking, low-stock alerts)
* ✅ **Shipments** (end-to-end tracking, status updates, blockchain proofs)
* ✅ **Blockchain Integration** (ledger of immutable logs for every shipment & product)
* ✅ **AI Query Service** (convert natural language questions into SQL queries & responses)
* ✅ **Analytics API** (KPI exports, CSV/JSON endpoints)

---

## 🏗️ System Architecture

```mermaid
flowchart TD
  A[Frontend - Next.js] -->|REST API Calls| B[Flask Backend]
  B -->|ORM Queries| C[(PostgreSQL DB)]
  B -->|Logs| D[(Blockchain Ledger)]
  B -->|AI Requests| E[AI Assistant API]
```

---

## 🗄️ Database Schema (Simplified ERD)

```mermaid
erDiagram
    USERS {
        int id PK
        string username
        string email
        string password_hash
        string role
    }
    PRODUCTS {
        int id PK
        string name
        string batch_id
        int stock
        date expiry_date
    }
    SHIPMENTS {
        int id PK
        int product_id FK
        string origin
        string destination
        string status
        date shipped_at
    }
    BLOCKCHAIN_LOGS {
        int id PK
        string action
        string reference_id
        date timestamp
        string tx_hash
    }
    USERS ||--o{ PRODUCTS : "manages"
    PRODUCTS ||--o{ SHIPMENTS : "contains"
    SHIPMENTS ||--o{ BLOCKCHAIN_LOGS : "logged in"
```

---

## 📡 API Endpoints

### 🔐 Auth

* `POST /api/auth/register` — create user
* `POST /api/auth/login` — login, return JWT
* `POST /api/auth/refresh` — refresh token

### 👤 Users

* `GET /api/users` — list users (admin only)
* `GET /api/users/:id` — get user details

### 📦 Products & Inventory

* `POST /api/products` — add product
* `GET /api/products` — list products
* `PUT /api/products/:id` — update product
* `DELETE /api/products/:id` — delete product

### 🚚 Shipments

* `POST /api/shipments` — create shipment
* `GET /api/shipments` — list shipments
* `PUT /api/shipments/:id` — update status

### 🔗 Blockchain Logs

* `GET /api/logs` — fetch immutable supply chain logs

### 🤖 AI Queries

* `POST /api/ai/query` — submit natural language query

---

## ⚡ Setup & Installation

### 1. Clone Repo

```bash
git clone https://github.com/your-org/supplysphere-backend.git
cd supplysphere-backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables (`.env`)

```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=postgresql://user:password@localhost/supplysphere
SECRET_KEY=your-secret-key
JWT_SECRET=your-jwt-secret
OPENAI_API_KEY=your-openai-api-key
```

### 5. Run Server

```bash
flask run
```

---

## 🧪 Testing

```bash
pytest --maxfail=1 --disable-warnings -q
```

---

## 📌 Roadmap

* [x] Authentication & User Roles
* [x] Product & Inventory CRUD
* [x] Shipments API
* [ ] Blockchain Integration
* [ ] AI Assistant Service
* [ ] Analytics Dashboard API
* [ ] Deployment (Docker + Render/ICP)

---

## 🤝 Contribution Guidelines

* Fork repo & create feature branch (`feature/your-feature`)
* Use conventional commits (`feat:`, `fix:`, `docs:`)
* Add tests for new features
* Submit PR with description

---

## 📄 License

MIT License — feel free to use and adapt for hackathon & research purposes.
