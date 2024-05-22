from dataclasses import dataclass

from Model.device import Device
import flet as ft


@dataclass
class Device9(Device):
    uid: str
    itemId: int
    name: str
    position: (float, float)
    device_status: bool
    object_status: bool
    battery: float
    rpm: float
    fuel_percentage: float
    total_km: float
    water_temp: float
    driver_id: str
    selected_type: str

    def __str__(self):
        return super().__str__() + (f"Batteria: {self.battery} V\n"
                                    f"Giri motore: {self.rpm} rpm\n"
                                    f"Percentuale carburante: {self.fuel_percentage}%\n"
                                    f"Km totali: {self.total_km} km\n"
                                    f"Temperatura acqua motore: {self.water_temp} °C\n"
                                    f"Tessera autista: {self.driver_id}")

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
                        ft.DataCell(ft.Text("Giri motore", weight=ft.FontWeight.W_400)),
                        ft.DataCell(ft.Text(str(self.rpm) + "rpm"))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Percentuale carburante", weight=ft.FontWeight.W_400)),
                        ft.DataCell(ft.Text(str(self.fuel_percentage) + "%"))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Km totali", weight=ft.FontWeight.W_400)),
                        ft.DataCell(ft.Text(str(self.total_km) + "Km"))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Temperatura acqua motore", weight=ft.FontWeight.W_400)),
                        ft.DataCell(ft.Text(str(self.water_temp) + "°C"))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Tessera autista", weight=ft.FontWeight.W_400)),
                        ft.DataCell(ft.Text(self.driver_id))
                    ]
                )
            ]
        )
        return rows
