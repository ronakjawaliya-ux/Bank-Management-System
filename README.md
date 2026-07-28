# 🏦 Bank Management System (Python)

A simple **Bank Management System** built using **Python** that allows users to perform essential banking operations through a command-line interface (CLI). Account data is stored permanently using **JSON**, ensuring information is preserved even after the program is closed.

---

## 📌 Features

### 👤 Account Management

- ✅ Create a New Bank Account
- ✅ View All Accounts
- ✅ Search Account by ID
- ✅ Update Account Details
- ✅ Delete Account
- ✅ Check Account Balance

### 💰 Banking Operations

- ✅ Deposit Money
- ✅ Withdraw Money
- ✅ Transfer Money Between Accounts
- ✅ View Total Bank Statistics

### 💾 Data Management

- ✅ Automatic Data Saving using JSON
- ✅ Automatic Data Loading on Startup

### 🛡️ Validation & Error Handling

- ✅ Input Validation using `try-except`
- ✅ Prevent Duplicate Account IDs
- ✅ Positive Account ID Validation
- ✅ Age Validation
- ✅ Phone Number Validation
- ✅ Balance Validation
- ✅ Invalid Transaction Handling
- ✅ File Handling Error Management

---

## 🛠️ Technologies Used

- Python 3
- JSON (Data Storage)

---

## 📂 Project Structure

```text
Bank-Management-System-Python/
│
├── main.py              # Main application
├── accounts.json        # Stores account data
├── README.md            # Project documentation
└── FEATURES.md          # Project features
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ronakjawaliya-ux/Bank-Management-System-Python.git
```

### 2. Open the project folder

```bash
cd Bank-Management-System-Python
```

### 3. Run the application

```bash
python main.py
```

---

## 📋 Menu Options

```text
===== Bank Management System =====

1. Create Account
2. View All Accounts
3. Search Account
4. Update Account
5. Deposit Money
6. Withdraw Money
7. Transfer Money
8. Check Balance
9. Delete Account
10. Total Accounts
11. Exit
```

---

## 💡 Features Explained

### 🆕 Create Account

- Creates a new bank account.
- Prevents duplicate Account IDs.
- Validates:
  - Account ID
  - Name
  - Age
  - Phone Number
  - Initial Balance

### 📋 View All Accounts

- Displays all registered accounts.
- Shows:
  - Account ID
  - Name
  - Age
  - Phone Number
  - Balance

### 🔍 Search Account

- Search an account using Account ID.
- Displays complete customer details.

### ✏️ Update Account

- Update customer information.
- Editable fields:
  - Name
  - Age
  - Phone Number
- Balance remains protected and can only be changed through banking transactions.

### 💰 Deposit Money

- Deposit money into an existing account.
- Automatically updates account balance.
- Saves changes to JSON.

### 💸 Withdraw Money

- Withdraw money from an account.
- Prevents:
  - Negative withdrawals
  - Insufficient balance

### 🔄 Transfer Money

- Transfer money between two accounts.
- Prevents transfers to the same account.
- Verifies both accounts exist.
- Checks sufficient sender balance.
- Automatically updates both balances.

### 💳 Check Balance

- View the current balance of an account.
- Displays account holder information.

### 🗑️ Delete Account

- Delete an existing account.
- Includes confirmation before deletion.

### 📊 Total Accounts

Displays:

- Total number of bank accounts
- Total money stored in the bank

---

## ⚠️ Input Validation

The application validates:

- Positive Account IDs
- Duplicate Account IDs
- Customer Name
- Age (1–120)
- 10-digit Phone Number
- Initial Balance
- Deposit Amount
- Withdrawal Amount
- Transfer Amount

The application prevents:

- Invalid numeric inputs
- Empty names
- Negative balances
- Invalid transactions
- Transfers to the same account
- Operations on non-existing accounts

---

## 📷 Sample Output

```text
========== Transfer Successful ==========

Transferred Amount : ₹500.00
From Account       : 101
To Account         : 102
Sender Balance     : ₹4500.00
Receiver Balance   : ₹2500.00

=========================================
```

---

## 📄 Sample JSON

```json
[
    {
        "id": 101,
        "name": "Ronak",
        "age": 22,
        "phone_no": "9876543210",
        "balance": 5000.0
    },
    {
        "id": 102,
        "name": "Aman",
        "age": 23,
        "phone_no": "9123456780",
        "balance": 3500.0
    }
]
```

---

## 🎯 Future Improvements

- 🔐 PIN Authentication
- 📜 Transaction History
- 📄 Mini Bank Statement
- 📅 Date & Time for Transactions
- 💳 Auto-generated Account Numbers
- 📈 Interest Calculation
- 🖥️ Graphical User Interface (Tkinter)
- 🗄️ SQLite/MySQL Database Integration
- 🌐 Flask Web Application

---

## 📚 What I Learned

This project helped me strengthen my understanding of:

- Python Fundamentals
- Functions
- Loops & Conditional Statements
- Lists & Dictionaries
- JSON File Handling
- Exception Handling (`try-except`)
- CRUD Operations
- Input Validation
- Banking Logic
- Problem Solving

---

## 👨‍💻 Author

**Ronak Jawalia**

- B.Tech CSE (AI & ML)
- Python Developer
- Learning Data Structures & Algorithms
- Building projects to strengthen programming skills

### GitHub

- **Profile:** https://github.com/ronakjawaliya-ux
- **Repository:** https://github.com/ronakjawaliya-ux/Bank-Management-System-Python

---

## ⭐ Support

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub. It motivates me to keep learning, improve my skills, and build more exciting projects.