#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_player():
    return {"message": "Player endpoint"}