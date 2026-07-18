from loader import Loader

from validator import Validator

from formatter import Formatter

from exporter import Exporter

from report import summary

document = Loader().load()

valid = Validator().validate(

    document

)

if valid:

    formatted = Formatter().format(

        document

    )

    Exporter().save(

        formatted

    )

summary(valid)
