from pathlib import Path

file_name_read_and_write = "log_for_game_in_main1.txt"
relative_file_directory_for_read_and_write = Path(file_name_read_and_write)

with open(relative_file_directory_for_read_and_write, 'r', encoding='utf-8') as data:
    
    results_all_games = list()
    
    for line in data:
        results_all_games.append(line)

    for count in range(0, len(results_all_games), 1):
        results_all_games[count] = results_all_games[count].replace('\n', '')


def print_resalt_for(results_all_games: str):

    if not results_all_games:
        print("\n")
        print("\n")
        print('СОХРАНЕННЫХ РЕЗУЛЬТАТОВ ИГР НЕТ')
        print("\n")
        print("\n")
    else:
        print("\n")
        print(f"\tВСЕГО СОХРАНЕННО ИГР: {len(results_all_games)}")
        print("\n")
        print("\tРЕЗУЛЬТАТЫ ПОСЛЕДНЕЙ СОХРАНЕННОЙ ИГРЫ:")
        print("\n")
        print("\t", "'"+ results_all_games[len(results_all_games)-1].split("Status ")[1].split(",")[0])
        print("\n")
        print("\t", "'"+ results_all_games[len(results_all_games)-1].split("Status ")[2].split(",")[0])
        print("\n")

print_resalt_for(results_all_games)