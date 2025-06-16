import pdfplumber

def extract_domain_count(pdf_path):
    count = 0
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    for cell in row:
                        if cell and isinstance(cell, str) and cell.strip().lower() == "in":
                            count += 1
    return count
