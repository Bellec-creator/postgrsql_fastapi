from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    mail: str
    login: str
    password: str
    roles: str
    activity: bool
    service: str

    class Config:
        orm_mode = True


class Project(BaseModel):
    id: int
    name: str
    shortname: str
    production_type: str
    task_type: str
    task_status: str
    resolution: str
    fps: str
    colorspace: str
    root_path: str
    env_var: str
    tempplate: str
    toolkit: str
    software: str

    class Config:
        orm_mode = True
