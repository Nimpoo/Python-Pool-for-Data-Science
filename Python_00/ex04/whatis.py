# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mayoub <mayoub@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 15:04:53 by mayoub            #+#    #+#              #
#    Updated: 2023/03/16 14:01:36 by mayoub           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == '__main__':

	def main():

		assertionError = "AssertionError: more than one argument are provided"
		assertionError2 = "AssertionError: argument is not an integer"

		# No args
		if len(sys.argv) < 2:
			sys.exit()

		# More than 2 args
		if len(sys.argv) > 2:
			raise AssertionError(assertionError)

		# If arg is not number
		try:
			int(sys.argv[1])
		except ValueError:
			raise AssertionError(assertionError2)

		# Odd or Even
		if len(sys.argv) == 2:
			if int(sys.argv[1]) % 2 == 0:
				print("I'm Even.")
			else:
				print("I'm Odd.")
	try:
		main()
	except AssertionError as e:
		print(e)