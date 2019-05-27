# puput

Puput is a tool to manage PR and PA

## Installation

You can install it using `pip install` as usual:
```bash
pip install puput
```

## Usage

Puput is intended to be used as a command:
```bash
$ puput <RSS URL>
```

The option `--to-date` limits the output to entries published in the last 24h:
```bash
$ puput --to-date <RSS URL>
```

The option `--title-starts` allows to specify a string the title must start with to be accepted:
```bash
$ puput --title-starts 'Hello' <RSS URL>
```

The option `--format` allows to specify a string, using Jinja2 templating system, to format the output based on the entry data:
```bash
$ puput --format '{{title}} {{link}}' <RSS URL>
```

## Example

This is how puput is used to tweet job offers sent to the PyBCN mailing list, which is published as RSS:
```bash
$ puput <RSS URL> --to-date --title-starts 'Job Offer' --format '#pybcn #jobs {{title[11:]}} {{link}}'
```
