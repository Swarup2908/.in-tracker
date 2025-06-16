# (.in) Domain Registration Tracker 📈

This project automatically scrapes, parses, and records the monthly count of newly registered **`.in` domains** from [registry.in](https://www.registry.in/domain-archives).  
It downloads official monthly PDF reports, extracts the count, and appends it to a CSV file. The task is automated using **Celery + Redis**, scheduled to run **on the 3rd of every month**.

---

## 📦 Features

- 🔗 Scrapes PDF reports from registry.in
- 📄 Parses `.pdf` files using `pdfplumber`
- 📊 Appends clean data to `domain_data.csv`
- 🧠 Avoids duplicate entries intelligently
- ⏰ Automated monthly execution using Celery

---

## 🗂 Project Structure

```
.
├── scraper.py          # PDF link scraper
├── parser.py           # PDF content parser
├── main.py             # Manual run trigger (optional)
├── tasks.py            # Celery task logic
├── celeryconfig.py     # Celery Beat scheduler config
├── domain_data.csv     # Output data file
├── reports/            # Folder with downloaded PDFs
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## 📥 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/in-domain-tracker.git
cd in-domain-tracker
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 🔹 Manually (Optional)

You can test the scraper and parser manually:

```bash
python main.py
```

### 🔹 Automatically with Celery

1. **Make sure Redis server is running**
   (Install via `sudo apt install redis` or follow official docs)

2. **Start the Celery Worker:**
   ```bash
   celery -A tasks worker --loglevel=info
   ```

3. **Start the Celery Beat Scheduler:**
   ```bash
   celery -A tasks beat --loglevel=info
   ```

---

## 🧪 Dependencies

Your `requirements.txt` contains:

```txt
requests
beautifulsoup4
pdfplumber
celery
redis
```

These libraries are responsible for:
- **requests** – Making HTTP requests to fetch pages
- **beautifulsoup4** – Parsing HTML to extract PDF links
- **pdfplumber** – Reading and extracting text from PDF reports
- **celery** – Running asynchronous tasks
- **redis** – Celery's backend broker for task scheduling

---

## 📊 Output

All parsed data is saved in `domain_data.csv` as:

```csv
Month,New Domains
June 2024,23112
May 2024,21753
...
```

---

## 📅 Automation Schedule

This project is configured to automatically update on the **3rd of every month**.
You can modify the schedule in `celeryconfig.py` if needed.

---
