import templa 
from datetime import datetime

def create_date(variables):
    # フックを追加することでiniファイルの値を色々加工したり色々できます
    # フック関数は引数としてiniファイルのパラメータ(辞書型)が渡ってきます。
    # フック関数の戻り値は引数で貰ったiniファイルの変数を返してください。
    variables["vhost"]["create_date"] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return variables


