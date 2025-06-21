import asyncio
from pyppeteer import launch

# Path to the Chromium executable
chromium_executable_path = 'D:/2_ZAGRUZKA/channel_analyzis/chromedriver-win64'

# Function to scrape Telegram channel posts
async def scrape_telegram_channel():
    # Launch the browser with the custom Chromium path
    browser = await launch(headless=True, executablePath=chromium_executable_path)

    # Create a new page
    page = await browser.newPage()

    # Navigate to the Telegram channel's page
    await page.goto('https://t.me/s/alwaysinomniaparatus', {'waitUntil': 'networkidle2'})

    # Wait for the element containing the messages to appear
    await page.waitForSelector('.tgme_widget_message_wrap')

    # Extract the posts' content using JavaScript
    messages = await page.evaluate('''() => {
        let message_elements = document.querySelectorAll('.tgme_widget_message_text');
        let messages = [];
        message_elements.forEach((message_element) => {
            messages.push(message_element.innerText);  # Get the inner text of each post
        });
        return messages;
    }''')

    # Print each message found
    print("Messages from the channel:")
    for i, message in enumerate(messages, 1):
        print(f"{i}: {message}")

    # Close the browser
    await browser.close()

# Main function that runs the Pyppeteer script
def main():
    # Run the async function for scraping
    asyncio.get_event_loop().run_until_complete(scrape_telegram_channel())

if __name__ == "__main__":
    main()
