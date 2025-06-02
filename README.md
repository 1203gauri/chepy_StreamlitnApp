 Chepy Streamlit App

An interactive web app built using [Streamlit](https://streamlit.io/) that harnesses the powerful capabilities of the [Chepy](https://github.com/securisec/chepy) Python library. This app provides a simple and user-friendly interface for developers, cybersecurity professionals, and data analysts to perform various text, binary, file, network, and data transformation operations.

---

 What is Chepy?

**Chepy** is a versatile and powerful Swiss army knife for developers and security professionals. It provides a wide range of operations for:

- Text manipulation (case conversion, encoding, hashing)
- Binary and hex transformations
- Network requests (GET/POST)
- File parsing and analysis
- JSON beautification and transformation

Chepy allows for chaining multiple operations programmatically, but in this Streamlit app, we've adapted its key features for a graphical interface that requires no coding experience.

> 🔗 Learn more about Chepy here: [Chepy GitHub Repository](https://github.com/securisec/chepy)

---
Features

 Text Operations
- Convert to **Upper Case** / **Lower Case**
- **Base64 Encoding**
- **Text Reversal**
- **URL Encoding**
- **SHA-256 Hashing**

###  Binary Operations
- Convert **Hex to Binary** and **Binary to Hex**
- Encode and decode **Base64**

###  File Operations
- Upload any file and view its content in **hexadecimal**
- Generate **MD5 Hash** of the file

###  Network Operations
- Perform **HTTP GET** requests to a given URL
- **Download** response content as a text file

###  Data Transformation
- Input raw **JSON** and instantly **beautify** it for better readability

---

 Requirements

Install dependencies via pip:

```bash
pip install streamlit chepy
