import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Column, Row
from flet_core.control_event import ControlEvent


def main(page:ft.page) -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.them_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200)
    checkbox_signup: Checkbox = Checkbox(label='I agree to it', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Sign up', width=200, disabled=True)

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.update()

    def submit(e: ControlEvent) -> None:
        print("Username:", text_username.value)
        print("Password:", text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f"Welcome: {text_username.value}", size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    page.add(
        Row(
            controls=[
                Column(
                    controls=[
                        text_username,
                        text_password,
                        checkbox_signup,
                        button_submit
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.app(target=main)      
