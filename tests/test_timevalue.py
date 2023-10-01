import datetime

import pytest
from django.conf import settings


class TestTimeValueAggregatedAPI():
    """Тестирование доступа по API к /timevalue/avg/"""

    url = '/timevalue/avg/'

    @pytest.mark.django_db(databases=['default', 'data'])
    def test_access_not_authenticated(self, client):
        """Запрос от неавторизованного пользователя должен отклоняться"""

        response = client.get(self.url)

        code = 401
        assert response.status_code == code, (
            f'Анонимный пользователь при запросе {self.url} '
            f'должен получать ответ с кодом {code}')

    @pytest.mark.django_db(databases=['default', 'data'])
    def test_access_authenticated(self, user_client):
        """Запрос от авторизованного пользователя должен проходить успешно
        Количесвто результатов должно совпадать с настройками пагинации"""

        response = user_client.get(self.url)
        code = 200
        assert response.status_code == code, (
            f'Авторизованный пользователь при запросе {self.url} '
            f'должен получать ответ с кодом {code}')

        assert len(response.data['results']) == settings.DEFAULT_PAGE_SIZE, (
            f'Количество выводимых результатов должно быть '
            f'равно {settings.DEFAULT_PAGE_SIZE}')

    @pytest.mark.django_db(databases=['default', 'data'])
    def test_create_authenticated(self, user_client):
        """Попытка записи должна отклоняться"""

        response = user_client.post(self.url, data={
            'minute': datetime.datetime.now(datetime.timezone.utc),
            'avg_value': 999
            })

        code = 405
        assert response.status_code == code, (
            f'Авторизованный пользователь при записи {self.url} '
            f'должен получать ответ с кодом {code}')

    @pytest.mark.django_db(databases=['default', 'data'])
    def test_delete_authenticated(self, user_client):
        """Попытка удаления должна отклоняться"""

        response = user_client.delete(self.url, data={
            'minute': datetime.datetime.now(
                datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:00Z'),
            })

        code = 405
        assert response.status_code == code, (
            f'Авторизованный пользователь при удалении {self.url} '
            f'должен получать ответ с кодом {code}')

    @pytest.mark.django_db(databases=['default', 'data'])
    def test_get_last_authenticated(self, user_client):
        """Запрос последней записи должен отдавать корректные результаты"""

        minute = datetime.datetime.now(datetime.timezone.utc)
        minute_str = minute.strftime('%Y-%m-%dT%H:%M:00Z')
        item_url = self.url + minute_str + '/'
        response = user_client.get(item_url)

        code = 200
        assert response.status_code == code, (
            f'Авторизованный пользователь при запросе {item_url} '
            f'должен получать ответ с кодом {code}')

        assert response.data['minute'] == minute_str, (
            f'Запрошенное время {minute_str} не совпадает'
            f'со временем ответа {response.data["minute"]}')

        assert isinstance(response.data['avg_value'], float), (
            f'Тип данных {response.data["avg_value"]} '
            'должен быть числом с плавающей точкой')
