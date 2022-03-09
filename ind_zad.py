#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    routes = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            start_destination = input("Введите название начального пункта "
                                      "назначения "
                                )
            end_destination = input("Введите название конечного пункта "
                                    "назначения "
                              )
            route_num = input("Введите номер маршрута ")
            route = {
                'start_destination': start_destination,
                'end_destination': end_destination,
                'route_num': route_num,
            }
            routes.append(route)
            if len(routes) > 1:
                routes.sort(
                    key=lambda item:
                    item.get('route_num', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "No",
                    "Начальный пункт",
                    "Конечный пункт",
                    "Номер маршрута"
                )
            )
            print(line)

            for idx, route in enumerate(routes, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:<15} |'.format(
                        idx,
                        route.get('start_destination', ''),
                        route.get('end_destination', ''),
                        route.get('route_num', 0)
                    )
                )
            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            route_num = (parts[1].capitalize())
            print(f"Для маршрута номер {route_num}:")
            count = 0
            for route in routes:
                if route.get('route_num') == route_num:
                    count += 1
                    print(
                        '{:>4}: Начальный пункт: {}; Конечный пункт:{}'.format(
                            count,
                            route.get('start_destination',
                                      ''),
                            route.get('end_destination', ''))
                    )
            if count == 0:
                print("Маршруты не найдены")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список всех маршрутов;")
            print("select <номер маршрута> - запросить маршруты с указанным"
                  " номером;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
