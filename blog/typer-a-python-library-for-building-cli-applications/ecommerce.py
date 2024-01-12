import typer

from typer import Context, Option


app = typer.Typer(help="Operations for e-commerce.")
app_user = typer.Typer(help="Operations for user model.")
app_product = typer.Typer(help="Operations for product model.")

app.add_typer(app_user, name="user")
app.add_typer(app_product, name="product")

@app.callback(invoke_without_command=True)
def main(
    ctx: Context,
    version: bool = Option(
        None,
        "--version",
        "-v",
        is_flag=True,
        help="Show the version and exit.",
    ),
) -> None:
    """Process envers for specific flags, otherwise show the help menu."""
    if version:
        __version__ = "0.1.0"
        typer.echo(f"Version: {__version__}")
        raise typer.Exit()

    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit(0)

@app_user.command("create")
def user_create(name: str = typer.Argument(..., help="Name of the user to create.")) -> None:
    """Create a new user with the given name."""
    print(f"Creating user: {name} - Done")


@app_user.command("update")
def user_update(name: str = typer.Argument(..., help="Name of the user to update.")) -> None:
    """Update user data with the given name."""
    print(f"Updating user: {name} - Done")

@app_product.command("create")
def product_create(name: str = typer.Argument(..., help="Name of the product to create.")) -> None:
    """Create a new product with the given name."""
    print(f"Creating product: {name} - Done")


@app_product.command("update")
def product_update(name: str = typer.Argument(..., help="Name of the product to update.")) -> None:
    """Update a product with the given name."""
    print(f"Updating product: {name} - Done")


if __name__ == "__main__":
    app()
