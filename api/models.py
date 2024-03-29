from typing import Any

class ClassEntity:

    def _init_(self, classname, details,
                 time, status, reserved_time) -> None:
        self.classname = classname
        self.details = details
        self.time = time
        self.status = status
        self.reserved_time = reserved_time

    def _str_(self) -> str:
        return self.classname
    
    def _getattribute_(self, __name: str) -> Any:
        if (__name=='time' or __name=='reserved_time'):
            return object._getattribute_(self, __name).strftime("%H:%M")
        else:
            return object._getattribute_(self, __name)