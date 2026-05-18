from rich.console import Console
from ui.terminal import render_agent

console = Console()


class EMAAgent:
    def __init__(self, config, state):
        self.config = config
        self.state = state

    def initialize(self):
        render_agent("ema", "idle")

        console.print(
            f"[cyan]{self.config['agent']['name']}[/cyan]"
        )

    def process_command(self, command):
        command = command.lower()

        if command == "help":
            self.show_help()

        elif command == "status":
            self.show_status()

        elif command == "sleep":
            self.sleep()

        elif command == "wake":
            self.wake()

        elif command == "exit":
            return False

        else:
            console.print(
                "[red]Unknown command[/red]"
            )

        return True

    def show_help(self):
        console.print("\n[bold cyan]AVAILABLE COMMANDS[/bold cyan]")

        console.print("help    - show commands")
        console.print("status  - current state")
        console.print("sleep   - sleep EMA")
        console.print("wake    - wake EMA")
        console.print("exit    - close REMA")

    def show_status(self):
        console.print(
            f"\n[green]ACTIVE AGENT:[/green] {self.state.get_agent()}"
        )

        console.print(
            f"[green]STATUS:[/green] {self.state.get_status()}"
        )

    def sleep(self):
        self.state.set_status("SLEEPING")
        render_agent("ema", "sleep")

        console.print(
            "\n[yellow]EMA entering sleep mode...[/yellow]"
        )

    def wake(self):
        self.state.set_status("ONLINE")
        render_agent("ema", "idle")

        console.print(
            "\n[cyan]EMA awakened[/cyan]"
        )