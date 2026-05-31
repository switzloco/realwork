import asyncio
import os
from dotenv import load_dotenv
from playwright.async_api import async_playwright

load_dotenv()

AUTH = os.environ.get("BRIGHT_DATA_BROWSER_AUTH")
SBR_WS_ENDPOINT = f'wss://{AUTH}@brd.superproxy.io:9222'

async def main():
    print("Connecting to Scraping Browser...")
    async with async_playwright() as pw:
        try:
            browser = await pw.chromium.connect_over_cdp(SBR_WS_ENDPOINT)
            context = await browser.new_context()
            page = await context.new_page()
            
            print("Connected! Navigating to CA SOS...")
            resp = await page.goto('https://bizfileonline.sos.ca.gov/search/business', timeout=30000)
            
            print(f"Status: {resp.status}")
            print(f"Title: {await page.title()}")
            content = await page.content()
            print("Snippet:", content[:500])
            
            await browser.close()
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    asyncio.run(main())
