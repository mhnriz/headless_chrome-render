const puppeteer = require('puppeteer');
const path = require('path')

(async () => {
  // Launch Chrome with the extension loaded
  const browser = await puppeteer.launch({
    headless: false,  // Extensions need non-headless mode
    args: [
      `--disable-extensions-except=${path.resolve('./extension')}`,
      `--load-extension=${path.resolve('./extension')}`,
      '--no-sandbox', 
      '--disable-setuid-sandbox'
    ],
  });

  const page = await browser.newPage();
  await page.goto('https://example.com');  // Test site or any other

  // Interact with the page or extension here

  await browser.close();
})();
