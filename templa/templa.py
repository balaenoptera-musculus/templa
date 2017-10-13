#!python
# -*- coding: utf-8 -*-
import argparse
import configparser
import importlib
import sys
from jinja2 import Environment, FileSystemLoader

def main():
  variables = {}
  hooks= {}
  parser = argparse.ArgumentParser()

  # テンプレートのパス
  parser.add_argument("path", help="input template directry")

  # テンプレートのパス
  parser.add_argument("template", help="input template file")

  # テンプレートの設定ファイル
  parser.add_argument("-i", "--ini", help="ini file(.ini)")

  # フックインポート
  parser.add_argument("-f", "--functions", help="function package name")

  # フックインポート
  parser.add_argument("-c", "--config", help="config file name(.ini)")

  args = parser.parse_args()

  # テンプレート読み込み
  env = Environment(loader=FileSystemLoader(args.path, encoding='utf8'))
  template = env.get_template(args.template)

  # iniファイル読み込み
  if args.ini != None:
    ini_val = configparser.ConfigParser()
    ini_val.read(args.ini, encoding="utf-8")

    for section in ini_val.sections():
      for key in ini_val[section]:
        if section not in variables:
          variables[section] = {}

        variables[section][key] = ini_val[section][key]
 

  # フック処理をインポートして実行
  if args.functions != None:
    sys.path.append(args.path)
    functions = importlib.import_module(args.functions)

    ini_config = configparser.ConfigParser()
    ini_config.read(args.config, encoding="utf-8")

    for section in ini_config.sections():
      if ini_config[section]["priority"] not in hooks:
        hooks["priority"] = {}

        hooks["priority"]["hook"] = ini_config[section]["hook"]


    for priority in hooks:
      variables = getattr(functions, hooks[priority]["hook"])(variables)

  print(template.render(variables))


if __name__ == "__main__":
  main()
