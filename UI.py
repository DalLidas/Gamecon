import json

import dearpygui.dearpygui as dpg

from DataClasses import *


class UI():
    def __init__(self, title='Main Window', width=1280, height=720):
        self.title = title
        self.width = width
        self.height = height

        self.UnitsData = Units
        self.BaseData = Base
        self.EnemyBlockdata = EnemyBlock
        self.ZombieData = Zombie

        dpg.create_context()
        dpg.create_viewport(title=self.title, width=self.width, height=self.height)

    def __del__(self):
        dpg.destroy_context()

    def Update(self, unitsData, worldata):
        self.UnitsData = Units.from_dict(unitsData)
        self.BaseData = [Base.from_dict(y) for y in unitsData["base"]]
        self.EnemyBlockdata = [EnemyBlock.from_dict(y) for y in unitsData["enemyBlocks"]]
        self.ZombieData = [Zombie.from_dict(y) for y in unitsData["zombies"]]

        # Создание окна
        with dpg.window(label="self.title", width=1280, height=720):
            # Отрисовка базы
            for base_data in self.BaseData:
                # head - yellow
                self.draw_cell(base_data.x * 50, base_data.y * 50, [255, 255, 0])
                # base - blue
                self.draw_cell((base_data.x - base_data.range) * 50, (base_data.y - base_data.range) * 50,
                               [16, 123, 185])

            # Отрисовка зомби
            for zombie in self.ZombieData:
                if zombie.type == "bomber":
                    self.draw_cell(zombie.x * 50, zombie.y * 50, [255, 0, 0])
                if zombie.type == "liner":
                    self.draw_cell(zombie.x * 50, zombie.y * 50, [255, 0, 213])
                if zombie.type == "fast":
                    self.draw_cell(zombie.x * 50, zombie.y * 50, [94, 0, 255])
                if zombie.type == "normal":
                    self.draw_cell(zombie.x * 50, zombie.y * 50, [159, 18, 18])
                if zombie.type == "juggernaut":
                    self.draw_cell(zombie.x * 50, zombie.y * 50, [92, 85, 142])
                if zombie.type == "chaos_knight":
                    self.draw_cell(zombie.x * 50, zombie.y * 50, [255, 84, 204])

            # Отрисовка блоков врага
            for enemy_block_data in self.EnemyBlockdata:
                color = [255, 145, 0] if enemy_block_data.attack == 40 else [255, 255, 255]
                self.draw_cell(enemy_block_data.x * 50, enemy_block_data.y * 50, color)

        # Запуск GUI
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    # Функция для отрисовки клетки
    def draw_cell(self, x, y, color):
        points = [[x, y], [x + 50, y], [x + 50, y + 50], [x, y + 50]]
        dpg.draw_polygon(points, color=color, fill=color)


if __name__ == "__main__":
    with open('data.json') as file:
        data = json.load(file)
        ui = UI()
        ui.Update(data, {})


