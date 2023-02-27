from typing import List, Dict

class PartyPlanner():
    """
    This module takes following as inputs and provides methods
    to easily perform planning tasks such as seating plan etc..

    1. Number of tables
    2. Guest List
    3. Seating Preferences
    """

    def __init__(self, num_tables: int, 
                    guest_list: List[str], 
                    planner_preferences: Dict[str, List[str]] = None
                ):
        self.num_tables = num_tables
        self.guest_list = guest_list
        self.planner_preferences = planner_preferences


    def _process_seating_preferences(self):
        """
        Separtes the planning preferences into 
        Pairing and Avoid dictionaries for each guest
        """
        if not self.planner_preferences:
            return {}, {}
    
        pair = {}
        avoid = {}

        def __organize_lists_into_dict(out_dict, in_list):
            """
            Iterates on the lists for each preference
            """
            for e in in_list:
                if not out_dict.get(e):
                    out_dict[e] = []
                others = [g for g in in_list if g != e]
                for other in others:
                    out_dict[e].append(other) 
        
        for plan in self.planner_preferences:
            if plan["preference"] == 'pair':
                __organize_lists_into_dict(pair, plan["guests"])
            elif plan["preference"] == 'avoid':
                __organize_lists_into_dict(avoid, plan["guests"])
            else:
                print(f"{plan['preference']} is not a valid preference. skipping...")
        
        return pair, avoid


    def gen_seating_chart(self):
        """
        Generates the seating chart by taking number of tables, guest list 
        and planner preferences into account
        """
        # Initialize empty seating chart
        seating_chart = {f"table_{i}": [] for i in range(1, self.num_tables + 1)}

        # process planner preferences
        pair,  avoid = self._process_seating_preferences()
        # FOR DEBUG MODE # 
        ## print(f"Pairing preferences by guest {pair}")
        ## print(f"Avoidance preferences by guest {avoid}")

        # Sort guests by number of preferences
        def __count_prefs(guest):
            return len(pair.get(guest, [])) + len(avoid.get(guest, []))
        guest_list_sorted = sorted(self.guest_list, key=__count_prefs, reverse=True)

        # Seat guests at tables based on preferences
        for guest in guest_list_sorted:
            table_choices = [f"table_{i}" for i in range(1, self.num_tables + 1)]
            for table_num in seating_chart:
                if guest in seating_chart[table_num]:
                    table_choices.remove(table_num)
                elif any(g in seating_chart[table_num] for g in avoid.get(guest, [])):
                    table_choices.remove(table_num)
            for g in pair.get(guest, []):
                for table_num in seating_chart:
                    if g in seating_chart[table_num] and table_num in table_choices:
                        table_choices = [table_num]
                        break
            if len(table_choices) > 0:
                table_num = table_choices[0]
                seating_chart[table_num].append(guest)
            # FOR DEBUG MODE #
            ## print(f"Guest: {guest}, Chart: {seating_chart}, Choices: {table_choices}")

        return seating_chart
