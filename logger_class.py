# Создайте систему логирования, которая получает поток сообщений вместе с их временными метками.
# Каждое уникальное сообщение должно печататься не чаще, чем раз в 10 секунд
# (то есть, сообщение, напечатанное во временной метке t,
# предотвратит печать других идентичных сообщений до временной метки t + 10).
# Все сообщения будут приходить в хронологическом порядке.
# Несколько сообщений могут поступить в одно и то же время.
#
# Реализуйте класс Logger:

from datetime import datetime, timedelta
from random import randint
from time import sleep

from pydantic.v1.errors import cls_kwargs


class Logger:
    def __init__(self):
        self.logger = list()

    @classmethod
    def check_time_stamp(cls, instance, time_stamp: datetime) -> bool:
        if not instance.logger:  # Проверяем, есть ли элементы в logger
            return True  # Если нет записей, можно добавлять
        tmp_tuple = instance.logger[-1]
        time_stamp_dict = datetime.strptime(tmp_tuple[0], '%Y-%m-%d %H:%M:%S.%f')
        time_stamp_dict = time_stamp_dict + timedelta(seconds=10)
        return time_stamp > time_stamp_dict

    def get_logger(self):
        return self.logger

    def set_logger(self, time_stemp: datetime = None, string: str = None):
        if time_stemp is not None and string is not None:
            if self.check_time_stamp(self, time_stemp):  # Передаем self как экземпляр
                tmp_tuple = (str(time_stemp), string)
                self.logger.append(tmp_tuple)
                return 'Added'
            else:
                return 'Not Added'
        else:
            return 'No data to add'

logger = Logger()
logger.set_logger(datetime.now(), 'string')
logger.set_logger(datetime.now(), 'string')
logger.set_logger(datetime.now(), 'string')
sleep(10)
logger.set_logger(datetime.now(), 'string')
print(logger.get_logger())