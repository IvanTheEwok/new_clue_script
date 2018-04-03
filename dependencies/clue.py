class Clue(object):

    """
    This class sets up the clue, and asks for three attributes: tier, value and number of stages.
    """

    def __init__(self, tier="", value="", stages=""):
        """
        This method checks if the class' attributes are given. If they're not, the user is prompted to input these attributes.
        """

        if not tier:
            tier = self.get_tier()    #Prompts the user for a tier.

        if not value:
            value = self.get_value()    #Prompts the user for a value.

        if not stages:
            stages = self.get_stages()    #Prompts the user for the number of stages.

        self.tier = tier
        self.value = value
        self.stages = stages

    def get_tier(self):
        """
        This function prompts the user for a difficulty
        """

        while True:
            tier = raw_input("Please enter the clue tier: ")
            if tier.lower() not in ["easy", "medium", "hard", "elite", "master"]:    #Makes sure the user inputs an actual tier.
                print "I'm sorry, {} is not a valid input.".format(tier.lower())
            else:
                return tier.lower()

    def get_value(self):
        """
        This function prompts the user for a total value of the loot from the clue. It also checks if the input is a number, or not.
        """

        while True:
            value = raw_input("Please enter the loots total value: ")
            try:
                int(value)    #Checks if the input is a number, and not text.
                return value
            except:    #If the input is text.
                print "I'm sorry, {} is not a valid input.".format(value)

    def get_stages(self):
        """
        This function prompts the user to input the number of stages the clue had.
        """

        while True:
            stages = raw_input("Please enter the number of stages: ")
            try:    #Checks if the input is a number, and not text.
                int(stages)
                return stages
            except:    #If the input is text.
                print "I'm sorry, {} is not a valid input.".format(stages)
