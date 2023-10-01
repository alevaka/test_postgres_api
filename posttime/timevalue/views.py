from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import TimeValueAggregated
from .serializers import TimeValueAggregatedSerializer


class TimeValueAggregatedViewset(ReadOnlyModelViewSet):
    """Вьюсет для получения списка агрегированных минутных данных
    из представления данных таблицы time_value"""

    queryset = TimeValueAggregated.objects.all()
    serializer_class = TimeValueAggregatedSerializer

    permission_classes = [permissions.IsAuthenticated, ]
