# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sihemayoub <sihemayoub@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 15:04:53 by mayoub            #+#    #+#              #
#    Updated: 2023/03/16 00:42:50 by sihemayoub       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == '__main__':

	assertionError = "AssertionError: more than one argument are provided"
	assertionError2 = "AssertionError: argument is not an integer"

	# No args
	if len(sys.argv) < 2:
		sys.exit()

	# More than 2 args
	try:
		assert len(sys.argv) <= 2, assertionError2
	except AssertionError as e:
		print(e)
		sys.exit()

	# If arg is not number
	try:
		assert sys.argv[1].isdigit(), assertionError2
	except AssertionError as e:
		print(e)
		sys.exit()

	# Odd or Even
	if len(sys.argv) == 2:
		if int(sys.argv[1]) % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
