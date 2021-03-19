import numpy as np
import time
import sys

import tkinter as tk


UNIT = 1
NWC_H = 930
NWC_W = 1200

room_coords = {
	"1003E": (118, 64, 70, 120),
	"1003B_A": (96, 62, 401, 6),
	"1003B_B": (96, 62, 322, 6),
	"1003G_A": (59, 87, 321, 120),
	"1003G_B": (59, 87, 416, 120),
	"1003G_C": (59, 87, 416, 179),
	"1000M_A1": (66, 53, 64, 961),
	"1000M_A2": (66, 53, 125, 961),
	"1000M_A5": (65, 49, 325, 961),
	"1000M_A6": (66, 51, 382, 961),
	"1008": (81, 118, 321, 305)
}
room_energy = {
	"1003E": [91, 91, 90, 92, 90, 92, 90, 90, 92, 91, 89, 89, 89, 91, 89, 89, 89, 90, 88, 90, 86, 88, 86, 87, 98, 411, 568, 567, 399, 342, 327, 407, 854,
		1068, 1070, 1089, 1023, 1763, 1827, 1411, 1042, 1134, 1718, 2515, 745, 867, 458, 433, 365, 549, 507, 589, 2787, 4301, 2517, 1682, 1204, 562, 450, 818,
		426, 439, 459, 511, 431, 440, 467, 469, 521, 465, 515, 373, 190, 132, 116, 90, 93, 92, 92, 93, 93, 92, 93, 92, 92, 93, 91, 92, 92, 94, 93, 90, 92, 89, 92, 90],
	"1003B_A": [570, 567, 562, 568, 563, 568, 564, 565, 566, 566, 562, 557, 555, 555, 550, 559, 566, 568, 560, 563, 559, 562, 559, 561, 571, 943, 1077, 1038,
		722, 617, 607, 752, 1427, 1568, 1578, 1570, 1478, 2185, 2319, 1811, 1515, 1737, 2602, 5745, 5247, 4832, 1790, 1870, 1708, 1744, 2640, 979, 809,
		1182, 3640, 3525, 2067, 1070, 917, 1409, 1215, 1074, 1103, 903, 663, 706, 722, 696, 742, 713, 764, 619, 477, 552, 690, 509, 540, 552, 561, 561, 563,
		563, 566, 554, 557, 560, 549, 563, 565, 574, 572, 562, 563, 550, 557, 558],
	"1003B_B": [570, 568, 562, 568, 564, 568, 564, 565, 566, 566, 562, 557, 555, 555, 550, 559, 566, 568, 560, 563, 559, 562, 559, 561, 571, 943, 1077, 1038, 722,
		617, 607, 752, 1427, 1568, 1578, 1570, 1479, 2185, 2319, 1811, 1515, 1737, 2602, 5745, 5247, 4832, 1790, 1870, 1708, 1744, 2641, 979, 809, 1182,
		3640, 3525, 2067, 1070, 917, 1409, 1215, 1074, 1103, 903, 663, 706, 722, 696, 742, 713, 765, 619, 477, 553, 690, 510, 541, 552, 561, 561, 563, 564,
		567, 554, 558, 560, 550, 563, 566, 574, 572, 562, 563, 551, 557, 559],
	"1003G_A": [91, 91, 90, 92, 90, 92, 90, 90, 92, 91, 89, 89, 89, 91, 89, 89, 89, 90, 88, 90, 86, 88, 86, 87, 98, 411, 568, 567, 399, 342, 327, 407, 854,
		1068, 1070, 1089, 1023, 1763, 1827, 1411, 1042, 1134, 1718, 2515, 745, 867, 458, 433, 365, 549, 507, 589, 2787, 4301, 2517, 1682, 1204, 562, 450, 818,
		426, 439, 459, 511, 431, 440, 467, 469, 521, 465, 515, 373, 190, 132, 116, 90, 93, 92, 92, 93, 93, 92, 93, 92, 92, 93, 91, 92, 92, 94, 93, 90, 92, 89, 92, 90],
	"1003G_B": [91, 91, 90, 92, 90, 92, 90, 90, 92, 91, 89, 89, 89, 91, 89, 89, 89, 90, 88, 90, 86, 88, 86, 87, 98, 411, 568, 567, 399, 342, 327, 407, 854,
		1068, 1070, 1089, 1023, 1763, 1827, 1411, 1042, 1134, 1718, 2515, 745, 867, 458, 433, 365, 549, 507, 589, 2787, 4301, 2517, 1682, 1204, 562, 450, 818,
		426, 439, 459, 511, 431, 440, 467, 469, 521, 465, 515, 373, 190, 132, 116, 90, 93, 92, 92, 93, 93, 92, 93, 92, 92, 93, 91, 92, 92, 94, 93, 90, 92, 89, 92, 90],
	"1003G_C": [91, 91, 90, 92, 90, 92, 90, 90, 92, 91, 89, 89, 89, 91, 89, 89, 89, 90, 88, 90, 86, 88, 86, 87, 98, 411, 568, 567, 399, 342, 327, 407, 854,
		1068, 1070, 1089, 1023, 1763, 1827, 1411, 1042, 1134, 1718, 2515, 745, 867, 458, 433, 365, 549, 507, 589, 2787, 4301, 2517, 1682, 1204, 562, 450, 818,
		426, 439, 459, 511, 431, 440, 467, 469, 521, 465, 515, 373, 190, 132, 116, 90, 93, 92, 92, 93, 93, 92, 93, 92, 92, 93, 91, 92, 92, 94, 93, 90, 92, 89, 92, 90],
	"1000M_A1": [235, 236, 239, 236, 236, 236, 236, 236, 236, 236, 236, 236, 235, 236, 235, 235, 235, 235, 235, 235, 234, 235, 234, 235, 235, 235, 235, 235,
		235, 235, 235, 235, 235, 235, 235, 235, 235, 234, 235, 235, 236, 236, 236, 237, 239, 237, 237, 236, 237, 236, 237, 238, 237, 238, 237, 238, 237,
		237, 237, 237, 237, 236, 235, 235, 235, 235, 237, 237, 236, 236, 236, 235, 235, 235, 236, 235, 236, 235, 236, 236, 236, 236, 236, 236, 236, 236,
		235, 236, 236, 237, 236, 236, 235, 235, 235, 235],
	"1000M_A2": [235, 236, 239, 236, 236, 236, 236, 236, 236, 236, 236, 236, 235, 236, 235, 235, 235, 235, 235, 235, 234, 235, 234, 235, 235, 235, 235, 235,
		235, 235, 235, 235, 235, 235, 235, 235, 235, 234, 235, 235, 236, 236, 236, 237, 239, 237, 237, 236, 237, 236, 237, 238, 237, 238, 237, 238, 237,
		237, 237, 237, 237, 236, 235, 235, 235, 235, 237, 237, 236, 236, 236, 235, 235, 235, 236, 235, 236, 235, 236, 236, 236, 236, 236, 236, 236, 236,
		235, 236, 236, 237, 236, 236, 235, 235, 235, 235],
	"1000M_A5": [235, 236, 239, 236, 236, 236, 236, 236, 236, 236, 236, 236, 235, 236, 235, 235, 235, 235, 235, 235, 234, 235, 234, 235, 235, 235, 235, 235,
		235, 235, 235, 235, 235, 235, 235, 235, 235, 234, 235, 235, 236, 236, 236, 237, 239, 237, 237, 236, 237, 236, 237, 238, 237, 238, 237, 238, 237,
		237, 237, 237, 237, 236, 235, 235, 235, 235, 237, 237, 236, 236, 236, 235, 235, 235, 236, 235, 236, 235, 236, 236, 236, 236, 236, 236, 236, 236,
		235, 236, 236, 237, 236, 236, 235, 235, 235, 235],
	"1000M_A6": [235, 236, 239, 236, 236, 236, 236, 236, 236, 236, 236, 236, 235, 236, 235, 235, 235, 235, 235, 235, 234, 235, 234, 235, 235, 235, 235, 235,
		235, 235, 235, 235, 235, 235, 235, 235, 235, 234, 235, 235, 236, 236, 236, 237, 239, 237, 237, 236, 237, 236, 237, 238, 237, 238, 237, 238, 237,
		237, 237, 237, 237, 236, 235, 235, 235, 235, 237, 237, 236, 236, 236, 235, 235, 235, 236, 235, 236, 235, 236, 236, 236, 236, 236, 236, 236, 236,
		235, 236, 236, 237, 236, 236, 235, 235, 235, 235],
	"1008": [174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173,
		174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173,
		174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173,
		174, 173, 174, 173, 174, 173, 174, 173, 174, 173, 174, 173]
}
occupantMap = {'Mark':0,
				'Joe':1,
				'Lei':2,
				'Abhi':3,
				'Ankur':4,
				'Anjaly':5,
				'Jingping':6,
				'Yanchen':7,
				'Hengjiu':8,
				'Chenye':9,
				'Fred':10,
				'Stephen':11,
				'Peter':12}

