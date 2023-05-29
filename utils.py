import re
import json
from json.decoder import JSONDecodeError


def print_menu() -> str:
    """Funcion encargada de imprimir el menu en consola y captura la opcion ingresada por el usuario.

    Returns:
        str: valor ingresado por el usuario.
    """
    print("\n*********MENU PRINCIPAL*********")
    menu_str = "\n1-\tListar jugadores del Dream Team.\n2-\tMostrar estadisticas de un jugador."
    menu_str += "\n3-\tExportar estadisticas a CSV.\n4-\tBuscar jugador por nombre."
    menu_str += "\n5-\tMostrar promedio de puntos por partido del Dream Team, ordenado por nombre de manera ascendente."
    menu_str += "\n6-\tBuscar por nombre jugadores del 'Hall of Fame'."
    menu_str += "\n7-\tMostrar jugador con mayor cantidad de rebotes."
    menu_str += "\n8-\tMostrar jugador con mayor porcentaje de tiros de campo."
    menu_str += "\n9-\tMostrar jugador con mayor cantidad de asistencias."
    menu_str += "\n10-\tMostrar jugadores con mayor promedio de puntos por partido."
    menu_str += "\n11-\tMostrar jugadores con mayor promedio de rebotes por partido."
    menu_str += "\n12-\tMostrar jugadores con mayor promedio de asistencias por partido."
    menu_str += "\n13-\tCalcular y mostrar el jugador con la mayor cantidad de robos totales."
    menu_str += "\n14-\tCalcular y mostrar el jugador con la mayor cantidad de bloqueos totales."
    menu_str += "\n15-\tMostrar jugadores con mayor promedio de tiros libres por partido."
    menu_str += "\n16-\tCalcular y mostrar el promedio de puntos por partido del equipo"
    menu_str += "\n\texcluyendo al jugador con la menor cantidad de puntos por partido."
    menu_str += "\n17-\tCalcular y mostrar el jugador con la mayor cantidad de logros obtenidos."
    menu_str += "\n18-\tMostrar jugadores con mayor promedio de triples por partido."
    menu_str += "\n19-\tCalcular y mostrar el jugador con la mayor cantidad de temporadas jugadas."
    menu_str += "\n20-\tPermitir al usuario ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha,"
    menu_str += "\n\tque hayan tenido un porcentaje de tiros de campo superior a ese valor."
    menu_str += (
        "\n23-\tCalcular de cada jugador cuál es su posición en cada uno de los siguientes ranking:"
    )
    menu_str += "\n\t[Puntos Rebotes Asistencias Robos]"
    menu_str += "\n\nPara salir del programa ingrese (s)."
    print(menu_str)
    option_menu = input("Seleccione un valor: ")
    if validate_int(option_menu):
        if int(option_menu) >= 1 and int(option_menu) <= 20 or int(option_menu) == 23:
            valid_option = option_menu
        else:
            return ""
    elif option_menu.lower() == "s":
        valid_option = option_menu
    else:
        return ""
    return valid_option


def print_results(message: str, results: tuple[list, dict], staticals: str = "all") -> None:
    """Funcion encargada de imprimir de manera legible los resultados obtenidos.

    Args:
        message (str): mensaje editable que se imprimira como encabezado
        results (tuple[list, dict]): resultados de las funciones.
        staticals (str, optional): key-value de diccionario de estadisticas. Por default es "ALL".
    """
    print("\n********************************************")
    print(f"{message}")
    str_staticals = staticals.replace("_", " ").capitalize()
    if type(results) is list:
        if results != []:
            for dict_i in results:
                print(f"{dict_i['nombre']}\t{dict_i['posicion']}")
                if staticals != "all" and staticals != "logros":
                    print(f"{str_staticals}: {dict_i['estadisticas'][staticals]}")
                elif staticals == "logros":
                    for logro in dict_i["logros"]:
                        print(logro)
                    print(f"Total de logros conseguidos: {len(dict_i['logros'])}")
                else:
                    for key in dict_i["estadisticas"]:
                        print(
                            f"{key.replace('_', ' ').capitalize()}: {dict_i['estadisticas'][key]}"
                        )
        else:
            print("No se encontraron resultados.")
    elif type(results) is dict:
        if results is not None:
            print(f"{results['nombre']}\t{results['posicion']}")
            if staticals != "all":
                print(f"{str_staticals}: {results['estadisticas'][staticals]}")
            else:
                for key in results["estadisticas"]:
                    print(f"{key.replace('_', ' ').capitalize()}: {results['estadisticas'][key]}")
        else:
            print("No se encontraron resultados.")
    else:
        print("No se encontraron resultados.")
    print("********************************************")


