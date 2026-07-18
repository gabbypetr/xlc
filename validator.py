import json


class Validator:

    def validate(
        self,
        document
    ):

        try:

            json.loads(

                document.text

            )

            return True

        except json.JSONDecodeError:

            return False
