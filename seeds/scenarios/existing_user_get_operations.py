from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan

class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который для просмотра опреций.
    Создаёт 300 пользователей, создает кредитный счет и выполняет опреции:
            покупки: 5
            пополнения: 1
            снятия наличных: 1
    """
    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга, который описывает, сколько пользователей нужно создать
        и какие именно данные для них генерировать.
        В данном случае создаём 300 пользователей, каждому создает кредитный счет и выполняет опреции:
            покупки: 5
            пополнения: 1
            снятия наличных: 1
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    top_up_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1)
                )
            )
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_get_operations"

if __name__ == "__main__":
    # Если файл запускается напрямую, создаём объект сценария и запускаем его.
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()  # Стартуем процесс сидинга