# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Find_my_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mayoub <mayoub@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 14:20:23 by mayoub            #+#    #+#              #
#    Updated: 2023/03/15 16:08:19 by mayoub           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
	if type(object) == list:
		print("List :", type(object))
	elif type(object) == tuple:
		print("Tuple :", type(object))
	elif type(object) == set:
		print("Set :", type(object))
	elif type(object) == dict:
		print("Dict :", type(object))
	elif type(object) == str:
		print(object, "is in the kitchen", type(object))
	else:
		print("Type not found")
	return 42
