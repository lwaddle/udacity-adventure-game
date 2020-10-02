import udacity_game_controls as gc

scene_controller = gc.SceneController()
scene = scene_controller.create_scene_from_file("test_values.txt")
scene_controller.add_scene(scene)

scene_controller.print_scene(scene_controller.scenes[69])

