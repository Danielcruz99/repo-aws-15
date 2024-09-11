from collections.abc import Mapping
from typing import Any

from boto.connection import AWSQueryConnection

class KMSConnection(AWSQueryConnection):
    APIVersion: str
    DefaultRegionName: str
    DefaultRegionEndpoint: str
    ServiceName: str
    TargetPrefix: str
    ResponseError: type[Exception]
    region: Any
    def __init__(self, **kwargs) -> None: ...
    def create_alias(self, alias_name: str, target_key_id: str) -> dict[str, Any] | None: ...
    def create_grant(
        self,
        key_id: str,
        grantee_principal: str,
        retiring_principal: str | None = None,
        operations: list[str] | None = None,
        constraints: dict[str, dict[str, str]] | None = None,
        grant_tokens: list[str] | None = None,
    ) -> dict[str, Any] | None: ...
    def create_key(
        self, policy: str | None = None, description: str | None = None, key_usage: str | None = None
    ) -> dict[str, Any] | None: ...
    def decrypt(
        self, ciphertext_blob: bytes, encryption_context: Mapping[str, Any] | None = None, grant_tokens: list[str] | None = None
    ) -> dict[str, Any] | None: ...
    def delete_alias(self, alias_name: str) -> dict[str, Any] | None: ...
    def describe_key(self, key_id: str) -> dict[str, Any] | None: ...
    def disable_key(self, key_id: str) -> dict[str, Any] | None: ...
    def disable_key_rotation(self, key_id: str) -> dict[str, Any] | None: ...
    def enable_key(self, key_id: str) -> dict[str, Any] | None: ...
    def enable_key_rotation(self, key_id: str) -> dict[str, Any] | None: ...
    def encrypt(
        self,
        key_id: str,
        plaintext: bytes,
        encryption_context: Mapping[str, Any] | None = None,
        grant_tokens: list[str] | None = None,
    ) -> dict[str, Any] | None: ...
    def generate_data_key(
        self,
        key_id: str,
        encryption_context: Mapping[str, Any] | None = None,
        number_of_bytes: int | None = None,
        key_spec: str | None = None,
        grant_tokens: list[str] | None = None,
    ) -> dict[str, Any] | None: ...
    def generate_data_key_without_plaintext(
        self,
        key_id: str,
        encryption_context: Mapping[str, Any] | None = None,
        key_spec: str | None = None,
        number_of_bytes: int | None = None,
        grant_tokens: list[str] | None = None,
    ) -> dict[str, Any] | None: ...
    def generate_random(self, number_of_bytes: int | None = None) -> dict[str, Any] | None: ...
    def get_key_policy(self, key_id: str, policy_name: str) -> dict[str, Any] | None: ...
    def get_key_rotation_status(self, key_id: str) -> dict[str, Any] | None: ...
    def list_aliases(self, limit: int | None = None, marker: str | None = None) -> dict[str, Any] | None: ...
    def list_grants(self, key_id: str, limit: int | None = None, marker: str | None = None) -> dict[str, Any] | None: ...
    def list_key_policies(self, key_id: str, limit: int | None = None, marker: str | None = None) -> dict[str, Any] | None: ...
    def list_keys(self, limit: int | None = None, marker: str | None = None) -> dict[str, Any] | None: ...
    def put_key_policy(self, key_id: str, policy_name: str, policy: str) -> dict[str, Any] | None: ...
    def re_encrypt(
        self,
        ciphertext_blob: bytes,
        destination_key_id: str,
        source_encryption_context: Mapping[str, Any] | None = None,
        destination_encryption_context: Mapping[str, Any] | None = None,
        grant_tokens: list[str] | None = None,
    ) -> dict[str, Any] | None: ...
    def retire_grant(self, grant_token: str) -> dict[str, Any] | None: ...
    def revoke_grant(self, key_id: str, grant_id: str) -> dict[str, Any] | None: ...
    def update_key_description(self, key_id: str, description: str) -> dict[str, Any] | None: ...
