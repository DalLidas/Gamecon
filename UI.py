import dearpygui.dearpygui as dpg

from DataClasses import *

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=1280, height=720)

UnitsData = Units.from_dict({})
BaseData = Base.from_dict({})
EnemyBlockdata = EnemyBlock.from_dict({})
ZombieData = Zombie.from_dict({})


def getData(worldData, unitsData):
    global UnitsData
    global BaseData
    global EnemyBlockdata
    global ZombieData

    data = unitsData
    UnitsData = Units.from_dict(data)
    BaseData = [Base.from_dict(y) for y in data["base"]]
    EnemyBlockdata = [EnemyBlock.from_dict(y) for y in data["enemyBlocks"]]
    ZombieData = [Zombie.from_dict(y) for y in data["zombies"]]

    print(data)


# Чтение данных из JSON файла


# Функция для отрисовки клетки
def draw_cell(x, y, color):
    points = [[x, y], [x + 50, y], [x + 50, y + 50], [x, y + 50]]
    dpg.draw_polygon(points, color=color, fill=color)


# Создание окна
with dpg.window(label="Main Window", width=1280, height=720):
    # Отрисовка базы
    for base_data in BaseData:
        # head - yellow
        draw_cell(base_data.x * 50, base_data.y * 50, [255, 255, 0])
        # base - blue
        draw_cell((base_data.x - base_data.range) * 50, (base_data.y - base_data.range) * 50,
                  [16, 123, 185])

        # Отрисовка зомби
    for zombie in ZombieData:
        if zombie.type == "bomber":
            draw_cell(zombie.x * 50, zombie.y * 50, [255, 0, 0])
        if zombie.type == "liner":
            draw_cell(zombie.x * 50, zombie.y * 50, [255, 0, 213])
        if zombie.type == "fast":
            draw_cell(zombie.x * 50, zombie.y * 50, [94, 0, 255])
        if zombie.type == "normal":
            draw_cell(zombie.x * 50, zombie.y * 50, [159, 18, 18])
        if zombie.type == "juggernaut":
            draw_cell(zombie.x * 50, zombie.y * 50, [92, 85, 142])
        if zombie.type == "chaos_knight":
            draw_cell(zombie.x * 50, zombie.y * 50, [255, 84, 204])

    # Отрисовка блоков врага
    for enemy_block_data in EnemyBlockdata:
        color = [255, 145, 0] if enemy_block_data.attack == 40 else [255, 255,
                                                                     255]
        draw_cell(enemy_block_data.x * 50, enemy_block_data.y * 50, color)

# Запуск GUI
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