room_states = ["1003E", "1003B_A", "1003B_B", "1003G_A",
			   "1003G_B", "1003G_C", "1000M_A1", "1000M_A2",
			   "1000M_A5", "1000M_A6", "1008"]
person_states = ["Peter", "Yanchen"]
default = "1000M_A6"


class NWC(tk.Tk, object):
	def __init__(self):
		super(NWC, self).__init__()
		self.action_space = room_states * 2 # number of rooms x number of people
		print(self.action_space)
		self.n_actions = len(self.action_space)
		# self.n_sparse = len(room_states) * 2 # number of people x number of rooms
		self.n_sparse = len(person_states)
		self.n_dense = len(room_states) + 1 # each room energy and 1 for time
		self.n_features = self.n_sparse + self.n_dense

		self.title('maze')
		self.occupants = {}
		self.room = {}
		self._build_NWC()
		self.t = 32

	def _build_NWC(self):
		self.canvas = tk.Canvas(self, bg='white',
						   height=NWC_H * UNIT,
						   width=NWC_W * UNIT)

		# create grids
		for room in room_coords:
			(w, h, y, x) = room_coords[room]
			self.canvas.create_line(x, y, x, y+h)
			self.canvas.create_line(x+w, y, x+w, y+h)
			self.canvas.create_line(x, y, x+w, y)
			self.canvas.create_line(x, y+h, x+w, y+h)
		(w, h, y, x) = room_coords[default]
		for i, person in enumerate(person_states):
			self.occupants[person] = self.canvas.create_oval(
				x+20*i, y, x+20*i+10, y+10, fill='black'
				)
			self.room[person] = default
		self.canvas.pack()

	def reset(self):
		self.update()
		time.sleep(0.1)
		self.t = 32
		# state = [0] * len(room_states) * 2
		# state[room_states.index(default)] = 1
		state = [0] * len(person_states)
		for i, person in enumerate(person_states):
			self.canvas.delete(self.occupants[person])
			(w, h, y, x) = room_coords[default]
			self.occupants[person] = self.canvas.create_oval(
				x+20*i, y, x+20*i+10, y+10, fill='black'
				)
			self.room[person] = default
			state[i] = room_states.index(default)
			# state[room_states.index(default) + len(room_states)*i] = 1
			# start all users at default

		state_energies = [0] * len(room_states)
		for i, room in enumerate(room_states):
			state_energies[i] = room_energy[room][self.t]
		return np.array(state + state_energies + [self.t]) # rooms, energy, time

	def calculate_reward(self):
		reward = 0



		return reward


	def step(self, action):
		ind = action % len(room_states) # which room to move
		print(room_states[ind])
		self.t += 1

		
		room_name = room_states[ind]
		person_ind = action // len(room_states) # which person takes action
		person = person_states[person_ind]
		s = self.canvas.coords(self.occupants[person]) # old location
		old_x, old_y = s[0], s[1]
		(w, h, y, x) = room_coords[room_name] # coords of new room
		self.canvas.move(self.occupants[person], x - old_x, y - old_y)
		old_room = self.room[person]
		self.room[person] = room_name
		# if action == 9 or action == 1:
		# 	reward = 1
		# 	done = True

		reward = room_energy[old_room][self.t] - room_energy[self.room[person]][self.t]
		print(reward)
		if self.t == 72:
			done = True
		else:
			done = False
		# state = [0] * len(room_states) * 2
		state = [0] * len(person_states)
		for i, person in enumerate(person_states):
			person_room = self.room[person]
			room_ind = room_states.index(person_room)
			state[i] = room_ind + i*len(room_states)
			# state[i*len(room_states) + room_ind] = 1
		# state[action] = 1
		state_energies = [0] * len(room_states)
		for i, room in enumerate(room_states):
			state_energies[i] = room_energy[room][self.t]
		s_ = np.array(state + state_energies + [self.t])
		return s_, reward, done

	def render(self):
		time.sleep(0.01)
		self.update()
		# for c in range(0, NWC_W * UNIT, UNIT):
		#     x0, y0, x1, y1 = c, 0, c, NWC_H * UNIT
		#     self.canvas.create_line(x0, y0, x1, y1)
		# for r in range(0, NWC_H * UNIT, UNIT):
		#     x0, y0, x1, y1 = 0, r, NWC_W * UNIT, r
		#     self.canvas.create_line(x0, y0, x1, y1)

def run_maze():
	step = 0
	for episode in range(300):
		# initial observation
		observation = env.reset()

		while True:
			# fresh env
			env.render()


			step += 1
	print('game over')
	env.destroy()

if __name__ == "__main__":
	env = NWC()
	env.after(100, run_maze)
	env.mainloop()