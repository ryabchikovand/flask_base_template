"""
Модуль конфигурирования базового
конфигурационного класса приложения
"""
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "223e23efewvfgbegbvsdfav"
