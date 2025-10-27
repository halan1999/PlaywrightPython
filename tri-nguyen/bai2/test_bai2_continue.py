from playwright.sync_api import Page, expect, Playwright
import re, time

def test_check_locator(page: Page):
    #lấy text dashboard
    page.locator("//span[contains(text(), 'Dashboard')]")
    #lấy customer
    page.locator("//aside[@id='menu']/descendant::span[contains(text(),'Dashboard')]")
    # lấy Sales
    page.locator("//li[@class='menu-item-sales']/descendant::span")
    # lấy Subcriptions
    page.locator("//li[@class='menu-item-subscriptions']/descendant::span")
    # lấy Expense
    page.locator("//li[@class='menu-item-expenses']/descendant::span")
    # lấy Contracts
    page.locator("//li[@class='menu-item-contracts']/descendant::span")
    # lấy project
    page.locator("//li[@class='menu-item-projects']/descendant::span")
    # lấy Tasks
    page.locator("//li[@class='menu-item-tasks']/descendant::span")
    # lấy Support
    page.locator("//li[@class='menu-item-support']/descendant::span")
    # lấy leads
    page.locator("//li[@class='menu-item-leads']/descendant::span")
    # lấy estimate request
    page.locator("//li[@class='menu-item-estimate_request']/descendant::span")
    # lấy knowledge base
    page.locator("//li[@class='menu-item-knowledge-base']/descendant::span")
    # lấy utilities
    page.locator("//li[@class='menu-item-utilities']/descendant::span")
    # lấy reports
    page.locator("//li[@class='menu-item-reports']/descendant::span[contains(text(),'Reports')]")
    # lấy icon section Invoices Awaiting Payment, Converted Leads, Projects In Progress, Tasks Not Finished 
    page.locator("//div[@id='widget-top_stats']/div[contains(@class, 'widget-dragger')]")
    # lấy text Invoices Awaiting Payment
    page.locator("//span[contains(text(),'Invoices Awaiting Payment')]")
    # lấy icon Invoices Awaiting Payment
    page.locator("//span[contains(normalize-space(),'Invoices Awaiting Payment')]/preceding-sibling::*[name()='svg']/*[name()='path']")
    # lấy số 1 / 3
    page.locator("//div[@class='top_stats_wrapper']//span[normalize-space()='1 / 3']")
    # lấy icon Converted Leads
    page.locator()
    # lấy text Projects In Progress
    page.locator("//span[contains(text(),'Projects In Progress')]")
    # lấy icon Projects In Progress
    page.locator("//span[contains(normalize-space(),'Projects In Progress')]/preceding-sibling::*[name()='svg']/*[name()='path']")

