datapath = "/mnt/ssd/"
databasepath = datapath + "AcademicGraph/"
db_file = f"{databasepath}AcademicGraph.sqlite" 


def is_numeric(a):
    "Check if a is numeric."
    return isinstance(a, int) | isinstance(a, float)


def convert_to_tuple_of_tuples(s):
    "Convert string to set of tuples"
    s = [x.split("//") for x in s.split(";")]
    s = [tuple([int(x[0]), x[1]]) for x in s]
    return tuple(s)


def convert_to_year_range(s):
    "Convert s to tuple of year ranges"
    if isinstance(s, str):
        s = s.split(";")
        s = tuple([int(x) for x in s])
    else:
        s = (int(s),)
    return s

