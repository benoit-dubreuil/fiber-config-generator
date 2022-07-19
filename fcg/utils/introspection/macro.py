import enum
import typing


class _AutoMacroFromName(str, enum.Enum):

    @staticmethod
    @typing.final
    def _generate_next_value_(name: str, start, count, last_values) -> str:
        __AFFIX: typing.Final[str] = '__'
        return __AFFIX + name.lower() + __AFFIX


@typing.final
@enum.unique
class Macro(_AutoMacroFromName):
    ALL = enum.auto()
    DICT = enum.auto()
    MAIN = enum.auto()
    NAME = enum.auto()
    QUALNAME = enum.auto()


Macro.ALL.TAlias_Macro_All = list[str]
