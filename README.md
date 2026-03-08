# 🔍 SQL Query Generator

**Natural Language to SQL with IBM Granite 3.3 2B**

SQL Query Generator is an intelligent database query assistant that leverages the IBM Granite 3.3 2B Instruct model to convert natural language requests into safe, production-ready SQLite SQL queries. Built with a focus on accessibility and security, this platform allows users to extract insights from data without requiring prior SQL knowledge.

## 🌟 Key Features

* **AI-Powered Translation:** Analyzes user requests in plain English to intelligently infer database tables, columns, and temporal conditions.
* **Robust Security:** Features comprehensive safety validation that blocks dangerous SQL keywords (like `DROP` and `DELETE`) and prevents SQL injection attempts.
* **Conversational Interface:** Provides a modern, user-friendly chat interface powered by Gradio.
* **Extensive Export Options:** Supports exporting query history into professionally formatted PDF reports via ReportLab, plain text files, and ready-to-use social media share links (WhatsApp/Facebook).

---

## 📁 Repository Structure

Based on the project files, here is what each file does:

* **`!pip install.py`**
  Contains the environment setup commands. It installs all required dependencies (Gradio, Transformers, PyTorch, ReportLab, etc.) needed to run the AI model and the web interface in a Google Colab environment.
* **`Basic AI Model Testing.py`**
  A lightweight testing script that uses the Hugging Face `pipeline` helper to quickly verify that the IBM Granite model is downloading and responding correctly.
* **`Advanced AI Model Configuration.py`**
  A more granular setup script that loads the model directly using `AutoTokenizer` and `AutoModelForCausalLM`. This file is used for fine-tuning generation parameters (like token limits) and testing deeper model interactions.
* **`SQL_Generator.py`**
  **The main application file.** This contains the core logic, including the database schema definitions, security validators, condition extraction regex, PDF/Text export handlers, and the complete Gradio web interface.
* **`SQL Query Generator _n.docx`**
  The original project documentation, outlining the architecture, scenarios, and database schema.

---

## 🚀 How to Run the Project

This project is optimized to run in **Google Colab** to take advantage of cloud GPUs for the AI model.

### Step 1: Install Dependencies
Open a new Google Colab notebook and run the contents of `!pip install.py` in the first cell:
```python
!pip install -q gradio transformers torch black autopep8 reportlab requests
