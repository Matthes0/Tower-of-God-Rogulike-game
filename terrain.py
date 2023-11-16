def generate_terrain(y, x):
    map_list = [[0] * x for i in range(0, y)]
    for i in range(0, y):
        for j in range(0, x):
            if i == 0 or i == y - 1 or j == 0 or j == x - 1:
                map_list[i][j] = IndestructibleWall(i, j)
            else:
                map_list[i][j] = Floor(i, j)
    return map_list


def place_actor(actor):
    import main, screen
    main.terrain_map[actor.y][actor.x].actor = actor
    screen.update_terrain()


def delete_actor(y, x):
    import main, screen
    main.terrain_map[y][x].actor = None
    screen.update_terrain()


def place_item(item):
    import main, screen
    main.terrain_map[item.y][item.x].items.append(item)
    screen.update_terrain()


def delete_item(y, x):
    import main, screen
    main.terrain_map[y][x].items.pop()
    screen.update_terrain()


class Terrain:
    def __init__(self, y, x, name, char, passable, actor=None, items=None):
        if items is None:
            items = list()
        self.x = x
        self.y = y
        self.name = name
        self.char = char
        self.passable = passable
        self.actor = actor
        self.items = items


class DestructibleWall(Terrain):

    def __init__(self, y, x):
        super().__init__(y, x, "Destructible Wall", "#", False)


class IndestructibleWall(Terrain):
    def __init__(self, y, x):
        super().__init__(y, x, "Indestructible Wall", "#", False)


class Floor(Terrain):
    def __init__(self, y, x):
        super().__init__(y, x, "Floor", ".", True)


class Door(Terrain):
    def __init__(self, y, x, open=False):
        super().__init__(y, x, "Door", "D", True)
        self.open = open
