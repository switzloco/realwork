# Scraping Without Bright Data

If you don't want to pay for Bright Data after the hackathon, the pipeline still works — Stage 2 just gets slower and less reliable.

**Free/cheap replacements:**
- **Playwright or Selenium** — handles JS-heavy sites (county portals). You manage your own browser instances. Slower, no proxy rotation, but free.
- **requests + BeautifulSoup** — works fine for simple sites (SoS, CSLB, SAM.gov). Most of the Tier 1 sources don't actually need proxies.
- **ScraperAPI or ScrapingBee** — cheaper pay-as-you-go alternatives if you just need proxy rotation occasionally.
- **SerpAPI** — for the SERP/news search use case specifically. Has a free tier.

**What you lose:** Bright Data's proxy network handles rate limiting, CAPTCHAs, and IP bans automatically. Without it, you'll need to add retry logic, respect rate limits manually, and accept that some hostile sites may block you. For a long-running project doing occasional lookups (not bulk scraping), this is usually fine.

**Migration path:** Abstract the Scraper Coordinator behind a simple interface (`scrape(url, method) → html`). Swap the Bright Data implementation for Playwright later without touching the rest of the pipeline.
