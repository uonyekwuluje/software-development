#!/usr/bin/env python3
import click

@click.group(invoke_without_command=True, chain=True)
def cli():
    pass

def add_number(x,y):
    psum = int(x) + int(y)
    print(f"The sum of {x} + {y} = {psum}")


@cli.command()
@click.option('-x', '--input_one', help="First Input")
@click.option('-y', '--input_two', help="Second Input")
def get_values(input_one, input_two):
    add_number(input_one, input_two)



if __name__ == '__main__':
    cli()
