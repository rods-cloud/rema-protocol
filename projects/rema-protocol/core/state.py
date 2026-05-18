class SystemState:
    def __init__(self):
        self.active_agent = None
        self.status = "BOOTING"

    def set_agent(self, agent_name):
        self.active_agent = agent_name

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def get_agent(self):
        return self.active_agent