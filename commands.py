def shutdown():
    return {
        "command": "shutdown -s -t 5",
        "200": "Компьютер успешно выключен",
        "Authentication Error": "Неверный логин или пароль",
        "TimeOut Error": "Не удалось подключиться к компьютеру",
        }

def Teacher_User():
    return {
        "command": "net user Teacher 6143 /add",
        "200": "Пользователь Teacher успешно создан ",
        "Authentication Error": "Неверный логин или пароль",
        "TimeOut Error": "Не удалось подключиться к компьютеру",
        }

def student_account():
        return {
        "command": 'net user Student ""',
        "200": "Изменен пароль от аккаунта Student",
        "Authentication Error": "Неверный логин или пароль",
        "TimeOut Error": "Не удалось подключиться к компьютеру",
        }

def change_password_user():
        return {
        "command": 'net user User 739146',
        "200": "Изменен пароль от аккаунта User",
        "Authentication Error": "Неверный логин или пароль",
        "TimeOut Error": "Не удалось подключиться к компьютеру",
        }

def delete_tau_design():
        return {
        "command": 'net user "TAU DESIGN" /delete',
        "200": "Учетная запись удалена",
        "Authentication Error": "Неверный логин или пароль",
        "TimeOut Error": "Не удалось подключиться к компьютеру",
        }

def reboot():
        return {
        "command": 'shutdown /r /t 5',
        "200": "Компьютер успешно перезагружен",
        "Authentication Error": "Неверный логин или пароль",
        "TimeOut Error": "Не удалось подключиться к компьютеру",
        }

        
def tau_session_deactivate():
        return {
        "command": 'net user "TAU SESSION" /active:no',
        "200": "Учетная запись TAU SESSION заблокирована",
        "Authentication Error": "Неверный логин или пароль",
        "TimeOut Error": "Не удалось подключиться к компьютеру",
        }

def tau_session_activate():
        return {
        "command": 'net user "TAU SESSION" /active:yes',
        "200": "Учетная запись TAU SESSION заблокирована",
        "Authentication Error": "Неверный логин или пароль",
        "TimeOut Error": "Не удалось подключиться к компьютеру",
        }

def zoom_install():
        return {
        "command": '\\89.250.88.4\документы tau\data\zoominstall.bat',
        "200": "Учетная запись TAU SESSION заблокирована",
        "Authentication Error": "Неверный логин или пароль",
        "TimeOut Error": "Не удалось подключиться к компьютеру",
        }