def import_json_players(input_path: str) -> list:
    """Funcion encargada de cargar los datos desde un JSON.

    Args:
        input_path (str): ruta donde se encuentra el JSON.

    Returns:
        list: lista de diccionarios con datos de jugadores.
    """
    try:
        players_list = []
        with open(input_path, "r", encoding="utf-8") as file:
            players_list = json.load(file)
        return players_list
    except JSONDecodeError as e:
        print(e)


def validate_int(num_str: str) -> bool:
    """Validacion de numeros enteros en formato string.

    Args:
        num_str (str): numero entero en formato str.

    Returns:
        bool: True si es un numero entero, False si no lo es.
    """
    if re.search(r"^[0-9]+$", num_str):
        return True
    return False


def validate_string(string: str) -> bool:
    """Validacion de cadena de caracteres solo contenga letras.

    Args:
        string (str): Cadena de caracteres.

    Returns:
        bool: True si contiene solo letras, False si no.
    """
    if re.search(r"^[a-zA-Z]+$", string):
        return True
    return False


def validate_float(float_str: str) -> bool:
    """Validacion de numeros con decimales en formato str.

    Args:
        float_str (str): numero con decimales en formato str.

    Returns:
        bool: True sin es un numero con decimales, False si no lo es.
    """
    if re.search(r"^[0-9]+[,.][0-9]+$", float_str):
        return True
    return False


def print_all_players(players_list: list) -> None:
    """Imprime todos los jugadores de una lista.

    Args:
        players_list (list): Lista de jugadores.
    """
    print("\nNombre Jugador - Posición")
    for player in players_list:
        print(f"{player['nombre']}\t-\t{player['posicion']}")


def select_player(players_list: list) -> dict:
    """Seleccionar un jugador de la plantilla.

    Args:
        players_list (list): Lista de diccionarios con datos de jugadores

    Returns:
        dict: jugador seleccionado.
    """
    print("Dream Team")
    for p_index in range(len(players_list)):
        print(f"{p_index} - {players_list[p_index]['nombre']}")
    option = input("\nSeleccione un jugador ingresando su indice:")
    return players_list[int(option)]


def export_player_to_csv(player_dict: dict) -> None:
    """Exporta los datos de un jugador seleccionado a un archivo CSV.

    Args:
        player_dict (dict): Lista de diccionarios con datos de jugadores.
    """
    save_path = f"./estadisticas_{str(player_dict['nombre']).replace(' ','_')}.csv"
    del player_dict["logros"]
    dict_estadistic = player_dict["estadisticas"]
    del player_dict["estadisticas"]
    try:
        with open(save_path, "w", encoding="utf-8") as csv:
            firts_line = ",".join(player_dict.keys()) + ","
            firts_line += ",".join(dict_estadistic.keys()) + "\n"
            csv.write(firts_line)
            values = ",".join(str(valor) for valor in player_dict.values()) + ","
            values += ",".join(str(valor) for valor in dict_estadistic.values()) + "\n"
            csv.write(values)
            print("¡Se genero el archivo CSV con exito!\n")
    except Exception as error:
        print("No se pudo generar el arhcivo CSV")
        print(f"Se genero la siguiente excepcion: {error}")


