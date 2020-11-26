from howlongtobeatpy import HowLongToBeat

def getMaxSimilarityElement(list_of_results):
    if list_of_results is not None and len(list_of_results) > 0:
        return max(list_of_results, key=lambda element: element.similarity)
    else:
        return None

game = input("Type the name of the game: ")

results = HowLongToBeat().search(game)
best_result = getMaxSimilarityElement(results)

if str(best_result.gameplay_main) > str(0):
    best_result.gameplay_main = str(best_result.gameplay_main)
else:
    best_result.gameplay_main = "Can't be beated"
    
# print("game_id: " + best_result.game_id)
# print("game_name: " + best_result.game_name)
# print("game_image_url: " + best_result.game_image_url)
# print("game_web_link: " + best_result.game_web_link)
# print("gameplay_main: " + best_result.gameplay_main)
# print("gameplay_main_unit: " + best_result.gameplay_main_unit)
# print("gameplay_main_label: " + best_result.gameplay_main_label)
# print("gameplay_main_extra: " + best_result.gameplay_main_extra)
# print("gameplay_main_extra_unit: " + best_result.gameplay_main_extra_unit)
# print("gameplay_main_extra_label: " + best_result.gameplay_main_extra_label)
# print("gameplay_completionist: " + best_result.gameplay_completionist)
# print("gameplay_completionist_unit: " + best_result.gameplay_completionist_unit)
# print("gameplay_completionist_label: " + best_result.gameplay_completionist_label)

print("Game: " + best_result.game_name)
print("Hours to beat: " + best_result.gameplay_main)


