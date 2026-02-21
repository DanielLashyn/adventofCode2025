class SInt:
	def __init__(self, value):
		if not isinstance(value, int):
			raise TypeError("SInt must be initialized with an int")
		self.value = value

	# -------------------
	# Representation
	# -------------------
	def __repr__(self):
		return str(self.value)

	def __str__(self):
		return str(self.value)

	def __int__(self):
		return self.value

	def __hash__(self):
		return hash(self.value)

	# -------------------
	# Indexing
	# -------------------
	def __getitem__(self, key):
		s = str(self.value)
		result = s[key]
		return int(result) if isinstance(result, str) else result

	def __setitem__(self, key, new_value):
		s = list(str(self.value))

		if isinstance(key, slice):
			s[key] = list(str(new_value))
		else:
			if not isinstance(new_value, int) or not (0 <= new_value <= 9):
				raise ValueError("Single digit assignment must be 0–9")
			s[key] = str(new_value)

		self.value = int("".join(s))

	# -------------------
	# Internal helper
	# -------------------
	def _coerce(self, other):
		if isinstance(other, SInt):
			return other.value
		if isinstance(other, int):
			return other
		return NotImplemented

    # -------------------
    # Other
    # -------------------
	def __len__(self):
		return len(str(self.value))
    
	def isEmpty(self):
		return len(str(self.value)) == 0

	# -------------------
	# Arithmetic
	# -------------------
	def __add__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(self.value + other)

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(self.value - other)

	def __rsub__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(other - self.value)

	def __mul__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(self.value * other)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __floordiv__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(self.value // other)

	def __rfloordiv__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(other // self.value)

	def __mod__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(self.value % other)

	def __rmod__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(other % self.value)

	def __pow__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(self.value ** other)

	def __rpow__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return SInt(other ** self.value)

	# -------------------
	# Comparisons
	# -------------------
	def __eq__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return False
		return self.value == other

	def __lt__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return self.value < other

	def __le__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return self.value <= other

	def __gt__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return self.value > other

	def __ge__(self, other):
		other = self._coerce(other)
		if other is NotImplemented:
			return NotImplemented
		return self.value >= other
