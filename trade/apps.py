from django.apps import AppConfig  # Importa a classe AppConfig do Django para configurar a aplicação


class TradeConfig(AppConfig):
    # Define o tipo de campo auto-incremento padrão para modelos nesta aplicação
    default_auto_field = 'django.db.models.BigAutoField'

    # Nome da aplicação Django. Deve corresponder ao nome do diretório da aplicação ou ao nome do módulo.
    name = 'trade'

