from rich.console import Console
import yaml

from core.state import SystemState
from core.daemon import REMADaemon
from agents.ema.agent import EMAAgent

console = Console()


def load_yaml(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)


system_config = load_yaml("configs/system.yaml")
ema_config = load_yaml("configs/ema.yaml")

console.print(
    f"[bold cyan]{system_config['system']['organization']}[/bold cyan]"
)

console.print(
    f"[cyan]{system_config['system']['project']}[/cyan]"
)

console.print(
    f"[white]Version {system_config['system']['version']}[/white]\n"
)

state = SystemState()

daemon = REMADaemon(state)
daemon.boot()

ema = EMAAgent(ema_config, state)
ema.initialize()

state.set_agent("EMA")

console.print(
    f"\n[bold green]ACTIVE AGENT:[/bold green] {state.active_agent}"
)

console.print(
    "\n[bold cyan]Interactive Runtime Started[/bold cyan]"
)

running = True

while running:
    command = input("\nEMA > ")

    running = ema.process_command(command)

console.print(
    "\n[bold red]REMA Protocol terminated[/bold red]"
)