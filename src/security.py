# security.py
class Security:
    def __init__(self):
        self.users = {}  # {username: {password, role}}
        self.roles = ['admin', 'accountant', 'seller']

    def add_user(self, username, password, role):
        """Agrega un nuevo usuario con su rol."""
        if role in self.roles:
            self.users[username] = {'password': password, 'role': role}
        else:
            print("Rol no permitido")

    def authenticate(self, username, password):
        """Autentica a un usuario."""
        user = self.users.get(username)
        if user and user['password'] == password:
            return f"Autenticación exitosa. Rol: {user['role']}"
        else:
            return "Autenticación fallida"