def find_player(player_dict: list) -> tuple[list[str, str], list[None, str]]:
    """Busca jugador por nombre e imprime sus logros

    Args:
        player_dict (list): Lista de diccionarios de jugadores.

    Returns:
        tuple[list[None, str], list[str, str]]: En caso de encontrar el jugador ingresado retornara su nombre y logros.
        En caso de no encontrar el nombre ingresado retornara un mensaje.
    """
    rgx_list = []
    find_value = input("Ingrese el nombre del jugador que desea saber sus logros:")
    if validate_string(find_value) and len(find_value) > 3:
        # TODO: MEJORAR REGEX PARA Christian y Chris
        rgx_list.append(find_value.lower())
        rgx_list.append(f"{find_value[:3].lower()}+")
        for player in player_dict:
            for rgx in rgx_list:
                if re.match(rgx, player["nombre"].lower()):
                    return player["nombre"], player["logros"]
        return None, f"No se encontro ningún jugador con el nombre {find_value}"
    return None, "Ingrese un valor alfabetico y superior a 3 caracteres."


def calculate_averaga_points_per_game(player_list: list) -> float:
    """Calcular promedio de puntos por partido juegados.

    Args:
        player_list (list): Lista de diccionarios con datos de jugadores.

    Returns:
        float: Promedio de puntos.
    """
    acumulador = 0
    for avr_points in player_list:
        acumulador += avr_points["estadisticas"]["promedio_puntos_por_partido"]
    resultado = acumulador / len(player_list)
    return round(float(resultado), 2)


def sort_players(
    player_list: list,
    valor_ord: str,
    staticts: str = None,
    flag_statics: bool = False,
    sort_ord: str = "asc",
) -> list:
    """Ordenar lista de jugadores.

    Args:
        player_list (list): Lista de diccionarios con datos de jugadores.
        valor_ord (str): Valor de ordenamiento.
        staticts (str, optional): Llave de diccionario estadisticas. Por default None.
        flag_statics (bool, optional): Para setear si se debe ordenar por el valor de una lista. Por default es False.
        sort_ord (str, optional): Forma de ordenamiento. Por default es "asc".

    Returns:
        list: Lista de jugadores ordenada.
    """
    lst = player_list[:]
    range_a = len(lst)
    flag_swap = True
    while flag_swap:
        flag_swap = False
        range_a = range_a - 1
        for i in range(range_a):
            if flag_statics:
                if sort_ord == "asc":
                    if lst[i][valor_ord][staticts] > lst[i + 1][valor_ord][staticts]:
                        lst[i], lst[i + 1] = lst[i + 1], lst[i]
                        flag_swap = True
                else:
                    if lst[i][valor_ord][staticts] < lst[i + 1][valor_ord][staticts]:
                        lst[i], lst[i + 1] = lst[i + 1], lst[i]
                        flag_swap = True
            else:
                if sort_ord == "asc":
                    if lst[i][valor_ord] > lst[i + 1][valor_ord]:
                        lst[i], lst[i + 1] = lst[i + 1], lst[i]
                        flag_swap = True
                else:
                    if lst[i][valor_ord] < lst[i + 1][valor_ord]:
                        lst[i], lst[i + 1] = lst[i + 1], lst[i]
                        flag_swap = True
    return lst


def find_player_hall_of_fame(player_list: list) -> list:
    """Buscar jugadores que pertenezcan al salon de la fama.

    Args:
        player_list (list): Lista de diccionarios con datos de jugadores.

    Returns:
        _type_: _description_
    """
    test = find_player(player_list)
    if test[0] is not None:
        for logros in test[1]:
            if re.match(r"^miembro del salon de la fama del baloncesto{1}", logros.lower()):
                return test[0]
    else:
        return test[1]


def highest_statistical_value(player_list: list, statistics: str) -> list:
    """Validar jugadores que superen x valor en una estadistica.

    Args:
        player_list (list): Lista de diccionarios con jugadores.
        statistics (str): Clave-valor de la estadistica a comparar

    Returns:
        list: Lista de jugadores que superen estadistica ingresada.
    """
    list_max_value = []
    value_user = input("Ingrese un valor numerico (entero o con decimales):")
    if validate_int(value_user) or validate_float(value_user):
        if re.search(r"[,]", value_user):
            value_user = value_user.replace(",", ".")
        value_user = float(value_user)
        for player in player_list:
            if value_user <= player["estadisticas"][statistics]:
                list_max_value.append(player)
    return list_max_value


