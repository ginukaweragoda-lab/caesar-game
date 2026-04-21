# 🔐 Caesar Cipher Program

A command-line Python application that encrypts and decrypts text using the classic **Caesar Cipher** technique.

---

## 📌 Features

- Encrypt or decrypt messages via the console or from a `.txt` file
- Supports custom shift values (0–25)
- Handles non-alphabetic characters (spaces, punctuation, numbers) gracefully — they pass through unchanged
- Writes batch file results to `results.txt`
- Input validation for mode, location, shift, and filename

---

## 🚀 How to Run

Make sure you have **Python 3** installed.

```bash
python caesar.py
```

---

## 🧭 Usage Guide

When you run the program, you'll be guided through the following steps:

1. **Choose mode** — encrypt (`e`) or decrypt (`d`)
2. **Choose input source** — console (`c`) or file (`f`)
3. **Enter your message** (if console) or **provide a filename** (if file)
4. **Enter a shift number** between 0 and 25
5. View your result or find it in `results.txt`
6. Choose to process another message or exit

---

## 📂 File Structure

```
caesar-cipher/
│
├── caesar.py        # Main program
├── messages.txt     # Sample input file
├── results.txt      # Output from file encryption/decryption
└── README.md
```

---

## 💡 Example

**Encrypting via console:**
```
Would you like to encrypt (e) or decrypt (d): e
Would you like to read from a file (f) or the console (c)? c
What message would you like to encrypt?: Hello World
What is the shift number: 4
Result: LIPPS ASVPH
```

**Decrypting from file** (`messages.txt` → `results.txt`) with shift `4`:

| Input         | Output        |
|---------------|---------------|
| HELLO         | LIPPS         |
| HELLO WORLD   | LIPPS ASVPH   |
| WHAT!?        | ALEX!?        |
| S O S         | W S W         |
| THE QUICK BROWN FOX... | XLI UYMGO FVSAR... |

---

## 🔧 How It Works

The Caesar Cipher shifts each letter in the alphabet by a fixed number of positions.

- `encrypt(message, shift)` — shifts each letter forward
- `decrypt(message, shift)` — shifts each letter backward
- Non-letter characters are left unchanged

```
A → E  (shift of 4)
H → L
Z → D  (wraps around)
```

---

## 📋 Requirements

- Python 3.x
- No external libraries needed

---

## 👤 Author

**Ginuka Weragoda** — Student No: 2406982  
*Coursework Assessment 1*
