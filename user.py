class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = 'user'

    def __str__(self):
        return f"{self.username} ({self.role})"