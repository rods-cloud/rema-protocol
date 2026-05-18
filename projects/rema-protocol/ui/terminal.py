from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()


def load_ascii(path):
    with open(path, "r") as file:
        return file.read()


def render_agent(agent_name, state):
    ascii_path = f"assets/ascii/{agent_name.lower()}/{state.lower()}.txt"

    try:
        avatar = load_ascii(ascii_path)

    except FileNotFoundError:
        avatar = "[ASCII NOT FOUND]"

    panel = Panel(
        Align.center(avatar),
        title=f"{agent_name.upper()} // {state.upper()}",
        border_style="cyan",
        padding=(1, 4)
    )

    console.print(panel)