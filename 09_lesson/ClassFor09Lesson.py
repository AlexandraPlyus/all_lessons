from sqlalchemy import create_engine, text


class Tables:

    def __init__(self, db_connection_string):
        self.connection_string = db_connection_string

    def connection(self):
        self.connection_string
        self.engine = create_engine(self.connection_string)
        self.connection = self.engine.connect()

    def get_max_id(self) -> int:
        self.max_id = self.connection.execute(
            text("SELECT MAX(teacher_id) as max_id FROM teacher")
        ).fetchone()[0]
        return self.max_id

    def add_teacher(self, id_new_teacher, email, group_id):
        self.connection.execute(
            text(
                "INSERT INTO teacher " +
                "(teacher_id, email, group_id) " +
                "VALUES (:id, :email, :group_id)"
            ),
            {"id": id_new_teacher, "email": email, "group_id": group_id},
        )
        self.connection.commit()

    def check_add_teacher(self, id_new_teacher):
        self.teacher = self.connection.execute(
            text("SELECT * FROM teacher WHERE teacher_id = :id"),
            {"id": id_new_teacher},
        ).fetchone()
        return self.teacher

    def delete_new_teacher(self, email):
        self.connection.execute(
            text("DELETE FROM teacher WHERE email = :email"), {"email": email}
        )
        self.connection.commit()
        self.connection.close()
        self.engine.dispose()

    def change_teacher_information(
        self, change_id_new_teacher, change_email, change_group_id
    ):
        self.connection.execute(
            text(
                "INSERT INTO teacher " +
                "(teacher_id, email, group_id) " +
                "VALUES (:id, :email, :group_id)"
            ),
            {
                "id": change_id_new_teacher,
                "email": change_email,
                "group_id": change_group_id,
            },
        )
        self.connection.commit()

    def check_change_teacher(self, id_change_teacher):
        self.teacher = self.connection.execute(
            text("SELECT * FROM teacher WHERE teacher_id = :id"),
            {"id": id_change_teacher},
        ).fetchone()
        return self.teacher

    def delete_change_teacher(self, change_email):
        self.connection.execute(
            text("DELETE FROM teacher WHERE email = :email"),
            {"email": change_email},
        )
        self.connection.commit()
        self.connection.close()
        self.engine.dispose()
