from django.apps import AppConfig


class DjangoInfraConfig(AppConfig):
    name = "src.shared.infrastructure"

    def ready(self) -> None:
        from src.config import settings
        from src.config.container import Container

        container = Container()
        container.config.from_dict(settings.__dict__)
        container.wire(modules=[".views"])
