# 建立migration資料檔

## python manage.py makemigrations

## 錯誤訊息：

Traceback (most recent call last):
File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/base/base.py", line 216, in ensure_connection self.connect()

File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/base/base.py", line 194, in connect self.connection = self.get_new_connection(conn_params)

File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/mysql/base.py", line 236, in get_new_connection return Database.connect(**conn_params)

File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/MySQLdb/__init__.py", line 86, in Connect return Connection(*args, **kwargs)
  
File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/MySQLdb/connections.py", line 204, in __init__super(Connection, self).__init__(*args, **kwargs2)

## _mysql_exceptions.OperationalError: (2002, "Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 15, in <module>
    execute_from_command_line(sys.argv)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/core/management/__init__.py", line 371, in execute_from_command_line
    utility.execute()
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/core/management/__init__.py", line 365, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/core/management/base.py", line 288, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/core/management/base.py", line 332, in execute
    self.check()
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/core/management/base.py", line 364, in check
    include_deployment_checks=include_deployment_checks,
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/core/management/base.py", line 351, in _run_checks
    return checks.run_checks(**kwargs)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/core/checks/registry.py", line 73, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/core/checks/model_checks.py", line 27, in check_all_models
    errors.extend(model.check(**kwargs))
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/models/base.py", line 1200, in check
    errors.extend(cls._check_fields(**kwargs))
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/models/base.py", line 1272, in _check_fields
    errors.extend(field.check(**kwargs))
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/models/fields/__init__.py", line 894, in check
    errors = super().check(**kwargs)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/models/fields/__init__.py", line 206, in check
    errors.extend(self._check_backend_specific_checks(**kwargs))
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/models/fields/__init__.py", line 303, in _check_backend_specific_checks
    return connections[db].validation.check_field(self, **kwargs)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/base/validation.py", line 21, in check_field
    field_type = field.db_type(self.connection)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/models/fields/__init__.py", line 648, in db_type
    return connection.data_types[self.get_internal_type()] % data
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/utils/functional.py", line 36, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/mysql/base.py", line 133, in data_types
    if self.features.supports_microsecond_precision:
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/utils/functional.py", line 36, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/mysql/features.py", line 65, in supports_microsecond_precision
    return self.connection.mysql_version >= (5, 6, 4)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/utils/functional.py", line 36, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/mysql/base.py", line 345, in mysql_version
    with self.temporary_connection() as cursor:
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/contextlib.py", line 82, in __enter__
    return next(self.gen)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/base/base.py", line 576, in temporary_connection
    cursor = self.cursor()
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/base/base.py", line 255, in cursor
    return self._cursor()
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/base/base.py", line 232, in _cursor
    self.ensure_connection()
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/base/base.py", line 216, in ensure_connection
    self.connect()
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/utils.py", line 89, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/base/base.py", line 216, in ensure_connection
    self.connect()
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/base/base.py", line 194, in connect
    self.connection = self.get_new_connection(conn_params)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/django/db/backends/mysql/base.py", line 236, in get_new_connection
    return Database.connect(**conn_params)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/MySQLdb/__init__.py", line 86, in Connect
    return Connection(*args, **kwargs)
  File "/home/ubuntu/.pyenv/versions/3.6.1/lib/python3.6/site-packages/MySQLdb/connections.py", line 204, in __init__
    super(Connection, self).__init__(*args, **kwargs2)

## django.db.utils.OperationalError: (2002, "Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)")
