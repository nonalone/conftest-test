def test_url_page_have_button_add(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.find_element_by_css_selector('[type="submit"]')
