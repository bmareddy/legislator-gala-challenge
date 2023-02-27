from modules.party_planner import PartyPlanner

###########################################
# Case 1: No Preferences 
###########################################
us_senate_gala_no_pref = PartyPlanner(
    num_tables = 2,
    guest_list = ["McConnell", "Schumer", "Cornyn", "Durbin"],
)
print(us_senate_gala_no_pref.gen_seating_chart())
#-- Output: {'table_1': ['McConnell', 'Schumer', 'Cornyn', 'Durbin'], 'table_2': []}

###########################################
# Case 2: Pair Dems and Rep
# Note: Since there is no avoid prefs,
#       all are seated together similar to case 1
# Opportunity to expand scope of the problem to require
# mutually exclusive pairing getting separate tables
###########################################
us_senate_gala_D_R = PartyPlanner(
    num_tables = 2,
    guest_list = ["McConnell", "Schumer", "Cornyn", "Durbin"],
    planner_preferences=[
        {
            "preference": "pair",
            "guests": ["McConnell", "Cornyn"]
        },
        {
            "preference": "pair",
            "guests": ["Schumer", "Durbin"]
        },
    ]
)
print(us_senate_gala_D_R.gen_seating_chart())
#-- Output: {'table_1': ['McConnell', 'Schumer', 'Cornyn', 'Durbin'], 'table_2': []}

###########################################
# Case 3: Enter Bernie Sanders. 
#           Schumer doesn't want to sit with Bernie
# Note: Poor Bernie ends up sitting alone
# Opportunity to expand scope of the problem to require
# that no one sits alone
###########################################
us_senate_gala_sanders = PartyPlanner(
    num_tables = 3,
    guest_list = ["McConnell", "Schumer", "Cornyn", "Durbin", "Sanders"],
    planner_preferences=[
        {
            "preference": "pair",
            "guests": ["McConnell", "Cornyn"]
        },
        {
            "preference": "pair",
            "guests": ["Schumer", "Durbin"]
        },
        {
            "preference": "avoid",
            "guests": ["Schumer", "Sanders"]
        }
    ]
)
print(us_senate_gala_sanders.gen_seating_chart())
#-- Output: {'table_1': ['Schumer', 'McConnell', 'Cornyn', 'Durbin'], 'table_2': ['Sanders'], 'table_3': []}

###########################################
# Case 4: Schumer gets picky
###########################################
us_senate_gala_avoid_0 = PartyPlanner(
    num_tables = 3,
    guest_list = ["McConnell", "Schumer", "Cornyn", "Durbin", "Sanders"],
    planner_preferences=[
        {
            "preference": "pair",
            "guests": ["McConnell", "Cornyn"]
        },
        {
            "preference": "avoid",
            "guests": ["Schumer", "Cornyn"]
        },
        {
            "preference": "avoid",
            "guests": ["Schumer", "Sanders"]
        }
    ]
)
print(us_senate_gala_avoid_0.gen_seating_chart())
#-- Output: {'table_1': ['Schumer', 'Durbin'], 'table_2': ['Cornyn', 'McConnell', 'Sanders'], 'table_3': []}

###########################################
# Case 5: Sanders is not the popular kid
# Note: Since McConnell wants to avoid Sanders
#       his preference to pair with Cornyn is
#       not respected
###########################################
us_senate_gala_avoid_1 = PartyPlanner(
    num_tables = 3,
    guest_list = ["McConnell", "Schumer", "Cornyn", "Durbin", "Sanders"],
    planner_preferences=[
        {
            "preference": "pair",
            "guests": ["McConnell", "Cornyn"]
        },
        {
            "preference": "avoid",
            "guests": ["Schumer", "Cornyn"]
        },
        {
            "preference": "avoid",
            "guests": ["Schumer", "Sanders"]
        },
        {
            "preference": "avoid",
            "guests": ["McConnell", "Sanders"]
        },        
    ]
)
print(us_senate_gala_avoid_1.gen_seating_chart())
#-- Output: {'table_1': ['McConnell', 'Schumer', 'Durbin'], 'table_2': ['Cornyn', 'Sanders'], 'table_3': []}

###########################################
# Case 5: Sanders is not the popular kid
# Note: Schumer and Sanders end up at their
#       tables, rightfully so
###########################################
us_senate_gala_avoid_2 = PartyPlanner(
    num_tables = 3,
    guest_list = ["McConnell", "Schumer", "Cornyn", "Durbin", "Sanders"],
    planner_preferences=[
        {
            "preference": "pair",
            "guests": ["McConnell", "Cornyn"]
        },
        {
            "preference": "avoid",
            "guests": ["Schumer", "Cornyn"]
        },
        {
            "preference": "avoid",
            "guests": ["Schumer", "Sanders"]
        },
        {
            "preference": "avoid",
            "guests": ["McConnell", "Sanders"]
        }, 
        {
            "preference": "avoid",
            "guests": ["Cornyn", "Sanders"]
        },        
    ]
)
print(us_senate_gala_avoid_2.gen_seating_chart())
#-- Output: {'table_1': ['Cornyn', 'McConnell', 'Durbin'], 'table_2': ['Sanders'], 'table_3': ['Schumer']}

###########################################
# Case 6: Party Line
###########################################
us_senate_gala_avoid_3 = PartyPlanner(
    num_tables = 3,
    guest_list = ["McConnell", "Schumer", "Cornyn", "Durbin", "Sanders"],
    planner_preferences=[
        {
            "preference": "pair",
            "guests": ["McConnell", "Cornyn"]
        },
        {
            "preference": "pair",
            "guests": ["Schumer", "Durbin"]
        },
        {
            "preference": "avoid",
            "guests": ["Schumer", "Cornyn"]
        },
        {
            "preference": "avoid",
            "guests": ["Schumer", "Sanders"]
        },
        {
            "preference": "avoid",
            "guests": ["McConnell", "Sanders"]
        }, 
        {
            "preference": "avoid",
            "guests": ["Cornyn", "Sanders"]
        },        
    ]
)
print(us_senate_gala_avoid_3.gen_seating_chart())
#-- Output: {'table_1': ['Schumer', 'Durbin'], 'table_2': ['Cornyn', 'McConnell'], 'table_3': ['Sanders']}
