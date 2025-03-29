# TDS Solver - Tools in Data Science (IIT Madras)

## Project Overview
The **TDS Solver** is a FastAPI-based application designed to answer questions from five graded assignments in the *Tools in Data Science* course offered by **IIT Madras Online Degree in Data Science**. It reads pre-processed answers from JSON files and serves responses via API endpoints.

## Project Structure
```
.
├── LICENSE
├── README.md
├── api
│   ├── __init__.py
│   └── main.py
├── assignments
│   ├── assignment1.json
│   ├── assignment2.json
│   ├── assignment3.json
│   ├── assignment4.json
│   └── assignment5.json
├── requirements.txt
└── venv
    └── bin
```

## Installation

### Prerequisites
- Python 3.10 or higher
- `pip` package manager

### Steps to Run Locally
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/tds-solver.git
   cd tds-solver
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate    # On Windows
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**:
   ```bash
   uvicorn api.main:app --reload
   ```

5. **Access the API locally**:
   - API URL: `http://127.0.0.1:8000`

---

## API Endpoints

### Base URL
```
http://127.0.0.1:8000
```

### Endpoint: `/api/`
- **Method:** `POST`
- **Description:** Returns the answer for a given question.
- **Request:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=q-extract-tables-from-pdf"
  ```
- **Response:**
  ```json
  {"answer": "60923"}
  ```

---

## Deployment
- If deployed, the public URL will be shared here.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **IIT Madras Online Degree** — Tools in Data Science Course
- **FastAPI** — Web Framework
- **Uvicorn** — ASGI Server

---

## Contact
For questions or support, contact **[Your Name]** at **[Your Email]**.


