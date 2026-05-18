from rich.console import Console

console = Console()


class REMADaemon:
    def __init__(self, state):
        self.state = state

    def boot(self):
        console.print(
            "[bold cyan]Initializing REMA Protocol...[/bold cyan]"
        )

        self.state.set_status("ONLINE")

        console.print(
            "[bold green]System Ready[/bold green]"
        )