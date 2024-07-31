#! /Users/audrius/Documents/VCSPython/py_projmngpg/bin/python3
from tb_persons import Persons
from tb_projects import Projects
from tb_tasks import Tasks
from tb_persontask import PersonTask
from db_conn import DBEngine
from initial_data import persons_list, projects_list, tasks_list, person_task_list


def main():
    # db_conn = DBEngine()
    # db_conn.connect()
    persons_table = Persons()
    persons_table.create_table()
    projects_table = Projects()
    projects_table.create_table()
    tasks_table = Tasks()
    tasks_table.create_table()
    person_task_table = PersonTask()
    person_task_table.create_table()
    # persons_table.append_data(persons_list)
    # projects_table.append_data(projects_list)
    # tasks_table.append_data(tasks_list)
    # person_task_table.append_data(person_task_list)


if __name__ == "__main__":
    main()
