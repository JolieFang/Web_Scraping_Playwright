from playwright.sync_api import sync_playwright
from playwright.sync_api import Browser
from flask import Flask, jsonify


app = Flask(__name__)
playwright = sync_playwright().start()
# use headless mode
browser: Browser = playwright.chromium.launch(headless=True)


@app.route("/")
def main():
     # fake the useragent
    myUserAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.38 Safari/537.36"
    context = browser.new_context(user_agent=myUserAgent)
    page = context.new_page()

    js = """Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});"""
    page.add_init_script(js)

    page.goto(
        "your scraped website here",
        wait_until="networkidle",
    )

    page.set_default_timeout(600000)

    page.expect_response(
        lambda response: "your scraped website here"
        in response.url
        and response.status == 200
    )
    all_items = page.query_selector_all(".data you need here")
    if all_items:
        first_item = all_items[0].text_content()
        return jsonify({"monthly visits is ": first_item})
    else:
        return jsonify({"error": "No items found"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, threaded=False)
