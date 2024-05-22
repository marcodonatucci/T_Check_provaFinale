from dataclasses import dataclass
import flet as ft


@dataclass
class Device:
    uid: str
    itemId: int
    name: str
    position: (float, float)
    device_status: bool
    object_status: bool
    selected_type: str

    def defineStatus(self, boolean):
        if boolean == 1:
            return "On"
        else:
            return "Off"

    def __str__(self):
        return (f"Dati dispositivo:\n"
                f"IMEI: {self.uid}\n"
                f"Nome: {self.name}\n"
                f"Status: {self.defineStatus(self.device_status)}\n"
                f"Posizione: {self.position}\n"
                f"Accensione: {self.defineStatus(self.object_status)}\n")

    def displayData(self):
        rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("IMEI", weight=ft.FontWeight.W_400)),
                    ft.DataCell(ft.Text(self.uid))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("nome", weight=ft.FontWeight.W_400)),
                    ft.DataCell(ft.Text(self.name))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Status dispositivo", weight=ft.FontWeight.W_400)),
                    ft.DataCell(ft.Text(self.defineStatus(self.device_status)))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Posizione", weight=ft.FontWeight.W_400)),
                    ft.DataCell(ft.Text(self.position))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Accensione", weight=ft.FontWeight.W_400)),
                    ft.DataCell(ft.Text(self.defineStatus(self.object_status)))
                ]
            )
        ]
        return rows
