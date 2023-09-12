import subprocess

def compile_to_exe(source_file):
    try:
        subprocess.run(['pyinstaller', '--onefile', source_file], check=True)
        print(f"Код успешно скомпилирован в {source_file[:-3]}.exe")
    except Exception as e:
        print(f"Произошла ошибка при компиляции: {e}")

if __name__ == "__main__":
    source_file = input("Введите имя исходного файла (без .py расширения): ") + ".py"
    compile_to_exe(source_file)