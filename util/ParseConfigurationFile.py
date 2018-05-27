# -*- coding = utf-8 -*-
from configparser import ConfigParser
from config.VarConfig import pageElementLocatorPath


class ParseConfigFile(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def get_items_section(self, section_name):
        options_dict = dict(self.cf.items(section_name))
        return options_dict

    def get_option_value(self, section_name, option_name):
        value = self.cf.get(section_name, option_name)
        return value


if __name__ == '__main__':
    pc = ParseConfigFile()
    print(pc.get_items_section('51kaihui_login'))
    print(pc.get_option_value('51kaihui_login', 'loginPage.username'))