import configparser

config = configparser.RawConfigParser()
config.read('./configurations/config.ini')


class ReadConfigRP:

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

    @staticmethod
    def url():
        page_url = config.get('Url', 'url')
        return page_url


class Search:

    @staticmethod
    def item_name():
        item_n = config.get('search', 'item_name')
        return item_n

    @staticmethod
    def expected_item():
        exp_item = config.get('search', 'expected_item')
        return exp_item
