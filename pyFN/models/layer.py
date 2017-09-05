"""FrameNet Layer class."""

__all__ = ['Layer']


class Layer():
    """FrameNet Layer class."""

    def __init__(self, name, rank=None):
        """Constructor."""
        self._name = name
        self._rank = rank

    @property
    def name(self):
        """Return the lexunit name."""
        return self._name

    @property
    def rank(self):
        """Return the layer rank."""
        return self._rank

    @rank.setter
    def rank(self, rank):
        self._rank = rank

    def __hash__(self):
        return hash((self._name, self._rank))

    def __eq__(self, other):
        return self._name == other.name and self._rank == other.rank

    def __ne__(self, other):
        return not self == other
