# test_my_application.py
def test_example_is_working(page):
    page.goto("https://example.com")
    assert page.inner_text('h1') == 'Example Dmkkomain'
    page.wait_for_timeout(3000)
    page.click("text=More information")