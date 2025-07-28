from ItchIo import ItchIOClient
from customdns import monkey_patch_dns

if __name__ == "__main__":
    monkey_patch_dns()
    API_KEY = input("itch.io apikey: ")
    itch = ItchIOClient(API_KEY)
    collections = itch.list_collections()
    for coll in collections:
        print(f"🗂️ Collection: {coll['title']} (ID: {coll['id']}) with {coll['games_count']} games")
        print("(Takes a while because we check if the game is taken down)")
        games = itch.get_collection_games(coll["id"])
        for g in games:
            game_id = g["game"]["id"]
            game_info = itch.get_game_by_id(game_id)

            if itch.is_game_taken_down(game_id):
                downloads = itch.get_game_downloads(game_id)
                print(f"🎮 {game_info['title']} by {game_info['user']['username']}")

                if len(downloads) == 0:
                    print("  📦 Completely deleted by itch")
                else:
                    for d in downloads:
                        print(f"  📦 {d['name']} ({d['filename']}) : {d['url']}")
