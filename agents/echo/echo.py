from parlai.core.agents import Agent


class EchoAgent(Agent):
    def __init__(self, opt):
        super().__init__(opt)
        self.id = self.__class__.__name__
        self.heard = None

    def observe(self, observation):
        self.heard = observation['text']
        return observation

    def act(self):
        return {
            'id': self.id,
            'text': self.heard
        }
