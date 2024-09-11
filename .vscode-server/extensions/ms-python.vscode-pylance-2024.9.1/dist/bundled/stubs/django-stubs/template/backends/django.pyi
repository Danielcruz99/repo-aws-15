from collections.abc import Iterator, Mapping
from typing import Any, NoReturn
from typing_extensions import override

from django.http.request import HttpRequest
from django.template import base
from django.template.engine import Engine
from django.template.exceptions import TemplateDoesNotExist
from django.utils.safestring import SafeText

from .base import BaseEngine

class DjangoTemplates(BaseEngine):
    engine: Engine = ...
    def __init__(self, params: dict[str, Any]) -> None: ...
    def get_templatetag_libraries(
        self, custom_libraries: dict[str, str]
    ) -> dict[str, str]: ...
    @override
    def from_string(self, template_code: str) -> Template: ...
    @override
    def get_template(self, template_name: str) -> Template: ...

class Template:
    template: base.Template
    backend: DjangoTemplates
    def __init__(self, template: base.Template, backend: DjangoTemplates) -> None: ...
    @property
    def origin(self) -> base.Origin: ...
    def render(
        self,
        context: Mapping[str, Any] | None = ...,
        request: HttpRequest | None = ...,
    ) -> SafeText: ...

def copy_exception(
    exc: TemplateDoesNotExist, backend: DjangoTemplates | None = ...
) -> TemplateDoesNotExist: ...
def reraise(exc: TemplateDoesNotExist, backend: DjangoTemplates) -> NoReturn: ...
def get_template_tag_modules() -> Iterator[tuple[str, str]]: ...
def get_installed_libraries() -> dict[str, str]: ...
def get_package_libraries(pkg: Any) -> Iterator[str]: ...
