from dataclasses import dataclass

from Model.device import Device
import flet as ft


@dataclass
class Device6(Device):
    uid: str
    itemId: int
    name: str
    position: (float, float)
    device_status: bool
    object_status: bool
    battery: float
    total_km: float
    selected_type: str

    def __str__(self):
        return super().__str__() + (f"Batteria: {self.battery} V\n"
                                    f"Km totali: {self.total_km} km")

    def displayData(self):
        rows = super().displayData()
        rows.extend(
            [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Batteria", weight=ft.FontWeight.W_400)),
                        ft.DataCell(ft.Text(str(self.battery) + "V"))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Km totali", weight=ft.FontWeight.W_400)),
                        ft.DataCell(ft.Text(str(self.total_km) + "Km"))
                    ]
                )
            ]
        )
        return rows
