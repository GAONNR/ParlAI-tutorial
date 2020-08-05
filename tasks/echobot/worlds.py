from parlai.core.worlds import World


class EchoBotWorld(World):
    """
    Simple Echo Bot.
    See https://blog.g40n.xyz/posts/2020-07-30-parlai-tutorial-2.html for more details.
    (Korean)
    """

    def __init__(self, opt, agents=None):
        super().__init__(opt)
        self.agents = agents

    def parley(self):
        human = self.agents[0]
        bot = self.agents[1]

        human_act = human.act()
        bot.observe(human_act)
        bot_act = bot.act()
        human.observe(bot_act)
