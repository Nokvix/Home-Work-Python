with (open("registrations.txt", "r", encoding="utf-8") as registrations,
      open("registrations_good.log", "w", encoding="utf-8") as registrations_good,
      open("registrations_bad.log", "w", encoding="utf-8") as registrations_bad):
    for registration_data in registrations:
        personal_data = registration_data.split()
        try:
            if len(personal_data) != 3:
                raise IndexError

            name, email, age = personal_data[0], personal_data[1], personal_data[2]

            if not name.isalpha():
                raise NameError

            elif "@" not in email or "." not in email:
                raise SyntaxError

            elif 10 > int(age) or 99 < int(age):
                raise ValueError

            else:
                registrations_good.write(registration_data)
        except IndexError:
            registrations_bad.write("{}\tНЕ присутствуют все три поля\n".format(registration_data.replace("\n", "")))
        except NameError:
            registrations_bad.write(
                "{}\tПоле «Имя» содержит НЕ только буквы\n".format(registration_data.replace("\n", "")))
        except SyntaxError:
            registrations_bad.write(
                "{}\tПоле «Имейл» НЕ содержит @ и точку\n".format(registration_data.replace("\n", "")))
        except ValueError:
            registrations_bad.write(
                "{}\tПоле «Возраст» НЕ представляет число от 10 до 99\n".format(registration_data.replace("\n", "")))
