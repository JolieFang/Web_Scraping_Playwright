from playwright.sync_api import sync_playwright
from playwright.sync_api import Browser
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def main():
    with sync_playwright() as p:
        # use headless mode
        browser: Browser = p.chromium.launch(headless=True)
        # fake the useragent 
        myUserAgent = "Chrome/110.0.5481.38"
        context = browser.new_context(user_agent=myUserAgent)
        page = context.new_page()

        js = """Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});"""
        page.add_init_script(js)

        page.goto(
            "your scraped website here",
            wait_until="networkidle",
        )
        # set the timeout 
        page.wait_for_timeout(60000)

        page.expect_response(
            lambda response: "your scraped website here"
            in response.url
            and response.status == 200
        )
        all_items = page.query_selector_all("data you need here")

        for el in all_items:
            text = el.text_content()
            return jsonify({"message": text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
