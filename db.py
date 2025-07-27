import json
from utils import get_timestamp

class DB:
    def __init__(self, name):
        self.__name = name

        self.__file_path = f"db/{self.__name}.json"

        try:
            with open(self.__file_path, 'r') as file:
                self.__data = json.load(file)
        except FileNotFoundError:
            self.__data = []
            self.__save()
        
        self.__last_id = max(row['id'] for row in self.__data) if len(self.__data) > 0 else 0


    def __save(self):
        with open(self.__file_path, 'w') as file:
            json.dump(self.__data, file, indent=4)


    def add(self, row):
        self.__last_id += 1
        row['id'] = self.__last_id
        row['is_deleted'] = False

        timestamp = get_timestamp()
        row['created_at'] = timestamp
        row['updated_at'] = timestamp

        self.__data.append(row)
        self.__save()
    

    def get_all(self):
        return [row for row in self.__data if not row.get('is_deleted', False)]
    

    def get_by_id(self, row_id):
        for row in self.__data:
            if row['id'] == row_id and not row.get('is_deleted', False):
                return row
        return None

    
    def update(self, row_id, updated_row):
        for index, row in enumerate(self.__data):
            if row['id'] == row_id:
                self.__data[index] = {**row, **updated_row, "updated_at": get_timestamp()}
                self.__save()
                return True

        return False


    def delete(self, row_id):
        self.update(row_id, { "is_deleted": True })
        self.__save()


class TasksDB(DB):
    def __init__(self):
        super().__init__('tasks')


class ProjectsDB(DB):
    def __init__(self):
        super().__init__('projects')