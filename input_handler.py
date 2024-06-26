import curses

import screen
import terrain


def get_input(player):
    import main
    while True:
        key = main.win.getkey().lower()
        if key == "key_home" or key == "key_a1":
            player.move(-1, -1)
            break
        if key == "key_up" or key == "key_a2":
            player.move(-1, 0)
            break
        if key == "key_ppage" or key == "key_a3":
            player.move(-1, 1)
            break
        if key == "key_left" or key == "key_b1":
            player.move(0, -1)
            break
        if key == "\n" or key == "key_b2":
            player.move(0, 0)
            break
        if key == "key_right" or key == "key_b3":
            player.move(0, 1)
            break
        if key == "key_end" or key == "key_c1":
            player.move(1, -1)
            break
        if key == "key_down" or key == "key_c2":
            player.move(1, 0)
            break
        if key == "key_npage" or key == "key_c3":
            player.move(1, 1)
            break
        if key == 'i':
            screen.show_equipment(player)
        if key == 'l':
            if main.terrain_map[player.y][player.x].char != "<" and main.terrain_map[player.y][player.x].char != ">":
                screen.update_chat(f"You are not standing on stairs.")
            elif len(main.turn_list) > 1:
                screen.update_chat(f"Clear monsters on the floor first.")

            else:
                # screen.update_chat(f"{player.y}, {player.x}")
                if main.terrain_map[player.y][player.x].name == "Upstairs to the Tower of Beginning":
                    main.terrain_map[player.y][player.x].actor = None
                    if main.terrain_map[player.y][player.x].level >= len(main.tower_of_beginning):
                        main.gain_level = True
                        main.tower_of_beginning.append(terrain.generate_terrain(50, 50, "1", main.terrain_map[player.y][player.x].level + 1))
                    main.terrain_map = main.tower_of_beginning[main.terrain_map[player.y][player.x].level]
                    for i in range(0, main.total_map_size_y - 1):
                        for j in range(0, main.total_map_size_x - 1):
                            if main.terrain_map[i][j].name == "Downstairs to the Tower of Beginning":
                                player.y = i
                                player.x = j
                                break
                    main.current_level = main.terrain_map[player.y][player.x].level
                    main.terrain_map[player.y][player.x].actor = player
                    screen.update_chat("")
                    break
                if main.terrain_map[player.y][player.x].name == "Downstairs to the Tower of Beginning":
                    main.terrain_map[player.y][player.x].actor = None
                    if main.terrain_map[player.y][player.x].level == 1:
                        main.terrain_map = main.lobby
                    else:
                        main.terrain_map = main.tower_of_beginning[main.terrain_map[player.y][player.x].level - 2]
                    for i in range(0, main.total_map_size_y - 1):
                        for j in range(0, main.total_map_size_x - 1):
                            if main.terrain_map[i][j].name == "Upstairs to the Tower of Beginning":
                                player.y = i
                                player.x = j
                                break
                    main.current_level = main.terrain_map[player.y][player.x].level
                    main.terrain_map[player.y][player.x].actor = player
                    screen.update_chat("")
                if main.terrain_map[player.y][player.x].name == "Upstairs to the Tower of Trials":
                    main.terrain_map[player.y][player.x].actor = None
                    if main.terrain_map[player.y][player.x].level >= len(main.tower_of_trials):
                        main.gain_level = True
                        main.tower_of_trials.append(terrain.generate_terrain(50, 50, "2", main.terrain_map[player.y][player.x].level + 1))
                    main.terrain_map = main.tower_of_trials[main.terrain_map[player.y][player.x].level]
                    for i in range(0, main.total_map_size_y - 1):
                        for j in range(0, main.total_map_size_x - 1):
                            if main.terrain_map[i][j].name == "Downstairs to the Tower of Trials":
                                player.y = i
                                player.x = j
                                break
                    main.current_level = main.terrain_map[player.y][player.x].level
                    main.terrain_map[player.y][player.x].actor = player
                    screen.update_chat("")
                    break
                if main.terrain_map[player.y][player.x].name == "Downstairs to the Tower of Trials":
                    main.terrain_map[player.y][player.x].actor = None
                    if main.terrain_map[player.y][player.x].level == 1:
                        main.terrain_map = main.lobby
                    else:
                        main.terrain_map = main.tower_of_trials[main.terrain_map[player.y][player.x].level - 2]
                    for i in range(0, main.total_map_size_y - 1):
                        for j in range(0, main.total_map_size_x - 1):
                            if main.terrain_map[i][j].name == "Upstairs to the Tower of Trials":
                                player.y = i
                                player.x = j
                                break
                    main.current_level = main.terrain_map[player.y][player.x].level
                    main.terrain_map[player.y][player.x].actor = player
                    screen.update_chat("")
                if main.terrain_map[player.y][player.x].name == "Upstairs to the Tower of God":
                    main.tower_of_god.append(
                        terrain.generate_terrain(50, 50, "3", main.terrain_map[player.y][player.x].level + 1))
                    main.terrain_map = main.tower_of_god[main.terrain_map[player.y][player.x].level]
                    for i in range(0, main.total_map_size_y - 1):
                        for j in range(0, main.total_map_size_x - 1):
                            if main.terrain_map[i][j].name == "Downstairs to the Tower of God":
                                player.y = i
                                player.x = j
                                break
                    main.current_level = main.terrain_map[player.y][player.x].level
                    main.terrain_map[player.y][player.x].actor = player
                    screen.update_chat("")
                    break

                break
        if key == "m":
            screen.show_all_message_log()
        if key == ',':
            if hasattr(main.terrain_map[player.y][player.x], "items") and len(main.terrain_map[player.y][player.x].items) > 0:
                screen.show_items_on_floor(player)
                break
            else:
                screen.update_chat("There are no items here.")

        if key == 'v':
            if screen.show_spells():
                break


