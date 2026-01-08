 🔐 Random Password Generator (CLI – Python)

## 📌 Project Description
This project is a beginner-friendly Python command-line application that generates random and secure passwords based on user-defined criteria such as password length and character types (letters, numbers, and symbols).

---

## 🎯 Objectives
- To generate secure random passwords
- To allow users to choose password length
- To allow users to select character types
- To understand randomization and input validation in Python

---

## 🛠 Technologies Used
- Python
- random module
- string module

---

## 🔄 Process (How the Project Works)

### Step 1: Import Required Modules
- The `random` module is used to generate random characters.
- The `string` module provides predefined character sets such as letters, digits, and symbols.

---

### Step 2: Take User Input
- The user enters the desired password length.
- The user selects whether to include:
  - Letters
  - Numbers
  - Symbols

---

### Step 3: Validate User Input
- Checks if password length is greater than zero.
- Ensures at least one character type is selected.

---

### Step 4: Character Set Handling
- Based on user choices, selected character sets are combined into a single string.

---

### Step 5: Password Generation
- A random password is generated using `random.choice()` based on the selected length.

---

### Step 6: Display Output
- The generated password is displayed on the terminal.

---

## ▶️ How to Execute the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/sravanthi0605/random-password-generator.git
# Paasword-Generator
