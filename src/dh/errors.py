"""Typed failures and their exit codes."""

EXIT_OK = 0
EXIT_INVALID = 1
EXIT_USAGE = 2
EXIT_NOT_FOUND = 3
EXIT_CONFLICT = 4
EXIT_INTERNAL = 5


class DhError(Exception):
    """Base for every failure the CLI reports as JSON rather than a traceback."""

    exit_code = EXIT_INTERNAL
    code = "INTERNAL"

    def __init__(self, message, hint=None):
        super().__init__(message)
        self.message = message
        self.hint = hint

    def as_dict(self):
        out = {"code": self.code, "message": self.message}
        if self.hint:
            out["hint"] = self.hint
        return out


class UsageError(DhError):
    exit_code = EXIT_USAGE
    code = "USAGE"


class NotFound(DhError):
    exit_code = EXIT_NOT_FOUND
    code = "NOT_FOUND"


class Conflict(DhError):
    exit_code = EXIT_CONFLICT
    code = "CONFLICT"


class ModelError(DhError):
    """A malformed contract, an unresolvable range, a broken bootstrap."""

    exit_code = EXIT_INVALID
    code = "MODEL"
