# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_my_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mayoub <mayoub@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 12:11:06 by mayoub            #+#    #+#              #
#    Updated: 2023/03/15 18:11:06 by mayoub           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
from time import time

if __name__ == '__main__':

	tmp = time()

	month = datetime.datetime.now()

	str_time = str(tmp)
	str_scientific = str(tmp)

	str_display = '{:,.4f}'.format(tmp) # , tout les 4 nbr en convertissant en float
	str_scientific = '{:.2e}'.format(tmp)

	print("Seconds since January 1, 1970:", str_display, "or", str_scientific, "in scientific notation")
	print(month.strftime("%B %a %y"))
	