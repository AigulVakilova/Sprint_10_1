import allure
import pytest
import data

@allure.feature("Заказ тарифа Такси")
class TestTaxiTariffOrder:

    @allure.title("Открывается форма заказа со всеми 6 тарифами, один из них активный")
    def test_order_form_has_six_tariffs_one_active(self, pages_ready_for_taxi_order):
        main_page, route_page, order_taxi_page = pages_ready_for_taxi_order

        with allure.step("Проверить, что форма заказа отображается"):
            assert order_taxi_page.is_order_form_displayed(), "Форма заказа такси не отображается"

        with allure.step("Проверить, что отображаются все 6 тарифов"):
            assert order_taxi_page.count_visible_tariffs() == 6, \
                f"Отображается не 6 тарифов, а {order_taxi_page.count_visible_tariffs()}"

        with allure.step("Проверить, что один тариф активен"):
            assert order_taxi_page.is_any_tariff_active(), "Ни один тариф не отмечен как активный"

    @allure.title("При наведении на иконку i тарифа Рабочий отображается верное описание")
    def test_tariff_work_tooltip_shows_correct_description(self, pages_ready_for_taxi_order):
        main_page, route_page, order_taxi_page = pages_ready_for_taxi_order

        with allure.step("Навести курсор на иконку i тарифа Рабочий"):
            order_taxi_page.hover_tariff_info_icon(data.TARIFF_WORK)

        with allure.step("Проверить, что тултип отображается"):
            assert order_taxi_page.is_tooltip_displayed(), "Тултип с описанием тарифа не отображается"

        with allure.step("Проверить текст описания тарифа Рабочий"):
            tooltip_text = order_taxi_page.get_tooltip_text()
            expected = data.TARIFF_DESCRIPTIONS[data.TARIFF_WORK]
            assert expected in tooltip_text, \
                f"Описание тарифа '{data.TARIFF_WORK}' не совпадает. Ожидалось: '{expected}', получено: '{tooltip_text}'"

    @allure.title("При наведении на иконку i тарифа Сонный отображается верное описание")
    @pytest.mark.xfail(reason="Баг: перепутаны описания тарифов Сонный и Разговорчивый")
    def test_tariff_sleepy_tooltip_shows_correct_description(self, pages_ready_for_taxi_order):
        main_page, route_page, order_taxi_page = pages_ready_for_taxi_order

        with allure.step("Выбрать тариф Сонный"):
            order_taxi_page.click_tariff_by_name(data.TARIFF_SLEEPY)

        with allure.step("Навести курсор на иконку i тарифа Сонный"):
            order_taxi_page.hover_tariff_info_icon(data.TARIFF_SLEEPY)

        with allure.step("Проверить, что тултип отображается"):
            assert order_taxi_page.is_tooltip_displayed(), "Тултип не отображается"

        with allure.step("Проверить текст описания тарифа Сонный"):
            tooltip_text = order_taxi_page.get_tooltip_text()
            expected = data.TARIFF_DESCRIPTIONS[data.TARIFF_SLEEPY]
            assert expected in tooltip_text, \
                f"Описание тарифа '{data.TARIFF_SLEEPY}' не совпадает. Ожидалось: '{expected}', получено: '{tooltip_text}'"

    @allure.title("При наведении на иконку i тарифа Отпускной отображается верное описание")
    def test_tariff_vacation_tooltip_shows_correct_description(self, pages_ready_for_taxi_order):
        main_page, route_page, order_taxi_page = pages_ready_for_taxi_order

        with allure.step("Выбрать тариф Отпускной"):
            order_taxi_page.click_tariff_by_name(data.TARIFF_VACATION)

        with allure.step("Навести курсор на иконку i тарифа Отпускной"):
            order_taxi_page.hover_tariff_info_icon(data.TARIFF_VACATION)

        with allure.step("Проверить, что тултип отображается"):
            assert order_taxi_page.is_tooltip_displayed(), "Тултип не отображается"

        with allure.step("Проверить текст описания тарифа Отпускной"):
            tooltip_text = order_taxi_page.get_tooltip_text()
            expected = data.TARIFF_DESCRIPTIONS[data.TARIFF_VACATION]
            assert expected in tooltip_text, \
                f"Описание тарифа '{data.TARIFF_VACATION}' не совпадает. Ожидалось: '{expected}', получено: '{tooltip_text}'"

    @allure.title("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий, Требования")
    def test_order_fields_block_displayed(self, pages_ready_for_taxi_order):
        main_page, route_page, order_taxi_page = pages_ready_for_taxi_order

        with allure.step("Проверить отображение поля Телефон"):
            assert order_taxi_page.is_phone_field_displayed(), "Поле Телефон не отображается"

        with allure.step("Проверить отображение поля Способ оплаты"):
            assert order_taxi_page.is_payment_field_displayed(), "Поле Способ оплаты не отображается"

        with allure.step("Проверить отображение поля Комментарий водителю"):
            assert order_taxi_page.is_comment_field_displayed(), "Поле Комментарий водителю не отображается"

        with allure.step("Проверить отображение блока Требования к заказу"):
            assert order_taxi_page.is_requirements_block_displayed(), "Блок Требования к заказу не отображается"


