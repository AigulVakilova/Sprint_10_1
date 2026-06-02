import allure

@allure.feature("Отрисовка маршрута")
class TestRouteRendering:

    @allure.title("При вводе двух разных адресов на карте отображаются две точки маршрута")
    def test_two_pins_displayed_on_map_with_different_addresses(self, pages_with_two_addresses):
        main_page, route_page = pages_with_two_addresses

        with allure.step("Проверить отображение точки начала маршрута"):
            assert main_page.is_from_pin_displayed(), "Точка начала маршрута не отображается на карте"

        with allure.step("Проверить отображение точки конца маршрута"):
            assert main_page.is_to_pin_displayed(), "Точка конца маршрута не отображается на карте"
