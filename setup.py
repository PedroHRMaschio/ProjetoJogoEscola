import cx_Freeze

executables = [cx_Freeze.Executable(
    script="main.py", icon="assets/icon.ico")]
cx_Freeze.setup(
    name="Jogo Tire notas boas (A e B)",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]}},
    executables=executables
)