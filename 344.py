import math, itertools, copy
import memoize

EMPTY = '_'
USELESS_COIN = 'U'
SILVER_COIN = '$'

GO_LEFT = 0
POCKET = 1

class State:
	def __cmp__(self, other):
		if self.position == other.position and self.won == other.won and self.to_play == other.to_play:
			return 0
		return -1
	def __hash__(self):
		return hash((tuple(self.position), self.won, self.to_play))

class Move:
	pass


def iter_over_possible_starting_positions():
	set_positions = set(range(N))
	useless_positions_combs = itertools.combinations(xrange(N), U)
	for comb in useless_positions_combs:
		position = [EMPTY for _ in xrange(N)]
		for pos in comb:
			position[pos] = USELESS_COIN
# Position decided
		silver_positions = set_positions - set(comb)
		last_silver_pos = None
		for pos in silver_positions:
			position[pos] = SILVER_COIN
			if last_silver_pos is not None:
				position[last_silver_pos] = EMPTY
			yield copy.deepcopy(position)
			last_silver_pos = pos

def is_state_won_in_one_move(state):
	i = 0
	for i in xrange(len(state.position)):
		if state.position[i] == USELESS_COIN:
			return False
		if state.position[i] == SILVER_COIN:
			return True

def make_move_to_state(state, move):
	state = copy.deepcopy(state)
	if move.typ == GO_LEFT:
		to_move = state.position[move.index]
		assert to_move != EMPTY
		state.position[move.index] = EMPTY
		assert state.position[move.index - move.how_long] == EMPTY
		state.position[move.index - move.how_long] = to_move
	elif move.typ == POCKET:
		to_pocket = state.position[move.index]
		assert to_pocket != EMPTY
		if to_pocket == SILVER_COIN:
			state.won = state.to_play
		state.position[move.index] = EMPTY
	if state.to_play == 0:
		state.to_play = 1
	elif state.to_play == 1:
		state.to_play = 0
	return state

def iter_over_possible_moves(position):
	for ind in xrange(len(position)):
		if position[ind] in (USELESS_COIN, SILVER_COIN):
			for how_long in itertools.count(1):
				if ind - how_long < 0:
					break
				if position[ind - how_long] in (USELESS_COIN, SILVER_COIN):
					break
				move = Move(); move.typ = GO_LEFT; move.index = ind; move.how_long = how_long
				yield move
			pocket_allowed = True
			for other_ind in xrange(ind - 1, -1, -1):
				if position[other_ind] != EMPTY:
					pocket_allowed = False
					break
			if pocket_allowed:
				move = Move(); move.typ = POCKET; move.index = ind; move.how_long = None
				yield move

def is_state_won(state):
	#print 'received by is_state_won:', state.__dict__
	assert state.to_play == 0
	if state.won == 1:
		#print 'returning False'
		return False
	if is_state_won_in_one_move(state):
		#print 'returning True'
		return True
	#print
	#print state.position, list(_.__dict__ for _ in iter_over_possible_moves(state.position))
	#print
	for my_move in iter_over_possible_moves(state.position):
		#print 'considering my_move: ', my_move.__dict__
		winning_move = my_move
		found_winning_move = True
		cstate = make_move_to_state(state, my_move)
		for opp_move in iter_over_possible_moves(cstate.position):
			#print 'considering opp_move: ', opp_move.__dict__
			ccstate = make_move_to_state(cstate, opp_move)
			if not is_state_won(ccstate):
				found_winning_move = False
		if found_winning_move:
			#print 'returning True'
			#print 'winning move: ', winning_move.__dict__, 'on:', state.position
			return True
	#print 'returning False'
	return False

is_state_won = memoize.MemoizedFunction(is_state_won, int(1e5), record_stats = True)

def iter_over_positions_that_win_in_next_turn():
	for silver_pos in xrange(N):
		for comb in itertools.combinations(range(silver_pos + 1, N), U):
			position = [EMPTY for _ in xrange(N)]
			position[silver_pos] = SILVER_COIN
			for pos in comb:
				position[pos] = USELESS_COIN
			yield position

def silver_index_sort_f(p):
	return -p.index(SILVER_COIN)

def print_pos_iterable(pos_iterable):
	for key, group in itertools.groupby(sorted(sorted(pos_iterable), key = silver_index_sort_f), silver_index_sort_f):
		for _ in group:
			print ' '.join(_)
		print

def produce_series(length):
	global N
	keep_N = N
	for n in xrange(N, N + length):
		nw = 0
		N = n
		for posi, position in enumerate(iter_over_possible_starting_positions()):
			state = State(); state.position = position; state.to_play = 0; state.won = None
			won = is_state_won(state)
			if not won:
				nw += 1
		print N, U, nw, posi + 1
	N = keep_N
			

				
# state = State()
# state.position = [USELESS_COIN, EMPTY, SILVER_COIN]
# state.to_play = 0
# state.won = None
# 
# print state.__dict__
# for move in iter_over_possible_moves(state.position):
# 	cstate = make_move_to_state(state, move)
# 	print
# 	print 'state before', state.__dict__
# 	print 'move        ', move.__dict__
# 	print 'state after ', cstate.__dict__
# 	
# 	
# print
# print state.__dict__
# print is_state_won(state)

def bin_coeff(n, k):
	arithm = math.factorial(n)
	paron = math.factorial(k) * math.factorial(n - k)
	return arithm / paron
	
N = 4
U = 1

if 0:
	produce_series(10)

if 0:
	print_pos_iterable(iter_over_positions_that_win_in_next_turn())

if 1:
	nw = 0
	to_print = [ ]
	for posi, position in enumerate(iter_over_possible_starting_positions()):
		state = State(); state.position = position; state.to_play = 0; state.won = None
		won = is_state_won(state)
		if won:
			nw += 1
		to_print.append((state.position, won))

#print nw

	print 'N =', N
	print 'U =', U
	print
	i = -1
	break_point = bin_coeff(N - 1, U)
	for pos, won in sorted(to_print, key = lambda t: t[0].index(SILVER_COIN)):
		i += 1
		if i % break_point == 0:
			print '=' * (N * 2 + 4)
		print ' '.join(pos), '...L' if not won else ''
	print
	print len(to_print) , posi + 1

#print is_state_won.total_cache_hits, is_state_won.total_calls
