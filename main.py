import os
from scraper import get_pdf_links
from downloader import download_pdf
from parser import extract_domain_count
from writer import write_to_csv, read_existing_data
from utils import get_month_year_from_filename

def main():
    print("🔍 Retrieving PDF links...")
    links = get_pdf_links()
    print(f"Found {len(links)} PDF links.")

    existing = {r['month_year'] for r in read_existing_data()}
    print(f"Already processed: {existing}" if existing else "No previous data found.")

    new_entries = 0

    for url in links:
        month_year = get_month_year_from_filename(url)
        print(f"\n🌐 Checking URL: {url}")
        print(f"➡️ Month-Year derived: {month_year}")

        if month_year in existing:
            print(f"✅ Skipping (already in CSV): {month_year}")
            continue

        pdf_path = download_pdf(url)
        if not pdf_path or not os.path.exists(pdf_path):
            print(f"❌ No PDF downloaded for {url}")
            continue
        print(f"🗂 Downloaded file: {pdf_path}")

        try:
            count = extract_domain_count(pdf_path)
            print(f"🔢 Extracted count: {count}")
        except Exception as e:
            print(f"❗ Parser error for {pdf_path}: {e}")
            continue

        if count and count > 0:
            write_to_csv(month_year, count)
            print(f"✅ Recorded: {month_year} — {count} domains")
            new_entries += 1
        else:
            print(f"⚠️ No valid `.in` domain count found for {month_year}")

    if new_entries == 0:
        print("\n❌ No new valid `.in` domain data found in any PDFs.")
    else:
        print(f"\n✅ Total new entries recorded: {new_entries}")

    # Final Summary
    data = read_existing_data()
    total = sum(int(x['count']) for x in data) if data else 0
    print(f"\n📊 Total months recorded: {len(data)}")
    print(f"📊 Total .in domains so far: {total}")

if __name__ == "__main__":
    main()
