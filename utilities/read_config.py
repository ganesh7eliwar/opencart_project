import configparser

config = configparser.RawConfigParser()
config.read('./configurations/config.ini')


class ReadConfigRP:

    @staticmethod
    def url():
        page_url = config.get('register page', 'url')
        return page_url

    @staticmethod
    def first_name():
        f_name = config.get('register page', 'first_name')
        return f_name

    @staticmethod
    def last_name():
        l_name = config.get('register page', 'last_name')
        return l_name

    @staticmethod
    def telephone():
        phone_no = config.get('register page', 'telephone')
        return phone_no

    @staticmethod
    def password():
        pass_wd = config.get('register page', 'password')
        return pass_wd

    @staticmethod
    def expected_title():
        exp_title = config.get('register page', 'expected_title')
        return exp_title


class ReadConfigLP:

    @staticmethod
    def email():
        email_id = config.get('login page', 'email')
        return email_id

    @staticmethod
    def password():
        pass_wd = config.get('login page', 'password')
        return pass_wd

    @staticmethod
    def expected_title():
        exp_title = config.get('login page', 'expected_title')
        return exp_title


class Url:

    @staticmethod
    def expected_url():
        exp_title = config.get('Url', 'expected_title')
        return exp_title


class Search:

    @staticmethod
    def item_name():
        item_n = config.get('search', 'item_name')
        return item_n

    @staticmethod
    def expected_item():
        exp_item =  config.get('search', 'expected_item')
        return exp_item