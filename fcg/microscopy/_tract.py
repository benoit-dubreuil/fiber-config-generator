import csv
import json
import pathlib
import pickle
import typing


class Tracts(typing.TypedDict):
    x: list[float]
    y: list[float]
    t: list[float]
    id: list[int]


# TODO
def _load_fib_tracts(filename: pathlib.Path) -> Tracts:
    pass


# TODO : Load `.fib`
def load_tracts(
    filename: pathlib.Path,
    field_x: str = "x",
    field_y: str = "y",
    field_t: str = "t",
    field_id: str = "id",
    file_format: str | None = None,
) -> Tracts:
    """Load the tracts from a `.fib`, `.csv`, `.json` or `.pcl` file.

    Parameters
    ----------
    filename
        Path to a `.fib`, `.csv`, `.json` or `.pcl` filename
    field_x
        Column name in the file corresponding to the tracts X positions.
    field_y
        Column name in the file corresponding to the tracts Y positions.
    field_t
        Column name in the file corresponding to the tracts time.
    field_id
        Column name in the file corresponding to the tracts ID.
    file_format
        Specify the file format (available are fib, cvs, json, pcl). If none is given, it will be inferred from the
        filename.

    """
    tracts: Tracts = {"x": [], "y": [], "t": [], "id": []}

    if pathlib.Path(filename).suffix == ".fib" or file_format == "fib":
        tracts = _load_fib_tracts(filename)
    elif pathlib.Path(filename).suffix == ".csv" or file_format == "csv":
        # Load the csv file
        with open(filename) as csvfile:
            #  Detect the csv format
            dialect = csv.Sniffer().sniff(csvfile.read())

            #  Create a reader
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)

            for i, row in enumerate(reader):
                if i == 0:
                    column_names = row
                else:
                    tracts["x"].append(float(row[column_names.index(field_x)]))
                    tracts["y"].append(float(row[column_names.index(field_y)]))
                    tracts["t"].append(float(row[column_names.index(field_t)]))
                    tracts["id"].append(int(row[column_names.index(field_id)]))

    elif pathlib.Path(filename).suffix == ".json" or file_format == "json":
        with open(filename) as f:
            content = json.load(f)
        tracts["x"] = content[field_x]
        tracts["y"] = content[field_y]
        tracts["t"] = content[field_t]
        tracts["id"] = content[field_id]

    elif pathlib.Path(filename).suffix == ".pcl" or file_format == "pcl":
        with open(filename, "rb") as f:
            content = pickle.load(f)
        tracts["x"] = content[field_x]
        tracts["y"] = content[field_y]
        tracts["t"] = content[field_t]
        tracts["id"] = content[field_id]

    return tracts
