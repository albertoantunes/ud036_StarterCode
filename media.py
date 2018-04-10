class Movie():
    """Movie object

    Attributes:
        title: The movie title
        poster_image_url: the movie poster image url
        trailer_youtube_url: the movie trailer url on youtube
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Constructor
        """

        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
