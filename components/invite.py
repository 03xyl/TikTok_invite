import time
from datetime import datetime, timedelta

from selenium.webdriver.common.devtools.v85.dom import get_attributes

from components.get_webdriver import driver, wait
from components.split_xlsx_update_files import split_xlsx, update_status

from config.settings import SETTINGS_DATA
from modules.user_operate.user import upload_files, delete_tag

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from modules.user_operate.user_utils import input_or_click_element


# driver.get('https://affiliate-us.tiktok.com/connection/creator-management?shop_region=US')
def _wait(a, b):
    try:
        wait.until(EC.presence_of_element_located((a, b)))
    except Exception as e:
        print(e)


def is_element(_by, css):
    try:
        return driver.find_element(_by, css).click()
    except Exception as e:
        print(e)

def selector_tag():
    driver.get(SETTINGS_DATA.get('my_url'))
    # 点击达人标签
    time.sleep(1)
    input_or_click_element((By.CSS_SELECTOR, 'div.grid.w-full.gap-12.mb-12.grid-cols-3 > div:nth-child(2) > div > div > div'),'click')
    # 默认选最上面的tag
    input_or_click_element((By.CSS_SELECTOR, '#arco-select-popup-0  li:nth-child(3) > span > span'),'click')
    element = driver.find_element(By.CSS_SELECTOR, '[data-e2e="75c1cb63-9d93-c8f6"]')
    return element.text


