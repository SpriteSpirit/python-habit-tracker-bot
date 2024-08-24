from rest_framework import viewsets, pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from habits.models import Habit
from habits.permissions import IsOwnerOrReadOnly
from habits.serializers import UserHabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """ Контроллер для управления привычками """

    queryset = Habit.objects.all()
    serializer_class = UserHabitSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = pagination.PageNumberPagination

    def perform_create(self, serializer):
        """ Сохраняет привычку пользователя """

        serializer.save(user=self.request.user)

    def get_queryset(self):
        """ Получает привычки, отфильтрованные по параметру запроса `is_public` """

        if self.request.query_params.get('is_public'):
            return Habit.objects.filter(is_public=True)
        return super().get_queryset()


class SendRemindersView(APIView):
    """ Отправляет напоминания о выполнении привычек в Telegram бот """

    def post(self, request):
        reminders = Habit.objects.filter(frequency=1, is_public=True)

        for reminder in reminders:
            # Отправить напоминание в Telegram бот
            # send_reminder.delay(reminder.id)

            return Response()


# TODO: создать валидаторы validators.py
# TODO: в сериализатор добавить валидаторы
# TODO: настроить маршрутизацию
# TODO: настроить пагинацию
# TODO: создать тесты
# TODO: создать .env и перенести все уязвимые данные
