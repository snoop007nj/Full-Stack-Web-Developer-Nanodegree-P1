#!/usr/bin/python2.7

import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	"""contructor"""
	def __init__(self, title, storyline, poster_image, trailer_youtube):
		#title of the movie
		self.title = title

		#story line of the movie
		self.storyLine = storyline

		#url to an image of the movie
		self.poster_image_url = poster_image

		#youtube trailer of the movie
		self.trailer_youtube_url = trailer_youtube	

	"""Open a youtube video"""
	def showTrailer(self):
		webbrowser.open(self.trailerYoutube)
