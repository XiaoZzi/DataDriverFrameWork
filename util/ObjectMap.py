# -*- coding = utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait


# 获取单个页面元素对象
def get_element(d, locate_type, locate_expression):
    try:
        element = WebDriverWait(d, 30).until(
            (lambda x: x.find_element(by=locate_type, value=locate_expression))
        )
        return element
    except Exception as e:
        raise e


# 获取多个相同页面元素对象，以list返回
# 不知道什么时候需要用到？
def get_elements(d, locate_type, locate_expression):
    try:
        elements = WebDriverWait(d, 30).until(
            (lambda x: x.find_elements(by=locate_type, value=locate_expression))
        )
        return elements
    except Exception as e:
        raise e


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    searchbox = get_element(d=driver, locate_type='id', locate_expression='kw')
    print(searchbox.tag_name)
    aList = get_elements(d=driver, locate_type='tag name', locate_expression='a')
    print(aList)
    driver.quit()