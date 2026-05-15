from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedCardsPlan, SeedAccountsPlan


class ExistingUserGetDocumentsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который выполняет операцию покупки.
    Создаёт 300 пользователей, открывает кредитный счёт и выдаёт карты.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга, который описывает, сколько пользователей нужно создать
        и какие именно данные для них генерировать.
        В данном случае создаём 100 пользователей, каждому создает сберегательный и депозитные счета.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=100,  # Количество пользователей
                savings_accounts=SeedAccountsPlan(count=1),
                deposit_accounts=SeedAccountsPlan(count=1)
            )
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_get_documents"


if __name__ == '__main__':
    # Если файл запускается напрямую, создаём объект сценария и запускаем его.
    seeds_scenario = ExistingUserGetDocumentsSeedsScenario()
    seeds_scenario.build()  # Стартуем процесс сидинга