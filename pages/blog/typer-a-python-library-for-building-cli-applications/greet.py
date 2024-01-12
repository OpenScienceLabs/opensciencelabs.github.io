
import typer

app = typer.Typer()

@app.command()
def greet(
    name: str = typer.Option(
        ..., 
        "--name",
        help="The name of the person to greet."
    )
) -> None:
    """Greets the user by name."""
    typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()
