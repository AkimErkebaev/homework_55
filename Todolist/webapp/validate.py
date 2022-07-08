def article_validate(name, description, status):
    errors = {}
    if not name:
        errors["title"] = "Поле обязательное"
    elif len(name) > 50:
        errors["title"] = "Должно быть меньше 50 символов"
    if not description:
        errors["description"] = "Поле обязательное"
    elif len(description) > 50:
        errors["description"] = "Должно быть меньше 50 символов"
    if not status:
        errors["content"] = "Поле обязательное"
    elif len(status) > 3000:
        errors["content"] = "Должно быть меньше 3000 символов"
    return errors
