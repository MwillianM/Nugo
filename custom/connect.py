import pymssql as sql
from configparser import ConfigParser
from json import dump


def getMetadata(confile, outfile):
  config = ConfigParser()
  confile = config.read(confile)
  config = config['MSSQL']
  with sql.connect(*(i for i in config.values())) as conn:
    with conn.cursor() as cursor:
      cursor.execute(
        "select table_name, column_name from information_schema.columns order by ordinal_position")
      query = cursor.fetchall()

  metadata = {}
  for table, column in query:
      metadata.setdefault(table, []).append(column)

  with open(outfile, 'w') as f:
    dump(metadata, f)


if __name__ == '__main__':
  inp = '../config.ini'
  out = '../metadata.json'
  getMetadata(inp, out)
