genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    print(genre_total_play_dict.items())
    print(genre_index_play_array_dict.items())


get_melon_best_album(genres, plays)
