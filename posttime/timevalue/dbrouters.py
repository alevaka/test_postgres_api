class DataDBRouter:
    """Роутер БД для доступа к БД time_value"""

    route_app_labels = {"timevalue", }

    def db_for_read(self, model, **hints):
        """Чтение модели TimeValueAggregated из БД data"""
        if model._meta.app_label in self.route_app_labels:
            return 'data'
        return 'default'

    def db_for_write(self, model, **hints):
        """Запись модели TimeValueAggregated из БД data"""
        if model._meta.app_label in self.route_app_labels:
            return 'data'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return False
        return (db == 'default')
