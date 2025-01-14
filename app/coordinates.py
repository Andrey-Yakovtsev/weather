"""
Получение и обработка координат GPS
"""
from dataclasses import dataclass
from subprocess import PIPE, Popen
from typing import Literal

import config

from app.exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using MacBook GPS"""
    coordinates = _get_whereami_coordinates()
    return _round_coordinates(coordinates)


# Было      #NOSONAR
# def _get_whereami_coordinates() -> Coordinates:
#     whereami_output = _get_whereami_output()
#     coordinates = _parse_coordinates(whereami_output)
#     return coordinates
def _get_whereami_coordinates() -> Coordinates:
    coordinates = _parse_coordinates()
    return coordinates


def _get_whereami_output() -> bytes:
    """
    Вызов метода выпилен
    """
    with Popen(["whereami"], stdout=PIPE) as process:
        output, err = process.communicate()
        exit_code = process.wait()
        if err is not None or exit_code != 0:
            raise CantGetCoordinates
        return output


# Было  #NOSONAR
# def _parse_coordinates(whereami_output: bytes) -> Coordinates:
# try:
#     output = whereami_output.decode().strip().lower().split("\n")
# except UnicodeDecodeError:
#     raise CantGetCoordinates
# return Coordinates(
# latitude=_parse_coord(output, "latitude"),
# longitude=_parse_coord(output, "longitude")
# )


# Стало с хардкодными координатами
def _parse_coordinates() -> Coordinates:
    return Coordinates(latitude=25.183366, longitude=55.255616)


def _parse_coord(
    output: list[str], coord_type: Literal["latitude"] | Literal["longitude"]
) -> float:
    for line in output:
        if line.startswith(f"{coord_type}:"):
            return _parse_float_coordinate(line.split()[1])
    raise CantGetCoordinates


def _parse_float_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates  # pylint: disable=raise-missing-from


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(
        *map(lambda c: round(c, 1), [coordinates.latitude, coordinates.longitude])
    )


if __name__ == "__main__":
    print(get_gps_coordinates())
