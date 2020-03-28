import os

import click

from demo import version
from demo.command.download.main import download_file
from demo.command.size.main import get_size


@click.group()
@click.version_option(version=version.version())
def cli():
    """demo's command line interface."""


@cli.command()
@click.option("--url", help="URL of the stuff to download.", required=True)
@click.option("--name", help="Local name of downloaded stuff.")
@click.option(
    "--destination",
    default=".",
    help="Where to download stuff. Defaults to current dir.",
)
def download(
    url, name, destination,
):
    """Download stuff.

    Examples:

        Download stuff to current dir:

            demo download --url https://example.com/foo

        Download stuff to specific dir:

            demo download --url https://example.com/foo --destination /local/path
    """
    download_file(url, name, destination)


@cli.command()
@click.option("--url", help="URL of the stuff to find out size of.", required=True)
def size(url):
    """Get the size of stuff.

    Examples:

        Get the size:

            demo size --url https://example.com/foo
    """
    get_size(url)


if __name__ == "__main__":
    cli()
