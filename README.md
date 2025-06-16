````markdown
# 🗂️ MySQL CSV Ingestion Pipeline with Python

This project automates the process of ingesting `.csv` files into a MySQL database using Python, Pandas, and SQLAlchemy — complete with logging, column name cleaning, and table validation.

---

## 🚀 Features

- 🔄 Auto-detects all `.csv` files in the current directory
- 🛠️ Creates and resets the MySQL database (`project1`)
-  Cleans column names to remove unwanted whitespace
- 📥 Ingests each CSV into MySQL as a separate table
-  Logs every step in `logs/Project1.log`
-  Displays all created tables at the end
- ⏱️ Tracks total ingestion runtime in minutes

---

## 📦 Tech Stack

- Python 3.x
- Pandas
- SQLAlchemy
- PyMySQL
- MySQL
- Logging module

---

## 🧠 Use Case

Ideal for:
- Students learning data pipelines
- Data engineers testing ingestion scripts
- Automating CSV-to-SQL ETL jobs
- Bootstrapping projects with bulk dataset loads

---

## 🛠️ Setup Instructions

1. **Ensure MySQL is running locally.**
2. **Update your MySQL credentials** in the script if needed:
   ```python
   'mysql+pymysql://root:your_password@localhost/data_set'
````

3. Place all your `.csv` files in the project directory.
4. Run the script:

   ```bash
   python ingest.py
   ```

---

## 📁 Folder Structure

```
📦project-folder/
 ┣ 📄 ingest.py
 ┣ 📁 logs/
 ┃ ┗ 📄 Project1.log
 ┣ 📄 *.csv (your data files)
```

---

## ✅ Example CSV to SQL Flow

```
life_expectancy.csv     →     life_expectancy (MySQL table)
lungcapdata.csv         →     lungcapdata (MySQL table)
```

---

## 🧾 Output Example

```
('life_expectancy',)
('lungcapdata',)
```

