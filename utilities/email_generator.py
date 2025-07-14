import random
import string


class EmailGenerator:
    @staticmethod
    def generate_email():
        username = ''.join(random.choices(string.ascii_lowercase, k=5))
        domain = random.choice(['gmail', 'yahoomail', 'outlook'])
        return f"{username}@{domain}.com"
