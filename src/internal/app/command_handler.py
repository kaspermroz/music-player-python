"""
CommandHandler is an abstract class which enforces command interface
"""
class CommandHandler:
    def HandlerName(self) -> str:
        return NotImplementedError()
    def Handle(self):
        return NotImplementedError()