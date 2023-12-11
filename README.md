# Beautify-Markdown-Table
This Python script beautifies a GitHub markdown table by filling with whitespaces and making it easier to read using Python.

## Usage
To run the application, use the following command, inputting the file to be edited:
```sh
python beautify.py 'README.md'
```

## Example
While the 2 tables are displayed the same on GitHub, the normal text formats are different.
Note that tables require 1 empty line above and below it (2 below it if is end of file).

```
| Fruit | Color | Description |
| --- | --- | --- |
| Apple | Red | Crunchy |
| Orange | Orange | Sour |
| Grape | Purple | Small |
```

```
| Fruit  | Color  | Description |
| ------ | ------ | ----------- |
| Apple  | Red    | Crunchy     |
| Orange | Orange | Sour        |
| Grape  | Purple | Small       |
```

| Fruit | Color | Description |
| --- | --- | --- |
| Apple | Red | Crunchy |
| Orange | Orange | Sour |
| Grape | Purple | Small |
