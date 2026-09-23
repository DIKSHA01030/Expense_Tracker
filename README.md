# 💰 AI-Powered Expense Tracker

An AI-powered personal finance management web application built with Python and Streamlit. The application allows users to manage income and expenses, upload transaction data, set budgets, track financial trends, receive reminders, and interact with an AI-powered financial assistant.

---

## 📌 Overview

Managing personal finances can become difficult when income, expenses, budgets, and recurring payments are spread across different sources.

This project provides a centralized platform where users can:

- Track income and expenses
- Upload transaction data through CSV files
- Analyze spending and income patterns
- Create category-wise budgets
- Monitor budget utilization
- Set payment and budget reminders
- Visualize financial trends
- Ask an AI assistant for financial insights

The application combines **data processing, visualization, database management, and AI** into a single personal finance platform.

---

## ✨ Features

### 👤 User Authentication

- User registration and login
- Password hashing using SHA-256
- User-specific financial data
- SQLite-based user management

### 💳 Expense & Income Tracking

- Record income and expenses
- Store transactions in SQLite
- Categorize financial transactions
- View and manage transaction records

### 📤 CSV Transaction Upload

Users can upload transaction data through CSV files.

The application uses **Pandas** to:

- Read CSV files
- Validate transaction data
- Process credit and debit transactions
- Convert uploaded data into structured records
- Store processed transactions in the database

### 📊 Financial Reports & Analytics

The application provides financial insights such as:

- Total income
- Total expenses
- Net savings
- Expense breakdown
- Income breakdown
- Spending trends
- Income trends
- Balance trends

Interactive visualizations are created using **Plotly**.

### 💰 Budget Planner

Users can create category-wise budgets and monitor their spending.

The application tracks:

- Allocated budget
- Actual spending
- Remaining budget
- Budget utilization
- Over-budget categories

### 🔔 Reminders

Users can create reminders for:

- Bills
- Budget-related activities
- Payments
- Due dates

The application can display reminders that are due.

### 🤖 ETBot — AI Financial Assistant

The project includes an AI-powered financial assistant called **ETBot**.

ETBot uses the **Cohere API** to provide financial insights based on the user's transaction information.

Users can interact with the assistant to ask questions about their spending and financial activity.

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Web Application
- Streamlit

### Database
- SQLite

### Data Processing
- Pandas

### Data Visualization
- Plotly Express

### AI / LLM
- Cohere API

### Authentication & Security
- Python `hashlib`
- SHA-256 password hashing

### Environment & Configuration
- python-dotenv

### Version Control
- Git
- GitHub

---

## 🏗️ Application Architecture

```text
                   ┌─────────────────────┐
                   │      Streamlit      │
                   │    Web Interface    │
                   └──────────┬──────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
   Authentication       Transactions        Budget & Reminders
          │                   │                   │
          └───────────────────┼───────────────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │     SQLite      │
                     │    Database     │
                     └─────────────────┘
                              │
               ┌──────────────┴──────────────┐
               │                             │
               ▼                             ▼
          Pandas / CSV                  Plotly Charts
               │                             │
               └──────────────┬──────────────┘
                              │
                              ▼
                     Financial Analytics

                              │
                              ▼
                     ┌─────────────────┐
                     │      ETBot      │
                     │   Cohere API    │
                     └─────────────────┘
