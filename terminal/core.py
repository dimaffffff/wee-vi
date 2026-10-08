from common import structures as st

_terminalState: list[list[st.character]] = []
_fontSize: int = -1


def init(textAmount: st.vector2):

    #populate the terminal state, this assumes that the terminal state is empty
    for _ in range(int(textAmount.x)):
        _terminalState.append([])
        for _ in range(int(textAmount.y)):
            _terminalState[-1].append(st.character())

