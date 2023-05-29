from utils import (
    print_menu,
    import_json_players,
    print_all_players,
    select_player,
    export_player_to_csv,
    calculate_averaga_points_per_game,
    sort_players,
    find_player_hall_of_fame,
    highest_statistical_value,
    avr_points_without_worse_scorer,
    sort_for_position,
    print_results,
    most_achievements,
    validate_same_statistics
)


def __main__():
    option = ""
    data_dream_team = import_json_players("./dt.json")
    while option != "s":
        option = print_menu()
        match option:
            case "1":
                print_all_players(data_dream_team["jugadores"])
            case "2":
                selected_player = select_player(data_dream_team["jugadores"])
                print_results("Estadisticas de:", selected_player)
            case "3":
                export_player_to_csv(selected_player)
            case "4":
                player, logros = data_dream_team["jugadores"]
                if player is not None:
                    print(f"\n{player} tiene los siguientes: {logros}")
                else:
                    print(logros)
            case "5":
                avr_points = calculate_averaga_points_per_game(data_dream_team["jugadores"])
                print(f"\nPromedio total de puntos por partido del DREAM TEAM: {avr_points}\n")
                sorted_list = sort_players(data_dream_team["jugadores"], "nombre")
                print_results(
                    "Promedio de puntos por jugador:", sorted_list, "promedio_puntos_por_partido"
                )
            case "6":
                player_hall_fame = find_player_hall_of_fame(data_dream_team["jugadores"])
                if player_hall_fame is not None:
                    print(f"{player_hall_fame} es miembro del salon de la fama")
                else:
                    print("El jugador seleccionado no es miembro del salon de la fama.")
            case "7":
                firts_rebounds = sort_players(
                    data_dream_team["jugadores"], "estadisticas", "rebotes_totales", True, "des"
                )
                firts_rebounds = validate_same_statistics(firts_rebounds, "rebotes_totales")
                print_results(
                    "El jugador con mayor rebotes capturados es:",
                    firts_rebounds[0],
                    "rebotes_totales",
                )
            case "8":
                firts_shot = sort_players(
                    data_dream_team["jugadores"],
                    "estadisticas",
                    "porcentaje_tiros_de_campo",
                    True,
                    "des",
                )
                firts_shot = validate_same_statistics(firts_shot, "porcentaje_tiros_de_campo")
                print_results(
                    f"El jugador con mayor % de tiros de campo es:",
                    firts_shot[0],
                    "porcentaje_tiros_de_campo",
                )
            case "9":
                firts_assistance = sort_players(
                    data_dream_team["jugadores"], "estadisticas", "asistencias_totales", True, "des"
                )
                firts_assistance = validate_same_statistics(firts_assistance, "asistencias_totales")
                print_results(
                    "El jugador con mayor cantidad de asistencias es:",
                    firts_assistance[0],
                    "asistencias_totales",
                )
            case "10":
                more_points = highest_statistical_value(
                    data_dream_team["jugadores"], "promedio_puntos_por_partido"
                )
                print_results(
                    "Jugadores con mayor prom. de puntos:",
                    more_points,
                    "promedio_puntos_por_partido",
                )
            case "11":
                more_rebounds = highest_statistical_value(
                    data_dream_team["jugadores"], "promedio_rebotes_por_partido"
                )
                print_results(
                    "Jugadores con mayor cantidad de rebores:",
                    more_rebounds,
                    "promedio_rebotes_por_partido",
                )
            case "12":
                more_assistance = highest_statistical_value(
                    data_dream_team["jugadores"], "promedio_asistencias_por_partido"
                )
                print_results(
                    "Jugadores con mayor prom. de asistencias:",
                    more_assistance,
                    "promedio_asistencias_por_partido",
                )
            case "13":
                firts_steals = sort_players(
                    data_dream_team["jugadores"], "estadisticas", "robos_totales", True, "des"
                )
                firts_steals = validate_same_statistics(firts_steals, "robos_totales")
                print_results(
                    "El jugador con mayor cantidad de robos es:", firts_steals[0], "robos_totales"
                )
            case "14":
                firts_blocks = sort_players(
                    data_dream_team["jugadores"], "estadisticas", "bloqueos_totales", True, "des"
                )
                firts_blocks = validate_same_statistics(firts_blocks, "bloqueos_totales")
                print_results(
                    "El jugador con mayor cantidad de bloqueos es:",
                    firts_blocks[0],
                    "bloqueos_totales",
                )
            case "15":
                free_throw = highest_statistical_value(
                    data_dream_team["jugadores"], "porcentaje_tiros_libres"
                )
                print_results(
                    "Jugadores con mayor prom. de tiros libres:",
                    free_throw,
                    "porcentaje_tiros_libres",
                )
            case "16":
                avr_points = avr_points_without_worse_scorer(data_dream_team["jugadores"])
                print(
                    "El promedio de puntos del DREAM TEAM sin su peor anotador es: ",
                    f"{avr_points}",
                )
            case "17":
                most_achievements(data_dream_team["jugadores"])
            case "18":
                three_point_shot = highest_statistical_value(
                    data_dream_team["jugadores"], "porcentaje_tiros_triples"
                )
                print_results(
                    "Jugadores con mayor prom. de triples:",
                    three_point_shot,
                    "porcentaje_tiros_triples",
                )
            case "19":
                firts_seasons = sort_players(
                    data_dream_team["jugadores"], "estadisticas", "temporadas", True, "des"
                )
                firts_seasons = validate_same_statistics(firts_seasons, "temporadas")
                print_results(
                    "El jugador con mayor cantidad de temporadas es:", firts_seasons, "temporadas"
                )
            case "20":
                sorted_position = sort_for_position(
                    data_dream_team["jugadores"], "porcentaje_tiros_de_campo"
                )
                print_results(
                    "Jugadores con mayor prom. de tiros de campo:",
                    sorted_position,
                    "porcentaje_tiros_de_campo",
                )
            case "23":
                print("HOLA MIKE")
            case "s":
                continue
            case _:
                print("Opción invalida")
        input("\nPresione enter volver al menu inicial.")
    print("\n********* PROGRAMA FINALIZADO *********")


if __name__ == "__main__":
    __main__()