@allure.feature("Заказ тарифа Такси")
class TestTaxiFullFlow:

    @allure.title("Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать - Появляется окно ожидания машины (проверить элементы по ТЗ)")
    @pytest.mark.xfail(reason="Баг: чекбокс Столик для ноутбука включён по умолчанию")
    def test_full_taxi_order_flow(self, pages_ready_for_taxi_order, search_page):
        main_page, route_page, order_taxi_page = pages_ready_for_taxi_order

        with allure.step("Выбрать тариф Рабочий"):
            order_taxi_page.click_tariff_work()

        with allure.step("Включить чекбокс Столик для ноутбука"):
            order_taxi_page.enable_laptop_table_switch()

        with allure.step("Запомнить стоимость тарифа"):
            tariff_price = order_taxi_page.get_tariff_price(data.TARIFF_WORK)

        with allure.step("Нажать кнопку Ввести номер и заказать"):
            order_taxi_page.click_enter_number_button()

        with allure.step("Проверить, что появилось окно поиска машины"):
            assert search_page.is_search_window_displayed(), "Окно поиска машины не появилось"

        with allure.step("Проверить заголовок окна поиска"):
            assert data.SEARCH_TITLE in search_page.get_search_title_text(), \
                f"Заголовок окна поиска не содержит '{data.SEARCH_TITLE}'"

        with allure.step("Проверить наличие таймера обратного отсчёта"):
            assert search_page.is_timer_displayed(), "Таймер обратного отсчёта не отображается"

        with allure.step("Проверить кнопку Отменить в окне поиска"):
            assert search_page.is_cancel_button_displayed(), "Кнопка Отменить не отображается"

        with allure.step("Проверить кнопку Детали в окне поиска"):
            assert search_page.is_details_button_displayed(), "Кнопка Детали не отображается"

        with allure.step("Дождаться окончания таймера и появления окна совершённого заказа"):
            search_page.wait_for_completed_order()
            assert search_page.is_completed_order_displayed(), "Окно совершённого заказа не отображается"

        with allure.step("Проверить элементы окна совершённого заказа"):
            assert search_page.is_car_number_displayed(), "Номер автомобиля не отображается"
            assert search_page.is_car_image_displayed(), "Картинка тарифа не отображается"
            assert search_page.is_driver_name_displayed(), "Имя водителя не отображается"
            assert search_page.is_driver_photo_displayed(), "Фото водителя не отображается"
            assert search_page.is_driver_rating_displayed(), "Рейтинг водителя не отображается"

        with allure.step("Нажать кнопку Детали"):
            search_page.click_details_button()

        with allure.step("Проверить, что открылось окно Детали"):
            assert search_page.is_details_block_displayed(), "Окно Детали не открылось"

        with allure.step("Проверить, что в Деталях указана стоимость тарифа"):
            details_cost = search_page.get_details_cost()
            assert tariff_price in details_cost, \
                f"Стоимость в Деталях '{details_cost}' не совпадает с выбранной '{tariff_price}'"

        with allure.step("Нажать кнопку Отмена"):
            search_page.click_cancel_button()

        with allure.step("Проверить, что окно закрылось"):
            assert search_page.is_search_window_closed(), "Окно заказа не закрылось после нажатия Отмена"
