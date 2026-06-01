import allure
import data

@allure.feature("Отрисовка блока с выбором маршрута")
class TestRouteBlockRendering:

    @allure.title("При вводе двух разных адресов отображается блок с выбором маршрута")
    def test_route_block_displayed_with_different_addresses(self, pages_with_two_addresses):
        main_page, route_page = pages_with_two_addresses

        with allure.step("Проверить, что блок с выбором маршрута отображается"):
            assert route_page.is_route_block_displayed(), "Блок с выбором маршрута не отображается"

    @allure.title("При вводе одинаковых адресов блок маршрута содержит текст 'Авто Бесплатно В пути 0 мин.'")
    def test_route_block_with_same_addresses_contains_correct_text(self, pages_with_same_address):
        main_page, route_page = pages_with_same_address

        with allure.step("Проверить, что блок с выбором маршрута отображается"):
            assert route_page.is_route_block_displayed(), "Блок с выбором маршрута не отображается"

        with allure.step(f"Проверить наличие текста '{data.SAME_ADDRESS_ROUTE_TEXT}' в блоке"):
            block_text = route_page.get_route_block_text()
            assert data.SAME_ADDRESS_ROUTE_TEXT in block_text, \
                f"Текст '{data.SAME_ADDRESS_ROUTE_TEXT}' не найден в блоке маршрута"

        with allure.step(f"Проверить наличие текста '{data.SAME_ADDRESS_TIME_TEXT}' в блоке"):
            assert data.SAME_ADDRESS_TIME_TEXT in block_text, \
                f"Текст '{data.SAME_ADDRESS_TIME_TEXT}' не найден в блоке маршрута"
