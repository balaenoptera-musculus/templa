#!python
# -*- coding: utf-8 -*-
import argparse
import configparser
import importlib
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
    val = configparser.ConfigParser()
    val.read(args.ini)

    for section in val.sections():
      for key in val[section]:
        if section not in variables:
          variables[section] = {}

        variables[section][key] = val[section][key]


  # フック処理をインポートして実行
  if args.functions != None:
    functions = importlib.import_module(args.functions)

    config = configparser.ConfigParser()
    config.read(args.config)

    for section in config.sections():
      if config[section]["priority"] not in hooks:
        hooks["priority"] = {}

        hooks["priority"]["callback"] = config[section]["callback"]


    for priority in hooks:
      variables = getattr(functions, hooks[priority]["callback"])(variables)

  print(template.render(val))


if __name__ == "__main__":
  main()
