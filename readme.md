# 🏦 Bank Management System (Python)

A simple **Bank Management System** built using **Python** that allows users to perform basic banking operations through a command-line interface (CLI). Account data is stored permanently using **JSON**, so information is preserved even after the program is closed.

---

## 📌 Features

* ✅ Create a New Bank Account
* ✅ View All Accounts
* ✅ Search Account by ID
* ✅ Deposit Money
* ✅ Withdraw Money
* ✅ Transfer Money Between Accounts
* ✅ Automatic Data Saving using JSON
* ✅ Input Validation with `try-except`
* ✅ Balance Validation
* ✅ Error Handling for Invalid Operations

---

## 🛠️ Technologies Used

* Python 3
* JSON (for data storage)

---

## 📂 Project Structure

```text
Bank-Management-System-Python/
│
├── main.py              # Main application
├── accounts.json        # Stores account data
└── README.md            # Project documentation
```

---

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/ronakjawaliya-ux/Bank-Management-System-Python.git
```

2. Open the project folder.

3. Run the program:

```bash
python main.py
```

---

## 📋 Menu Options

```text
===== Bank Management System =====

1. Create Account
2. View Accounts
3. Deposit Money
4. Withdraw Money
5. Search Account
6. Transfer Money
7. Exit
```

---

## 💡 Features Explained

### 🆕 Create Account

* Creates a new bank account.
* Stores account details in a JSON file.

### 💰 Deposit Money

* Adds money to an existing account.
* Validates account ID and amount.

### 💸 Withdraw Money

* Withdraws money if sufficient balance is available.
* Prevents negative balances.

### 🔍 Search Account

* Searches an account using its Account ID.
* Displays account information if found.

### 🔄 Transfer Money

* Transfers money between two accounts.
* Prevents transfers to the same account.
* Checks if both accounts exist.
* Ensures sufficient balance before transferring.
* Saves updated balances automatically.

---

## ⚠️ Input Validation

The application handles several invalid inputs, including:

* Invalid Account IDs
* Invalid transfer amounts
* Negative or zero amounts
* Insufficient balance
* Sender and receiver being the same account
* Non-existent accounts

---

## 📷 Sample Output

```text
========== Transfer Successful ==========

Transferred Amount : ₹500.00
From Account ID    : 101
To Account ID      : 102
Sender Balance     : ₹4500.00
Receiver Balance   : ₹2500.00
```

---

## 🎯 Future Improvements

* 🔐 PIN Authentication
* 📜 Transaction History
* 📄 Mini Bank Statement
* 📅 Date & Time for Transactions
* 💳 Auto-generated Account Numbers
* 📈 Interest Calculation
* 🖥️ Graphical User Interface (Tkinter)
* 🗄️ SQLite/MySQL Database Integration

---

## 📚 What I Learned

This project helped me practice:

* Python Fundamentals
* Functions
* Loops and Conditional Statements
* Dictionaries and Lists
* File Handling
* JSON Data Storage
* Exception Handling (`try-except`)
* Problem Solving
* Building a Complete CLI Application

---

## 👨‍💻 Author

**Ronak Jawalia**

* B.Tech CSE (AI & ML)
* Python Developer
* Learning Data Structures & Algorithms
* Building projects to strengthen programming skills

### GitHub

* **Profile:** https://github.com/ronakjawaliya-ux
* **Repository:** https://github.com/ronakjawaliya-ux/Bank-Management-System-Python

---

## ⭐ Support

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub. It motivates me to keep learning and building more projects!