def run():
    # driver.get(SETTINGS_DATA.get('my_url'))
    # 添加标签
    # selector_tag()
    # batch invite
    input_or_click_element((By.ID, 'crm_batch_invite'),'click')
    # SELECT ALL
    input_or_click_element((By.CSS_SELECTOR, 'table thead .arco-checkbox-mask'),'click')
    #select one
    # time.sleep(1)
    # driver.find_elements(By.CSS_SELECTOR,'table > tbody td.arco-table-td.arco-table-operation.arco-table-checkbox  span.arco-icon-hover.arco-checkbox-icon-hover.arco-checkbox-mask-wrapper > div')[11].click()
    # #second
    # invite to collaborate
    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="20c84e8e-6e2b-893c"]'),'click')

    # #wait four regins
    # wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-e2e="1adf7b37-5743-0a73"]')))
    # #block four regions
    # driver.execute_script("Array.from(document.querySelectorAll('[role=region]')).forEach(item => item.style.display = 'block')")

    # ------------------------------------1.creat invitation------------------------
    # click create invitation

    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="500724e9-9450-8cd5"]'),'click')
    # invitation name

    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="feafd809-5fe4-3adf"]'),'input',input_value='1')

    # valid unit
    # 获取当天的日期
    today = datetime.today().date()
    # 加上30天
    future_date = today + timedelta(days=30)
    # 有效日期格式化后的结果为邀请日期
    invite_date = future_date.strftime("%m/%d/%Y")

    # 自动填写有效期
    _wait(By.CSS_SELECTOR, '[data-tid="m4b_date_picker"] .arco-picker-start-time')
    driver.find_element(By.CSS_SELECTOR, '[data-tid="m4b_date_picker"] .arco-picker-start-time').send_keys(
        '1' + invite_date)
    is_element(By.CSS_SELECTOR, '.arco-picker-cell-selected')

    # email address
    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="4b47def3-3477-eebf"]'),'click')
    # d1.send_keys('ENVIPRO@WOWORLDTECH.COM')
    driver.execute_script("document.querySelector('#target_complete_details_contacts_7_input').value=''")
    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="4b47def3-3477-eebf"]'),'input',input_value='ENVIPRO@WOWORLDTECH.COM')
    # driver.execute_script('document.querySelector("#target_complete_details_contacts_7_input").value = " "')
    # inster
    input_or_click_element((By.ID, 'target_complete_details_message_input'),'click')

    driver.execute_script("document.querySelector('#target_complete_details_message_input').value=''")
    input_or_click_element((By.ID, 'target_complete_details_message_input'),'input',input_value='''
    I hope this message finds you well! I’m David, Product Operations Manager at ENVIPRO, excited to discuss a collaboration to promote our star product—Supracalm Raspberry Lemonade Drink.
    About the Product:
    Supracalm combines L-Theanine, KSM-66 Ashwagandha, Magnesium Glycinate, and Vitamin D3 to improve sleep quality and enhance mental health.
    Collaboration Highlights:
    - 20% Commission on sales.
    - Tiered Bonuses for top performers.
    - Advertising Support for your content.
    - Product Trial for personal use.
    ''')

    # -----------------------------------2.choose product---------------------------------
    # click product
    _wait(By.CSS_SELECTOR, '[data-e2e="2db00f21-e6e3-0eda"]')
    driver.find_elements(By.CSS_SELECTOR, '[data-e2e="2db00f21-e6e3-0eda"]')[1].click()
    # Add product
    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="05f9b037-2b9d-d20b"]'),'click')

    # # 点击sold两次
    # time.sleep(1)
    # _wait(By.CSS_SELECTOR, 'div.sc-hRJfrW.gyanuy tr th:nth-child(4)')
    # is_element(By.CSS_SELECTOR,' div.arco-table-container  th:nth-child(4) > div > div > span > div > div')
    # time.sleep(1)
    # is_element(By.CSS_SELECTOR,' div.arco-table-container  th:nth-child(4) > div > div > span > div > div')

    #点商品名字
    input_or_click_element((By.CSS_SELECTOR, 'body > div.arco-drawer-wrapper > div.arco-drawer.m4b-drawer.slideRight-appear-done.slideRight-enter-done > div > span > div > div.arco-drawer-content > div > div > div.flex.items-center.space-x-12.mb-16 > div.m4b-input-group-select > div.arco-select.arco-select-single.arco-select-size-default.m4b-select.m4b-new-select.m4b-select.m4b-input-group-select-child.m4b-select-has-tooltip-error.m4b-select-multiple-nowrap > div > span'),'click')
    #点击商品id
    time.sleep(1)
    is_element(By.CSS_SELECTOR, '#arco-select-popup-5 > div > div > li:nth-child(2)')
    #输入商品id并搜索
    time.sleep(1)
    input_or_click_element((By.CSS_SELECTOR, '[data-tid="m4b_input_search"]'),'input',input_value='1729913816983376656')
    input_or_click_element((By.CSS_SELECTOR, 'div.arco-input-group-wrapper.arco-input-group-wrapper-default.arco-input-has-suffix.arco-input-search.m4b-input-search.m4b-input-group-select-child  span.arco-input-group-suffix > svg'),'click')
    # 全选product
    input_or_click_element((By.CSS_SELECTOR,'body > div.arco-drawer-wrapper > div.arco-drawer.m4b-drawer.slideRight-appear-done.slideRight-enter-done > div > span > div > div.arco-drawer-content > div > div > div.sc-hRJfrW.gyanuy > div > div > div > div.arco-table-container > div > div > table > thead > tr > th.arco-table-th.arco-table-operation.arco-table-checkbox > div > label > span > div'),'click')
    # Add
    time.sleep(1)
    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="6453523e-5b3f-f3a9"]'),'click')
    # send20
    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="3a1bf7cf-465b-f541"]'),'input',input_value='20')

    # -----------------------------------3.set up free sample--------------
    # click
    driver.find_elements(By.CSS_SELECTOR, '[data-tid="m4b_collapse_item"]')[2].click()
    # Manually review requests
    input_or_click_element((By.CSS_SELECTOR, '#content-container > main > div > div > div > div > div.arco-spin.m4b-loading.sc-dcJsrY.iNoNsl.w-full.h-full > div > form > div > div > div.flex.flex-col.flex-grow.space-y-16 > div.arco-collapse.arco-collapse-borderless.m4b-collapse.m4b-collapse-title-default.sc-cfxfcM.kqvQmQ > div:nth-child(3) > div > div > div.arco-collapse-item-content.arco-collapse-item-content-expanded > div > div.arco-radio-group.arco-radio-size-default.arco-radio-mode-outline.m4b-radio-group.flex.justify-between.mt-16.m4b-radio-group-gap-size-default > label:nth-child(2) > div > div:nth-child(1) > span > div'),'click')


    # -----------------------------------4.choose creators-----------------
    # click choose creators
    time.sleep(1)
    driver.find_elements(By.CSS_SELECTOR, '[data-e2e="1adf7b37-5743-0a73"]')[-1].click()
    # creators
    time.sleep(1)
    driver.find_elements(By.CSS_SELECTOR, 'table thead tr th div')[-5].click()
    # send
    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="140f8059-efa6-4618"]'),'click')
    time.sleep(3)
    # 发送成功
    if driver.find_element(By.CSS_SELECTOR,
                           'div.flex.items-center.justify-center.mb-16 > div'):
        print('发送成功')
    else:
        print('发送失败')





    # print(bool_)
    # 打开一个新标签页
    # time.sleep(5)
    # driver.execute_script(f"window.open('{SETTINGS_DATA.get('my_url')}');")
    #
    # # 切换到新打开的标签页
    # driver.switch_to.window(driver.window_handles[-1])
    #
    # bool_ = delete_tag(tag)
    # print(bool_)

flag = True
while flag:
    flag, names = split_xlsx('TKPersonData.xlsx')
    upload_files()
    tag = selector_tag()
    run()
    delete_tag(tag)
    update_status(names)

# selector_tag()
# run()




