# src/best_practices/console.py
import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
	"""The hypermoden Python Project"""
	click.echo("Hello, World!")

	
