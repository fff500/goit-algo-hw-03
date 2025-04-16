import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('source_dir', type=str, help='Джерело для копіювання')
parser.add_argument('--destination_dir', type=str, default='dist', help='Куди копіювати (за замовчуванням dist)')

def copy_files():
    args = parser.parse_args()

    def traverse_folder(path):
      if path.is_dir():
          for child in path.iterdir():
              traverse_folder(child)

      if path.is_file():
          type_folder_name = path.suffix[1:]
          type_folder_path = Path(f"{args.destination_dir}/{type_folder_name}")
          type_folder_path.mkdir(parents=True, exist_ok=True)
          shutil.copy(path, type_folder_path)

    try:
        source_dir_path = Path(args.source_dir)
        dest_dir_path = Path(args.destination_dir)
        dest_dir_path.mkdir(exist_ok=True)

        traverse_folder(source_dir_path)
    except FileNotFoundError:
        return "Не вдалося знайти файл з даними"
    except PermissionError:
        return "Немає доступу до файлу"

if __name__ == "__main__":
    copy_files()
