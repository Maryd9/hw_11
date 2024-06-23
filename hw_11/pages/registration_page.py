import time

import tests.resources.resource
from selene import browser, have, command
from hw_11.data.user import User


class RegistrationFormPage:
    def __init__(self):
        self.first_name_element = browser.element('#firstName')
        self.last_name_element = browser.element('#lastName')
        self.user_email_element = browser.element('#userEmail')
        self.gender_element = browser.all('.custom-control-label')
        self.user_phone_element = browser.element('#userNumber')
        self.date_of_birth_element = browser.element('#dateOfBirthInput')
        self.subject_element = browser.element('#subjectsInput')
        self.hobby_element = browser.all(".custom-control-label")
        self.picture_element = browser.element('#uploadPicture')
        self.current_address_element = browser.element('#currentAddress')
        self.state_element = browser.element('#state')
        self.city_element = browser.element('#city')
        self.table_element = browser.element('.table').all('td')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command=command.js.remove)

    def _fill_first_name(self, value):
        self.first_name_element.type(value)
        return self

    def _fill_last_name(self, value):
        self.last_name_element.type(value)
        return self

    def _fill_user_email(self, value):
        self.user_email_element.type(value)
        return self

    def _fill_gender(self, value):
        self.gender_element.element_by(have.exact_text(value)).perform(command.js.scroll_into_view).click()
        return self

    def _fill_user_phone(self, value):
        self.user_phone_element.type(value)
        return self

    def _fill_date_of_birth(self, year, month, day):
        self.date_of_birth_element.click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def _fill_subject(self, value):
        self.subject_element.type(value).press_enter()
        return self

    def _fill_hobby(self, value):
        self.hobby_element.element_by(have.exact_text(value)).perform(command.js.scroll_into_view).click()
        return self

    def _fill_picture(self, file_name):
        self.picture_element.set_value(tests.resources.resource.path(file_name))
        return self

    def _fill_current_address(self, value):
        self.current_address_element.type(value)
        return self

    def _fill_state(self, value):
        self.state_element.perform(command.js.scroll_into_view)
        self.state_element.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def _fill_city(self, value):
        self.city_element.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def _click_submit(self):
        browser.element('#submit').click()
        return self

    def register(self, user: User):
        (
            self._fill_first_name(user.first_name)
            ._fill_last_name(user.last_name)
            ._fill_user_email(user.email)
            ._fill_gender(user.gender)
            ._fill_user_phone(user.phone)
            ._fill_date_of_birth(user.date_of_birth_year, user.date_of_birth_month, user.date_of_birth_day)
            ._fill_subject(user.subject)
            ._fill_hobby(user.hobby)
            ._fill_picture(user.picture)
            ._fill_current_address(user.address)
            ._fill_state(user.state)
            ._fill_city(user.city)
            ._click_submit()
        )

    def should_have_registered(self, user: User):
        self.table_element.even.should(
            have.exact_texts(f"{user.first_name} {user.last_name}",
                             user.email,
                             user.gender,
                             user.phone,
                             f"{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}",
                             user.subject,
                             user.hobby,
                             user.picture,
                             user.address,
                             f"{user.state} {user.city}", ))
        return self
