
from datetime import datetime
from typing import Any, Dict, List, Optional

try:
    from pydantic import HttpUrl
except ImportError:
    from typing import AnyStr as HttpUrl

from .data import AttributesModel


class StateVersionModel(AttributesModel):
    vcs_commit_sha: Optional[str]
    vcs_commit_url: Optional[str]
    created_at: Optional[datetime]
    hosted_state_download_url: Optional[HttpUrl]
    serial: Optional[int]
    size: Optional[int]
    state_version: Optional[int]

    modules: Optional[Dict]
    providers: Optional[Dict]
    resources: Optional[List[Dict]]


class StateVersionOutputModel(AttributesModel):
    name: str
    sensitive: bool
    type: str
    value: Any
