import allure

@allure.feature("Подготовка к заказу такси")
class TestTaxiOrderPreparation:

    @allure.title("При переключении Оптимальный->Быстрый меняется активный таб и пересчитывается стоимость/время")
    def test_switching_between_optimal_and_fast_tabs(self, pages_with_two_addresses):
        main_page, route_page = pages_with_two_addresses

        with allure.step("Нажать на таб Оптимальный"):
            route_page.click_route_optimal()

        with allure.step("Проверить, что таб Оптимальный активен"):
            assert route_page.is_optimal_tab_active(), "Таб Оптимальный не активен"

        with allure.step("Запомнить стоимость и время маршрута Оптимальный"):
            price_optimal = route_page.get_route_price()
            time_optimal = route_page.get_route_time()

        with allure.step("Нажать на таб Быстрый"):
            route_page.click_route_fast()

        with allure.step("Проверить, что таб Быстрый активен"):
            assert route_page.is_fast_tab_active(), "Таб Быстрый не активен после переключения"

        with allure.step("Проверить пересчёт стоимости или времени"):
            price_fast = route_page.get_route_price()
            time_fast = route_page.get_route_time()
            assert price_optimal != price_fast or time_optimal != time_fast, \
                "Стоимость и время не изменились при переключении с Оптимального на Быстрый"

    @allure.title("При выборе вида маршрута Свой становятся активны все типы передвижения")
    def test_custom_route_enables_all_transport_types(self, pages_with_two_addresses):
        main_page, route_page = pages_with_two_addresses

        with allure.step("Нажать на таб Свой"):
            route_page.click_route_custom()

        with allure.step("Проверить, что таб Свой активен"):
            assert route_page.is_custom_tab_active(), "Таб Свой не активен после нажатия"

        with allure.step("Проверить, что все типы передвижения отображаются"):
            assert route_page.are_all_transport_types_displayed(), \
                "Не все типы передвижения отображаются при выборе маршрута Свой"

    @allure.title("При выборе вида маршрута Быстрый активна кнопка Вызвать такси")
    def test_fast_route_shows_call_taxi_button(self, pages_with_two_addresses):
        main_page, route_page = pages_with_two_addresses

        with allure.step("Нажать на таб Быстрый"):
            route_page.click_route_fast()

        with allure.step("Проверить, что кнопка Вызвать такси отображается и активна"):
            assert route_page.is_call_taxi_button_displayed(), "Кнопка Вызвать такси не отображается"
            assert route_page.is_call_taxi_button_enabled(), "Кнопка Вызвать такси не активна"

    @allure.title("При выборе маршрута Свой и типа Драйв активна кнопка Забронировать")
    def test_custom_drive_shows_book_button(self, pages_with_two_addresses):
        main_page, route_page = pages_with_two_addresses

        with allure.step("Нажать на таб Свой"):
            route_page.click_route_custom()

        with allure.step("Выбрать тип передвижения Драйв"):
            route_page.click_transport_drive()

        with allure.step("Проверить, что кнопка Забронировать отображается и активна"):
            assert route_page.is_book_drive_button_displayed(), "Кнопка Забронировать не отображается"
            assert route_page.is_book_drive_button_enabled(), "Кнопка Забронировать не активна"
