from typing import List

from fastapi import Depends, HTTPException, status

from .. import app
from ..models import schemas


@app.get("/")
def hello_world():
    return "ABC"
