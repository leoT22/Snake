import cx_Freeze

executables = [cx_Freeze.Executable('snake.py')]

cx_Freeze.setup(
    name="Snake game",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['assets']}},

    executables = executables
    
)