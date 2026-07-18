import json

from settings import (
    INDENT,
    SORT_KEYS
)


class Formatter:

    def format(
        self,
        document
    ):

        data = json.loads(

            document.text

        )

        return json.dumps(

            data,

            indent=INDENT,

            sort_keys=SORT_KEYS

        )
