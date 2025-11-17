from selenium.webdriver.common.by import By

class Locators():

    LOGIN_BUTTON_ON_MAIN_PAGE=(By.XPATH, '//button[text()="Войти в аккаунт"]')     # Кнопка "Войти в аккаунт" на главной странице
    REG_BUTTON_ON_LOGIN_PAGE=(By.XPATH, '//a[text()="Зарегистрироваться"]')     # Кнопка "Зарегистрироваться" на странице входа
    INPUT_NAME=(By.XPATH, '//label[text()="Имя"]/following-sibling::input')     # Поле ввода имени на странице регистрации
    INPUT_EMAIL=(By.XPATH, '//label[text()="Email"]/following-sibling::input')     # Поле ввода Email на странице регистрации и на странице входа
    INPUT_PASSWORD=(By.NAME, 'Пароль')     # Поле ввода пароля на странице регистрации и на странице входа
    REG_BUTTON_ON_REG_PAGE=(By.XPATH, '//button[text()="Зарегистрироваться"]')     # Кнопка "Зарегистрироваться" на странице регистрации
    LOGIN_BUTTON_ON_REG_PAGE=(By.XPATH, '//a[text()="Войти"]')     # Кнопка "Войти" на странице регистрации
    LOGIN_BUTTON_ON_RESTORE_PAGE=(By.XPATH, '//a[text()="Войти"]')     # Кнопка "Войти" на странице восстановления пароля
    PLACE_ORDER_BUTTON=(By.XPATH, '//button[text()="Оформить заказ"]')     # Кнопка "Оформить заказ" на главной странице
    CONSTRUCTOR_BUTTON=(By.XPATH, '//p[text()="Конструктор"]')     # Кнопка перехода в конструктор
    CREATE_BURGER=(By.XPATH, '//h1[text()="Соберите бургер"]')     # Заголовок "Соберите бургер"
    LOGO_STELLARBURGERS=(By.XPATH, '//div/a[@href="/"]')     # Лого Stellar Burgers

    PROFILE_BUTTON=(By.XPATH, '//p[text()="Личный Кабинет"]')     # Кнопка перехода в личный кабинет
    LOGIN_BUTTON=(By.XPATH, '//button[text()="Войти"]')     # Кнопка "Войти" на странице входа
    LOGIN_EMAIL_INPUT=(By.XPATH, "//input[@type='text']")     # Поле ввода логина на странице входа
    LOGIN_PASSWORD_INPUT=(By.XPATH, ".//input[@type='password']")     # Поле ввода пароля на странице входа
    LOGOUT_BUTTON=(By.XPATH, '//button[text()="Выход"]')     # Кнопка "Выход" в Личном Кабинете

    ERROR_INCORRECT_PASSWORD=(By.XPATH, '//p[text()="Некорректный пароль"]')     # Сообщение о некорректном пароле
    ERROR_BORDER=(By.CSS_SELECTOR, ".input_status_error")     # Красная рамка вокруг поля ввода пароля

    SELECTOR_BUNS=(By.XPATH, '//span[text()="Булки"]/parent::div')     # Раздел с булками в конструкторе
    SELECTOR_SAUCES=(By.XPATH, '//span[text()="Соусы"]/parent::div')     # Раздел с соусами в конструкторе
    SELECTOR_FILLINGS=(By.XPATH, '//span[text()="Начинки"]/parent::div')     # Раздел с начинками в конструкторе    