from ClassFor09Lesson import Tables

db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"


# Тест на добавление учителя
def test_add_teacher():

    # Подключение
    tables_exemplar = Tables(db_connection_string)
    tables_exemplar.connection()

    try:
        # Узнаём наибольшее значение id, берём +1
        max_id = tables_exemplar.get_max_id()
        id_new_teacher = max_id + 1

        # Добавляем учителя
        email = "test@school.com"
        group_id = 1
        tables_exemplar.add_teacher(id_new_teacher, email, group_id)

        # Проверяем, что учитель добавлен
        new_teacher = tables_exemplar.check_add_teacher(id_new_teacher)
        assert new_teacher.email == email

    finally:
        # Очищаем, закрываем
        tables_exemplar.delete_new_teacher(email)


# Тест на изменение данных учителя
def test_change_teacher_information():

    # Подключение
    tables_exemplar = Tables(db_connection_string)
    tables_exemplar.connection()

    try:
        # Узнаём наибольшее значение id, берём +1
        max_id = tables_exemplar.get_max_id()
        id_new_teacher = max_id + 1

        # Добавляем учителя
        email = "test@school.com"
        group_id = 1
        tables_exemplar.add_teacher(id_new_teacher, email, group_id)

        # Проверяем, что учитель добавлен
        new_teacher = tables_exemplar.check_add_teacher(id_new_teacher)
        assert new_teacher.email == email

        # Меняем данные учителя
        change_id_new_teacher = id_new_teacher + 1
        change_email = "changetest@school.com"
        change_group_id = 1 + 1
        tables_exemplar.change_teacher_information(
            change_id_new_teacher, change_email, change_group_id
        )

        # Проверяем, что данные изменились
        change_teacher = tables_exemplar.check_change_teacher(
            change_id_new_teacher
        )
        assert change_teacher.email == change_email

    finally:
        # Очищаем, закрываем
        tables_exemplar.delete_change_teacher(change_email)


# Тест на удаление учителя
def test_delete_teacher():

    # Подключение
    tables_exemplar = Tables(db_connection_string)
    tables_exemplar.connection()

    try:
        # Узнаём наибольшее значение id, берём +1
        max_id = tables_exemplar.get_max_id()
        id_new_teacher = max_id + 1

        # Добавляем учителя
        email = "test@school.com"
        group_id = 1
        tables_exemplar.add_teacher(id_new_teacher, email, group_id)

        # Проверяем, что учитель добавлен
        new_teacher = tables_exemplar.check_add_teacher(id_new_teacher)
        assert new_teacher.email == email

    finally:
        # Удаляем созданного учителя, проверяем отсутствие
        tables_exemplar.delete_new_teacher(email)
        if new_teacher.email is None:
            pass
