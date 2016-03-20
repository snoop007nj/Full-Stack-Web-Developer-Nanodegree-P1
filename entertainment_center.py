#!/usr/bin/python2.7

import media
import fresh_tomatoes

"""Declaring 6 new instances of class Movie"""

toyStory = media.Movie("Toy Story",
			"A story of a boy and hist toys that come to life",
			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
			"A marine on an alien planet",
			"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
			"https://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock",
			"Using rock music to learn",
			"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
			"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
			"A rat is a chef in Paris",
			"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
			"https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
			"Going back in time to meet authors",
			"http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
			"https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
			"Going back in time to meet authors",
			"http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
			"https://www.youtube.com/watch?v=PbA63a7H0bo")

#list of movies
movies = [toyStory, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

#display content in html
fresh_tomatoes.open_movies_page(movies)

