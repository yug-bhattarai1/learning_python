import typer

app = typer.Typer(name="learning_typer", help ="first run")

@app.command()
def greet(name: str):
    typer.echo(f"Hello {name}")

@app.command()
def goodbye(name: str):
    typer.echo(f"Goodbye {name}.")


if __name__ == "__main__":
    app()