def targetting(player, mode="single"):
    import main, screen
    screen.update_chat("")
    tmp_y = player.y
    tmp_x = player.x
    real_y = player.y
    real_x = player.x
    if tmp_y > int(main.map_height / 2):
        offset = tmp_y - int(main.map_height / 2)
        tmp_y -= offset
    if tmp_x > int(main.map_width / 2):
        offset = tmp_x - int(main.map_width / 2)
        tmp_x -= offset

    main.win.move(tmp_y, tmp_x)
    while True:
        key = main.win.getkey().lower()
        if key == "key_home" or key == "key_a1":
            if 0 <= tmp_y - 1 < main.map_height and 0 <= tmp_x - 1 < main.map_width and 0 <= real_y - 1 < main.total_map_size_y and 0 <= real_x - 1 < main.total_map_size_x:
                tmp_y -= 1
                tmp_x -= 1
                real_y -= 1
                real_x -= 1
                main.win.move(tmp_y, tmp_x)
        elif key == "key_up" or key == "key_a2":
            if 0 <= tmp_y - 1 < main.map_height and 0 <= tmp_x < main.map_width and 0 <= real_y - 1 < main.total_map_size_y and 0 <= real_x < main.total_map_size_x:
                tmp_y -= 1
                real_y -= 1
                main.win.move(tmp_y, tmp_x)
        elif key == "key_ppage" or key == "key_a3":
            if 0 <= tmp_y - 1 < main.map_height and 0 <= tmp_x + 1 < main.map_width and 0 <= real_y - 1 < main.total_map_size_y and 0 <= real_x + 1 < main.total_map_size_x:
                tmp_y -= 1
                tmp_x += 1
                real_y -= 1
                real_x += 1
                main.win.move(tmp_y, tmp_x)
        elif key == "key_left" or key == "key_b1":
            if 0 <= tmp_y < main.map_height and 0 <= tmp_x - 1 < main.map_width and 0 <= real_y < main.total_map_size_y and 0 <= real_x - 1 < main.total_map_size_x:
                tmp_x -= 1
                real_x -= 1
                main.win.move(tmp_y, tmp_x)
        elif key == "key_right" or key == "key_b3":
            if 0 <= tmp_y < main.map_height and 0 <= tmp_x + 1 < main.map_width and 0 <= real_y < main.total_map_size_y and 0 <= real_x + 1 < main.total_map_size_x:
                tmp_x += 1
                real_x += 1
                main.win.move(tmp_y, tmp_x)
        elif key == "key_end" or key == "key_c1":
            if 0 <= tmp_y + 1 < main.map_height and 0 <= tmp_x - 1 < main.map_width and 0 <= real_y + 1 < main.total_map_size_y and 0 <= real_x - 1 < main.total_map_size_x:
                tmp_y += 1
                tmp_x -= 1
                real_y += 1
                real_x -= 1
                main.win.move(tmp_y, tmp_x)
        elif key == "key_down" or key == "key_c2":
            if 0 <= tmp_y + 1 < main.map_height and 0 <= tmp_x < main.map_width and 0 <= real_y + 1 < main.total_map_size_y and 0 <= real_x < main.total_map_size_x:
                tmp_y += 1
                real_y += 1
                main.win.move(tmp_y, tmp_x)
        elif key == "key_npage" or key == "key_c3":
            if 0 <= tmp_y + 1 < main.map_height and 0 <= tmp_x + 1 < main.map_width and 0 <= real_y + 1 < main.total_map_size_y and 0 <= real_x + 1 < main.total_map_size_x:
                tmp_y += 1
                tmp_x += 1
                real_y += 1
                real_x += 1
                main.win.move(tmp_y, tmp_x)
        elif key == '\n' or key == "key_b2":
            match mode:
                case "single":
                    if main.terrain_map[real_y][real_x].actor is not None:
                        return main.terrain_map[real_y][real_x].actor
                    else:
                        screen.update_chat("You didn't target enemy.")
                        break
                case "aoe":
                    actors_list = []
                    for i in range(real_y - 1, real_y + 1):
                        for j in range(real_x - 1, real_x + 1):
                            if 0 < real_y < main.total_map_size_y and 0 < real_x < main.total_map_size_x:
                                if main.terrain_map[i][j].actor is not None:
                                    actors_list.append(main.terrain_map[i][j].actor)
                    return actors_list
                case "wall":
                    if main.terrain_map[real_y][real_x].destructible is True:
                        return real_y, real_x


        else:
            screen.update_chat("")
            break
