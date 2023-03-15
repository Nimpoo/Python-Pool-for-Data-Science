# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mayoub <mayoub@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 14:37:26 by mayoub            #+#    #+#              #
#    Updated: 2023/03/15 15:34:23 by mayoub           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
	if object == None:
		print("Nothing:", object, type(object))
	elif type(object) == float and str(object) == "nan":
		print("Cheese:", object, type(object))
	elif type(object) == int and object == 0:
		print("Zero:", object, type(object))
	elif object == "":
		print("Empty:", object, type(object))
	elif object == False:
		print("Fake:", object, type(object))
	else:
		print("Type not found")
		return 1
	return 0
