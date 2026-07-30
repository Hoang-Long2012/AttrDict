from collections.abc import Mapping
__version__ = "0.1.0"
__all__ = ["AttrDict"]
class AttrDict(dict):
	"""
Dictionary with attribute-style access.

Note:
Attribute syntax (``.``) follows normal Python attribute lookup. If a name
matches an existing attribute or method, it refers to that attribute
instead of a dictionary key. Use item access (``[]``) for conflicting keys.
"""
	def __init__(self, *args, **kwargs):
		super().__init__()
		data = dict(*args, **kwargs)
		for key, value in data.items():
			self[key] = self._convert(value)
	def _key_exists(self, key):
		if key not in self:
			raise AttributeError(f"{type(self).__name__!r} object has no attribute {key!r}")
	@classmethod
	def _convert(cls, value):
		if isinstance(value, cls):
			return value
		if isinstance(value, Mapping):
			return cls(value)
		if isinstance(value, list):
			return [cls._convert(v) for v in value]
		if isinstance(value, set):
			return {cls._convert(v) for v in value}
		if isinstance(value, frozenset):
			return frozenset(cls._convert(v) for v in value)
		if isinstance(value, tuple):
			return tuple(cls._convert(v) for v in value)
		return value
	def __getattr__(self, key):
		"""Return the value of the named attribute."""
		self._key_exists(key)
		return self[key]
	def __setattr__(self, key, value):
		if hasattr(type(self), key):
			super().__setattr__(key, value)
		else:
			self[key] = value
	def __delattr__(self, key):
		if hasattr(type(self), key):
			super().__delattr__(key)
		else:
			self._key_exists(key)
			del self[key]
	def __setitem__(self, key, value):
		value = self._convert(value)
		super().__setitem__(key, value)
	def __dir__(self):
		return sorted(set(super().__dir__()) | set(self.keys()))
	def __repr__(self):
		return f"{type(self).__name__}({super().__repr__()})"
	def copy(self):
		"""Return a shallow copy of the AttrDict."""
		return type(self)(self)