import unittest
from tkinter import Tk, messagebox
from unittest.mock import patch
from src.GUI.GUI_login import App

class TestVerifyIncorrectCredentials(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.root = self.app.root

    def tearDown(self):
        self.root.destroy()

    @patch.object(messagebox, 'showerror')
    def test_verify_incorrect_credentials(self, mock_showerror):
        # Configura las entradas de usuario y contraseña incorrectas
        self.app.user.insert(0, "usuario_incorrecto")
        self.app.password.insert(0, "contraseña_incorrecta")

        # Llama a la función verify
        self.app.verify()

        # Verifica que la ventana principal (root) aún exista
        self.assertTrue(self.root.winfo_exists())

        # Verifica que showerror fue llamado con los argumentos esperados
        mock_showerror.assert_called_once_with(message="Datos incorrectos", title="Mensaje")

if __name__ == '__main__':
    unittest.main()