def avr_points_without_worse_scorer(player_list: list) -> float:
    """Calcula el promedio de puntos del equipo descartando al
    promedio de puntos por partido más bajo del equipo.

    Args:
        player_list (list): Lista de diccionarios con jugadores.

    Returns:
        float: promedio de puntos por partido calculado.
    """
    menor_puntos = sort_players(player_list, "estadisticas", "promedio_puntos_por_partido", True)
    print(
        f"El peor anotador del equipo es {menor_puntos[-1]['nombre']}",
        "\nPromedio de puntos por partido:",
        f"{menor_puntos[-1]['estadisticas']['promedio_puntos_por_partido']}",
    )
    del menor_puntos[-1]
    return calculate_averaga_points_per_game(menor_puntos)


def sort_for_position(player_list: list, statistics_key: str) -> list:
    """Ordena jugadores que superen x valor de estadistica alfabeticamente.

    Args:
        player_list (list): Lista de diccionarios con datos de jugadores
        statistics_key (str): Llave de diccionario estadisticas.

    Returns:
        list: Lista de jugadores ordenada alfabetidamente que hayan superado x valor en una estadistica.
    """
    highest_statiscal = highest_statistical_value(player_list, statistics_key)
    sort_position = sort_players(highest_statiscal, "posicion")
    return sort_position


def most_achievements(player_list: list) -> None:
    """Calcula y muesta al jugador con más logros conseguidos.

    Args:
        player_list (list): Lista de diccionarios con datos de jugadores
    """
    max_logros = ["", 0]
    for player in player_list:
        if len(player["logros"]) > max_logros[1]:
            max_logros[0] = [player]
            max_logros[1] = len(player["logros"])
    print_results("El jugador con más logros es:", max_logros[0], "logros")


def validate_same_statistics(player_list: list, statistics: str) -> list:
    """Valida jugadores que tienen la misma puntuación en X estadística.

    Args:
        player_list (list): Lista de diccionarios con datos de jugadores
        statistics (str): Llave correspondiente al diccionario de estadisticas

    Returns:
        list: Lista de jugadores con mismo valor en X estadistica.
    """
    max_player = player_list[0]
    list_max_players = [max_player]
    for player in player_list[1:]:
        if max_player["estadisticas"][statistics] == player["estadisticas"][statistics]:
            list_max_players.append(player)
    return list_max_players


def player_statistics_ranking(player_list: list) -> None:
    """Genera los rankings de puntos, rebotes, robos , asistencias y los exporta a un CSV.

    Args:
        player_list (list): Lista de diccionarios con datos de jugadores.
    """
    list_keys = ["puntos_totales", "rebotes_totales", "asistencias_totales", "robos_totales"]
    for item in list_keys:
        new_list = sort_players(player_list, "estadisticas", item, True, "des")
        for index in range(len(new_list)):
            for player in player_list:
                if new_list[index]["nombre"] == player["nombre"]:
                    player[item] = index+1
                    break
    export_ranking_to_csv(player_list)


def export_ranking_to_csv(player_dict: dict) -> None:
    """Función de uso interno para generar CSV con rankings de estadisticas.

    Args:
        player_dict (dict): Lista de diccionarios con datos de los jugadores
    """
    save_path = "./ranking_de_estadisticas.csv"
    flag_firt_line = False
    try:
        for player in player_dict:
            del player["logros"]
            del player["estadisticas"]
            del player["posicion"]
            if not flag_firt_line:
                with open(save_path, "w", encoding="utf-8") as csv:
                    firts_line = ",".join(player.keys()) + "\n"
                    csv.write(firts_line)
                    flag_firt_line = True
                    values = ",".join(str(valor) for valor in player.values()) + "\n"
                    csv.write(values)
            else:
                with open(save_path, "r", encoding="utf-8") as csv:
                    lineas = csv.readlines()
                value_line = ",".join(str(valor) for valor in player.values()) + "\n"
                lineas.append(value_line)
                with open(save_path, "w", encoding="utf-8") as csv:
                    csv.writelines(lineas)
        print("¡Se genero el archivo CSV con exito!\n")
    except Exception as error:
        print("No se pudo generar el arhcivo CSV")
        print(f"Se genero la siguiente excepcion: {error}")
