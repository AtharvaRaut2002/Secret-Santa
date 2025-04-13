# 🎁 Secret Santa Assignment System

A Python-based automated Secret Santa assignment system designed for **Acme Inc.** to efficiently assign secret children to employees while avoiding self-assignments and last year's matches. Built with modular design, robust error handling, logging, and test support.

---

## 📄 Documentation

This project aims to provide a modular and extensible solution for organizing a Secret Santa event based on employee data. This README serves as the **comprehensive documentation** for understanding, installing, running, and extending the system.

---

## ✅ Features

- ✅ Prevents self-assignments
- ✅ Avoids repeat matches from last year
- ✅ Each employee gets one unique secret child
- ✅ Modular OOP structure
- ✅ Reads Excel input files
- ✅ Outputs to CSV
- ✅ Logs processing info and errors
- ✅ Includes unit tests

---

## 🛠️ Installation Instructions

### Prerequisites

- Python 3.13+
- pip

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/secret-santa.git
   cd secret-santa

2. **Create a virtual environment (optional but recommended):**
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

4. **🚀 How to Run**
    
    ```bash
    python src/main.py

5. **How to test**

    ```bash
    python -m unittest tests.test_assignment
