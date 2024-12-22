#!/usr/bin/env python3
import click

from . import gpg_subkey_generator


@click.group()
@click.version_option(version="0.1.0")
def main():
    click.echo("Hello, World!")


@main.command()
def generate_subkey():
    gpg_subkey_generator.generate_subkey()


if __name__ == "__main__":
    main()
