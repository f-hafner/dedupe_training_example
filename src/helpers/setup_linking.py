import src.helpers.comparator_functions as cf

# define fields for linking
fields = [{"field": "firstname", "variable name": "firstname", "type": "String", "has missing": False},
            {"field": "firstname", "variable name": "same_firstname", "type": "Exact"},
            {"field": "lastname", "variable name": "lastname", "type": "String", "has missing": False},
            {"field": "lastname", "variable name": "same_lastname", "type": "Exact"},
            {"field": "middlename", "variable name": "middlename", "type": "String", "has missing": True},
            {"field": "year_range", "variable name": "year_range", "type": "Custom", "comparator": cf.compare_range_from_tuple, "has missing": True},
            {"field": "main_us_institutions_year", "variable name": "main_inst_year", "type": "Custom", "comparator": cf.set_of_tuples_distance_overall, "has missing": True},
            {"field": "main_us_institutions_year", "variable name": "main_inst_similarity", "type": "Custom", "comparator": cf.set_of_tuples_distance_string, "has missing": True},
            {"field": "main_us_institutions_year", "variable name": "main_inst_year_similarity", "type": "Custom", "comparator": cf.set_of_tuples_distance_number, "has missing": True},
            {'type': 'Interaction', 'interaction variables': ['main_inst_year_similarity', 'firstname']},
            {'type': 'Interaction', 'interaction variables': ['main_inst_year_similarity', 'lastname']},
            {'type': 'Interaction', 'interaction variables': ['main_inst_year_similarity', 'firstname']},
            {'type': 'Interaction', 'interaction variables': ['main_inst_year_similarity', 'lastname']},
            {"field": "all_us_institutions_year", "variable name": "all_inst_year", "type": "Custom", "comparator": cf.set_of_tuples_distance_overall, "has missing": True},
            {"field": "all_us_institutions_year", "variable name": "all_inst_similarity", "type": "Custom", "comparator": cf.set_of_tuples_distance_string, "has missing": True},
            {"field": "all_us_institutions_year", "variable name": "all_inst_year_similarity", "type": "Custom", "comparator": cf.set_of_tuples_distance_number, "has missing": True}
        ] 
