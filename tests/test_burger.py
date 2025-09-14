from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestForBurger:
    """Класс для тестирования функциональности бургера."""

    def test_set_buns(self, bun: "Bun") -> None:
        """Тест установки булочки."""
        burger = Burger()  # Создаём объект прямо в тесте
        burger.set_buns(bun)
        assert burger.bun == bun, "Булочка установлена некорректно"

    def test_add_ingredient(self, ingredient: "Ingredient") -> None:
        """Тест добавления ингредиента."""
        burger = Burger()  # Создаём объект прямо в тесте
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient, "Ингредиент не добавлен"
        assert len(burger.ingredients) == 1, "Неверное количество ингредиентов"

    def test_remove_ingredient(self, ingredient: "Ingredient") -> None:
        """Тест удаления ингредиента."""
        burger = Burger()  # Создаём объект прямо в тесте
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0, "Ингредиент не удален"

    def test_move_ingredient(self, ingredient: "Ingredient") -> None:
        """Тест перемещения ингредиента."""
        burger = Burger()  # Создаём объект прямо в тесте
        burger.add_ingredient(ingredient)
        ingredient_another = Ingredient(
            INGREDIENT_TYPE_FILLING,
            'сыр',
            19.99
        )
        burger.add_ingredient(ingredient_another)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == ingredient_another, (
            "Неверное перемещение"
        )
        assert burger.ingredients[1] == ingredient, "Неверное перемещение"

    def test_get_price(self, bun: "Bun", ingredient: "Ingredient") -> None:
        """Тест расчета стоимости бургера."""
        burger = Burger()  # Создаём объект прямо в тесте
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_price = bun.get_price() * 2 + ingredient.get_price()

        assert burger.get_price() == expected_price, (
            "Неверный расчет стоимости бургера"
        )

    # Проверка формирования чека
    def test_get_receipt(
        self, bun: "Bun", ingredient: "Ingredient"
    ) -> None:
        """
        Тест проверки формирования чека для бургера.

        Проверяет:
        * Корректность отображения булочек
        * Правильность отображения ингредиентов
        * Верность формирования итоговой цены
        """
        burger = Burger()  # Создаём объект прямо в тесте

        # Настройка бургера
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        # Формирование ожидаемого чека
        expected_receipt = (
            f'(==== {bun.get_name()} ====)\n'
            f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n'
            f'(==== {bun.get_name()} ====)\n\n'
            f'Price: {burger.get_price():.2f}'
        )

        # Проверка результата
        assert burger.get_receipt() == expected_receipt, (
            "Сформированный чек не соответствует ожидаемому результату"
        )
