# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mayoub <mayoub@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:24:00 by mayoub            #+#    #+#              #
#    Updated: 2023/03/15 18:07:29 by mayoub           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':

	ft_list = ["Hello", "tata!"] # List
	ft_tuple = ("Hello", "toto") # Tuple
	ft_set = {"Hello", "tutu!"} # Set
	ft_dict = {"Hello" : "titi!"} # Dictionnary

	# List
	ft_list[1] = "World!";

	# Tuple
	tmp_tuple = list(ft_tuple)
	tmp_tuple[1] = "France!";
	ft_tuple = tuple(tmp_tuple);

	# Set
	ft_set.discard("tutu!")
	ft_set.add("Nice!");

	# Dictionnary
	ft_dict['Hello'] = "42Nice!";

	print(ft_list)
	print(ft_tuple)
	print(ft_set)
	print(ft_dict)
