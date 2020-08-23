import pytest
from selenium import webdriver


def test_check_add_to_market_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert True
