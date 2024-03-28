from typing import Any

class ClassEntity:

    def __init__(self, classname, details,
                 time, status) -> None:
        self.classname = classname
        self.details = details
        self.time = time
        self.status = status

    def __str__(self) -> str:
        return self.classname
    
    def __getattribute__(self, __name: str) -> Any:
        if (__name=='time'):
            return object.__getattribute__(self, __name).strftime("%d/%m/%Y %H:%M:%S")
        else:
            return object.__getattribute__(self, __name)
        