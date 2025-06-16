from celery import Celery
from scraper import get_pdf_links

app = Celery('tasks', broker='redis://localhost:6379/0')
app.config_from_object('celeryconfig')

@app.task
def run_domain_scraper():
    pdf_links = get_pdf_links()
    
    with open("latest_pdf_links.txt", "w") as f:
        for link in pdf_links:
            f.write(link + "\n")
    
    print(f"✅ {len(pdf_links)} domain PDFs saved to latest_pdf_links.txt")
