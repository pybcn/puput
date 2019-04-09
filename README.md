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
