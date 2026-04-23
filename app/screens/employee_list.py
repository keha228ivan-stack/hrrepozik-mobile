from kivy.lang import Builder
from kivymd.uix.list import OneLineAvatarIconListItem

from app.screens.base import BaseScreen

KV = '''
#:import dp kivy.metrics.dp
#:import get_color_from_hex kivy.utils.get_color_from_hex
<EmployeeListScreen>:
    name: "employees"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#F4F7FB")
        MDTopAppBar:
            title: "Сотрудники"
            left_action_items: [["arrow-left", lambda x: app.go("manager_dashboard")]]
            right_action_items: [["home-outline", lambda x: app.go("manager_dashboard")], ["logout", lambda x: app.logout()]]
        MDTextField:
            id: new_employee_email
            hint_text: "Email нового сотрудника"
        MDRaisedButton:
            text: "Добавить сотрудника"
            on_release: root.add_employee()
        ScrollView:
            MDList:
                id: employee_list
'''
Builder.load_string(KV)


class EmployeeListScreen(BaseScreen):
    def on_pre_enter(self, *args):
        items = self.app.load_employees()
        self.ids.employee_list.clear_widgets()
        for emp in items:
            item = OneLineAvatarIconListItem(text=f"{emp.name} ({emp.avg_progress}%)")
            item.bind(on_release=lambda _, uid=emp.user_id: self.app.open_employee(uid))
            self.ids.employee_list.add_widget(item)

    def add_employee(self):
        email = self.ids.new_employee_email.text.strip()
        if not email:
            return
        self.app.add_employee(email)
        self.on_pre_enter()
