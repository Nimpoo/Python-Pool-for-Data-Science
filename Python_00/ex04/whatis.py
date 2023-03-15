# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mayoub <mayoub@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 15:04:53 by mayoub            #+#    #+#              #
#    Updated: 2023/03/15 15:49:21 by mayoub           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == '__main__':

	# No args
	if len(sys.argv) < 2:
		sys.exit()

	# More than 2 args
	if len(sys.argv) > 2:
		print("AssertionError: more than one argument are provided")
		sys.exit()

	# If arg is not number
	try:
		int(sys.argv[1])
	except ValueError:
		print("AssertionError: argument is not an integer");
		sys.exit()

	# Odd or Even
	if len(sys.argv) == 2:
		if int(sys.argv[1]) % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
