# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from datetime import datetime
from typing import Any, Optional

from sqlalchemy import types

from superset.db_engine_specs.base import BaseEngineSpec


class DynamoDBEngineSpec(BaseEngineSpec):
    engine = "dynamodb"
    engine_name = "Amazon DynamoDB"

    _time_grain_expressions = {
        None: "{col}",
        "PT1S": "DATETIME(STRFTIME('%Y-%m-%dT%H:%M:%S', {col}))",
        "PT1M": "DATETIME(STRFTIME('%Y-%m-%dT%H:%M:00', {col}))",
        "PT1H": "DATETIME(STRFTIME('%Y-%m-%dT%H:00:00', {col}))",
        "P1D": "DATETIME({col}, 'start of day')",
        "P1W": "DATETIME({col}, 'start of day', -strftime('%w', {col}) || ' days')",
        "P1M": "DATETIME({col}, 'start of month')",
        "P3M": (
            "DATETIME({col}, 'start of month', "
            "printf('-%d month', (strftime('%m', {col}) - 1) % 3))"
        ),
        "P1Y": "DATETIME({col}, 'start of year')",
        "P1W/1970-01-03T00:00:00Z": "DATETIME({col}, 'start of day', 'weekday 6')",
        "P1W/1970-01-04T00:00:00Z": "DATETIME({col}, 'start of day', 'weekday 0')",
        "1969-12-28T00:00:00Z/P1W": (
            "DATETIME({col}, 'start of day', 'weekday 0', '-7 days')"
        ),
        "1969-12-29T00:00:00Z/P1W": (
            "DATETIME({col}, 'start of day', 'weekday 1', '-7 days')"
        ),
    }

    @classmethod
    def epoch_to_dttm(cls) -> str:
        return "datetime({col}, 'unixepoch')"

    @classmethod
    def convert_dttm(
        cls, target_type: str, dttm: datetime, db_extra: Optional[dict[str, Any]] = None
    ) -> Optional[str]:
        sqla_type = cls.get_sqla_column_type(target_type)

        if isinstance(sqla_type, (types.String, types.DateTime)):
            return f"""'{dttm.isoformat(sep=" ", timespec="seconds")}'"""

        return None
