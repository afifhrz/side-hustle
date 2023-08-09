from model.main import Model
from model.auth import User
from view.main import View


class SignInController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.page1login_button.config(command=self.signin)
        self.frame.page1create_user.config(command=self.signup)

    def signup(self) -> None:
        self.view.switch("signup")

    def signin(self) -> None:
        username = self.frame.usernameEntry.get()
        pasword = self.frame.passwordEntry.get()
        data = {"username": username, "password": pasword}
        print(data)
        self.frame.password_input.delete(0, last=len(pasword))
        user: User = {"username": data["username"]}
        self.model.auth.login(user)
