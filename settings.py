class Settings:
        w = 30
        h = 16.875
        w1 = 20
        h1 = 14
        i = 2
        tile_w = 32 * i
        tile_h = 32 * i
        small_tile_w = tile_w - 2
        small_tile_h = tile_h - 2
        field_size = (w1 * tile_w, h1 * tile_h)
        start_field_size = (w1 * tile_w, h1 * tile_h)
        start_button_size = (300, 300)
        name_button_size = (600, 600)
        button_for_text_size = (500, 250)
        resolution = (w * tile_w, h * tile_h)
        information_field_size = (198 * i, 448 * i)
        score_field_size = (198 * i, 106 * i)
        records_field_size = (198 * i, 327 * i)

        restart_button_size = (90 * i, 60 * i)
        quit_button_size = (90 * i, 60 * i)
        game_over_field_size = (w1 * tile_w - 100, h1 * tile_h - 50)
        fps = 60
        speed = 10

