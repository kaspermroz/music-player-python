from src.internal.app.interfaces.command_handler import CommandHandler


class SayHiHandler(CommandHandler):
    def HandlerName(self) -> str:
        return "SayHi"

    def Handle(self):
        return "hi"
