import media
import fresh_tomatoes

# Movies list
movies_list = [
    media.Movie(
        'Pacific Rim',
        'https://ia.media-imdb.com/images/M/MV5BMTY3MTI5NjQ4Nl5BMl5BanBnXkFtZT'
        'cwOTU1OTU0OQ@@._V1_SY1000_CR0,0,676,1000_AL_.jpg',
        'https://www.youtube.com/watch?v=5guMumPFBag'
    ),
    media.Movie(
        'Avengers: Infinity War',
        'https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZT'
        'gwNzY1MTUwNTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
        'https://www.youtube.com/watch?v=QwievZ1Tx-8'
    ),
    media.Movie(
        'The Hangover',
        'https://ia.media-imdb.com/images/M/MV5BNDAxMTZmZGItZmM2NC00M2E1LWI1Nm'
        'EtZjhhODM2MGU0ZmJlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX675_CR0,0,675,99'
        '9_AL_.jpg',
        'https://www.youtube.com/watch?v=tcdUhdOlz9M'
    ),
    media.Movie(
        'Akira',
        'https://ia.media-imdb.com/images/M/MV5BM2ZiZTk1ODgtMTZkNS00NTYxLWIxZT'
        'UtNWExZGYwZTRjODViXkEyXkFqcGdeQXVyMTE2MzA3MDM@._V1_SY1000_CR0,0,675,1'
        '000_AL_.jpg',
        'https://www.youtube.com/watch?v=lG2WL9brJr0'
    ),
    media.Movie(
        'Rick',
        'https://ia.media-imdb.com/images/M/MV5BMTk3MTQ2MjQ4OV5BMl5BanBnXkFtZT'
        'cwNDQ1NTUyMQ@@._V1_.jpg',
        'https://www.youtube.com/watch?v=vNz83znrSKY'
    ),
    media.Movie(
        'Rolling',
        'https://ia.media-imdb.com/images/M/MV5BYmEyZjkyODktMzk2Zi00NzU4LWExND'
        'ctYzgyYzk2ZDAyM2ZjXkEyXkFqcGdeQXVyNTM3NjI2NTA@._V1_SY1000_CR0,0,658,1'
        '000_AL_.jpg',
        'https://www.youtube.com/watch?v=DLzxrzFCyOs'
    )
]

# generate the static webpage using the movies list provided
# and opens it in the browser
fresh_tomatoes.open_movies_page(movies_list)
