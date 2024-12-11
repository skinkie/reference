def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod



my_import('netex_to_db.main')(['/tmp/test.xml.gz'], '/tmp/test.duckdb')