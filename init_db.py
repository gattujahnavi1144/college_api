from connection import getSqliteConnection


def main():
    departments = [
        (1, "Computer Science"),
        (2, "Electrical Engineering"),
        (3, "Mechanical Engineering"),
        (4, "Mathematics"),
        (5, "Physics"),
    ]
    students = [
        (101, "Alice Johnson", 1),
        (102, "Bob Smith", 2),
        (103, "Carol Lee", 3),
        (104, "David Brown", 4),
        (105, "Emily White", 5),
        (106, "JAhnavi GAttu", 1),
    ]

    connection = getSqliteConnection()
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("DROP TABLE IF EXISTS students")
        connection.execute("DROP TABLE IF EXISTS departments")
        connection.execute(
            "CREATE TABLE departments ("
            "DepartmentId INTEGER PRIMARY KEY, "
            "DepartmentName TEXT NOT NULL)"
        )
        connection.execute(
            "CREATE TABLE students ("
            "StudentId INTEGER PRIMARY KEY, "
            "StudentName TEXT NOT NULL, "
            "DepartmentId INTEGER, "
            "FOREIGN KEY (DepartmentId) REFERENCES departments (DepartmentId))"
        )
        department_cursor = connection.executemany(
            "INSERT INTO departments (DepartmentId, DepartmentName) VALUES (?, ?)",
            departments,
        )
        student_cursor = connection.executemany(
            "INSERT INTO students (StudentId, StudentName, DepartmentId) "
            "VALUES (?, ?, ?)",
            students,
        )
        connection.commit()
        department_count = department_cursor.rowcount
        student_count = student_cursor.rowcount
    finally:
        connection.close()

    print(f"Inserted {department_count} rows into departments.")
    print(f"Inserted {student_count} rows into students.")


if __name__ == "__main__":
    main()